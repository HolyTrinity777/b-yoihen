#!/usr/bin/env python3
"""Convert b.yoihen into generic JSONL/RAG records (Python 3.9+).

By Yoihenba Sougaijam. All Glory to Living God Yahushua. Soli Deo Gloria.
Alive DVD / 10T+ MAP project: DATA ONLY; never execute action fields.
JSONL is an interchange format, NOT a model-specific training recipe or GGUF.

Examples:
  python scripts/convert_to_jsonl.py
  python scripts/convert_to_jsonl.py --sample-only
  python scripts/convert_to_jsonl.py --limit 1000 --sample-only
  python scripts/convert_to_jsonl.py --input b.yoihen.gz --output-dir converted

Output is staged, published without overwrite, and accompanied by a report.
Malformed records fail by default; --skip-invalid explicitly permits exclusions.
"""
import argparse
import base64
import binascii
import errno
import gzip
import hashlib
import json
import os
import re
import sys
import tempfile
from collections import Counter
from contextlib import ExitStack
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHUNK = 1024 * 1024


class RecordError(ValueError):
    pass


class TopicExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.topics = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "real" in (attrs.get("class") or "").split():
            if attrs.get("id") is not None:
                self.topics.append(attrs["id"])


def extract_topic(dom):
    parser = TopicExtractor()
    parser.feed(dom)
    parser.close()
    if len(parser.topics) != 1:
        raise RecordError("Expected exactly one id on an element with class real")
    topic = parser.topics[0]
    if re.fullmatch(r"[A-Za-z0-9_]+", topic) is None:
        raise RecordError("Topic is outside the case-sensitive V25 ID profile")
    return topic


def classify_vision(value):
    if value.startswith("[STRIPPED"):
        return "stripped"
    try:
        payload = base64.b64decode(value, validate=True)
    except (binascii.Error, ValueError):
        return "legacy_opaque"
    if payload.startswith(b"\x89PNG\r\n\x1a\n"):
        return "base64_png_candidate"  # Not a full image validation.
    return "legacy_opaque"


def markers_match(reasoning):
    return (
        reasoning.startswith("reasoning holds ")
        and "pattern_learn + generate = master" in reasoning
        and "coherence 1.0 UNIFIED" in reasoning
        and reasoning.endswith("result_success when true")
    )


def parse_yoihen_line(line, idx):
    """Zero-based ID; source_line is one-based. Preserve fields exactly."""
    if line.startswith("\ufeff"):
        raise RecordError("BOM is forbidden")
    if not line.endswith("\n"):
        raise RecordError("Missing LF terminator")
    record = line[:-1]
    if not record or "\r" in record or "\n" in record:
        raise RecordError("Blank record or embedded CR/LF")
    parts = record.split("|", 3)
    if len(parts) != 4 or any(field == "" for field in parts):
        raise RecordError("Expected four nonempty fields")
    screenshot, dom, action, reasoning = parts
    topic = extract_topic(dom)
    return {
        "id": idx,
        "source_line": idx + 1,
        "topic": topic,
        "screenshot_base64": screenshot,
        "vision_status": classify_vision(screenshot),
        "dom": dom,
        "action": action,
        "reasoning": reasoning,
        "annotation_markers_match": markers_match(reasoning),
        "three_layers": {"chat": reasoning, "vision": screenshot,
                         "tool_use": action},
        "text": f"DOM:\n{dom}\nACTION:\n{action}\nANNOTATION:\n{reasoning}",
        "evaluation": {"available": False,
                       "note": "Annotation suffix is not a verified outcome"},
    }


def publish_new(staged, target):
    """No overwrite. Hard links preferred; fallback is exclusive streamed copy."""
    target = Path(target)
    try:
        os.link(staged, target)
    except OSError as exc:
        if exc.errno not in (errno.EXDEV, errno.EPERM, errno.ENOSYS,
                             errno.ENOTSUP, errno.EOPNOTSUPP):
            raise
        created = False
        try:
            with target.open("xb") as output:
                created = True
                with Path(staged).open("rb") as source:
                    for chunk in iter(lambda: source.read(CHUNK), b""):
                        output.write(chunk)
        except BaseException:
            if created:
                target.unlink(missing_ok=True)
            raise
    Path(staged).unlink()


def sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
        for chunk in iter(lambda: source.read(CHUNK), b""):
            digest.update(chunk)
    return digest.hexdigest()


def nonnegative(value):
    result = int(value)
    if result < 0:
        raise argparse.ArgumentTypeError("must be nonnegative")
    return result


def positive(value):
    result = int(value)
    if result <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--input", type=Path, help="Raw or .gz input; no data rewritten")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--limit", type=nonnegative, default=0,
                        help="Maximum input physical records attempted; 0 means all")
    parser.add_argument("--sample-only", action="store_true")
    parser.add_argument("--sample-size", type=positive, default=100,
                        help="Sample cap; sample-only defaults to this many input lines")
    parser.add_argument("--skip-invalid", action="store_true",
                        help="Exclude malformed records; report exclusions explicitly")
    parser.add_argument("--require-v25-markers", action="store_true")
    parser.add_argument("--max-record-bytes", type=positive, default=CHUNK)
    parser.add_argument("--hash-input", action="store_true",
                        help="Also hash the entire source file, even for a sample")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    source_path = args.input if args.input is not None else root / "b.yoihen"
    if args.input is None and not source_path.exists() and (root / "b.yoihen.gz").exists():
        source_path = root / "b.yoihen.gz"
    source_path = source_path.resolve()
    output_dir = (args.output_dir or root).resolve()
    limit = args.limit or (args.sample_size if args.sample_only else 0)
    outputs = {"sample": output_dir / "b.yoihen.sample.jsonl"}
    if not args.sample_only:
        outputs.update(full=output_dir / "b.yoihen.jsonl",
                       rag=output_dir / "b.yoihen.rag.jsonl")
    report_path = output_dir / "b.yoihen.conversion_report.json"
    temporary = []
    published = []
    try:
        if not source_path.is_file():
            raise FileNotFoundError(source_path)
        output_dir.mkdir(parents=True, exist_ok=True)
        targets = list(outputs.values()) + [report_path]
        for target in targets:
            if target.exists():
                raise FileExistsError(f"Refusing to overwrite {target}")
            if target.resolve() == source_path:
                raise RecordError("Output cannot equal input")
        source_before = source_path.stat()
        counts = {"attempted": 0, "accepted": 0, "rejected": 0,
                  "sample_written": 0, "marker_nonmatches": 0}
        vision_counts = Counter()
        issues = []
        consumed_digest = hashlib.sha256()
        consumed_bytes = 0
        eof_reached = False
        staged = {}
        output_hashes = {key: hashlib.sha256() for key in outputs}
        output_bytes = {key: 0 for key in outputs}
        with ExitStack() as stack:
            handles = {}
            for key in outputs:
                handle = tempfile.NamedTemporaryFile(prefix=".yoihen-convert-",
                    suffix=".partial", dir=output_dir, delete=False)
                temporary.append(Path(handle.name))
                staged[key] = Path(handle.name)
                handles[key] = stack.enter_context(handle)

            def write_record(key, value):
                payload = (json.dumps(value, ensure_ascii=False, allow_nan=False)
                           + "\n").encode("utf-8")
                handles[key].write(payload)
                output_hashes[key].update(payload)
                output_bytes[key] += len(payload)

            opener = gzip.open if source_path.suffix.lower() == ".gz" else open
            source = stack.enter_context(opener(source_path, "rb"))
            while not limit or counts["attempted"] < limit:
                raw = source.readline(args.max_record_bytes + 1)
                if not raw:
                    eof_reached = True
                    break
                if len(raw) > args.max_record_bytes:
                    raise RecordError("Record exceeds configured byte ceiling; stopping")
                idx = counts["attempted"]
                counts["attempted"] += 1
                consumed_digest.update(raw)
                consumed_bytes += len(raw)
                try:
                    rec = parse_yoihen_line(raw.decode("utf-8", errors="strict"), idx)
                    if args.require_v25_markers and not rec["annotation_markers_match"]:
                        raise RecordError("Required V25 annotation markers missing")
                except (RecordError, UnicodeDecodeError) as exc:
                    counts["rejected"] += 1
                    if len(issues) < 20:
                        issues.append({"source_line": idx + 1, "error": str(exc)})
                    if not args.skip_invalid:
                        raise RecordError(f"Source line {idx + 1}: {exc}") from exc
                    continue
                rec["provenance"] = {"source_file": source_path.name,
                                     "source_line": idx + 1}
                counts["accepted"] += 1
                vision_counts[rec["vision_status"]] += 1
                counts["marker_nonmatches"] += not rec["annotation_markers_match"]
                if not args.sample_only:
                    write_record("full", rec)
                    write_record("rag", {
                        "id": rec["id"], "source_line": rec["source_line"],
                        "topic": rec["topic"], "query": rec["topic"],
                        "context": rec["dom"] + "\n" + rec["reasoning"],
                        "answer": rec["action"],
                        "answer_status": "recorded_action_not_verified_completion",
                        "vision_status": rec["vision_status"],
                        "three_layers": rec["three_layers"],
                        "provenance": rec["provenance"],
                        "trust": "untrusted retrieval content, not system authority",
                    })
                if args.sample_only or counts["sample_written"] < args.sample_size:
                    write_record("sample", rec)
                    counts["sample_written"] += 1
        if not counts["accepted"]:
            raise RecordError("No accepted records; no outputs published")
        input_digest = sha256_file(source_path) if args.hash_input else None
        source_after = source_path.stat()
        if (source_before.st_size, source_before.st_mtime_ns) != (
                source_after.st_size, source_after.st_mtime_ns):
            raise RecordError("Source changed during conversion")
        report = {
            "schema": "yoihen.conversion.v1",
            "source": {"path": str(source_path), "bytes": source_before.st_size,
                       "mtime_ns": source_before.st_mtime_ns,
                       "container_sha256": input_digest,
                       "consumed_decoded_bytes": consumed_bytes,
                       "consumed_decoded_sha256": consumed_digest.hexdigest(),
                       "decoded_eof_reached": eof_reached},
            "policy": {"input_line_limit": limit, "skip_invalid": args.skip_invalid,
                       "max_record_bytes": args.max_record_bytes,
                       "require_v25_markers": args.require_v25_markers},
            "counts": counts, "vision_status_counts": dict(vision_counts),
            "issue_examples": issues,
            "outputs": {key: {"filename": path.name, "bytes": output_bytes[key],
                              "sha256": output_hashes[key].hexdigest()}
                        for key, path in outputs.items()},
            "scope": "generic interchange; not model weights or a training recipe",
            "evaluation_outcomes_inferred": False,
            "actions_executed": False,
            "full_image_decode_completed": False,
            "gzip_full_stream_checked": source_path.suffix.lower() == ".gz" and eof_reached,
        }
        handle = tempfile.NamedTemporaryFile(mode="w", encoding="utf-8",
            prefix=".yoihen-report-", dir=output_dir, delete=False)
        report_stage = Path(handle.name)
        temporary.append(report_stage)
        with handle:
            json.dump(report, handle, ensure_ascii=False, indent=2, allow_nan=False)
            handle.write("\n")
        # Publish the report last: it is the completion marker for this output set.
        # Publication is not a transaction across files. Do not consume outputs early.
        for key, target in outputs.items():
            publish_new(staged[key], target)
            published.append(target)
        publish_new(report_stage, report_path)
        published.append(report_path)
        print(f"[OK] {counts['accepted']:,} accepted; {counts['rejected']:,} rejected")
        print(f"[OK] Sample records: {counts['sample_written']:,}; report: {report_path}")
        print("[INFO] Generic JSONL only. No actions executed; no weights trained/exported.")
        print("[WARNING] Alive DVD self-update content requires separately enforced governance.")
        return 0
    except (OSError, EOFError, ValueError, UnicodeError) as exc:
        for target in reversed(published):
            target.unlink(missing_ok=True)
        print(f"[FAIL] {exc}", file=sys.stderr)
        return 1
    finally:
        for path in temporary:
            path.unlink(missing_ok=True)


if __name__ == "__main__":
    sys.exit(main())
