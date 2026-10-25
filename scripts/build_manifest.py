#!/usr/bin/env python3
"""Measure local .yoihen bytes and create MANIFEST.json plus SHA256SUMS.

Standard library only. Does not execute actions or infer REAL provenance.
No archive is downloaded. Existing output files are never overwritten.
Defaults select b.yoihen.gz if present, otherwise b.yoihen, at repo root.
"""
import argparse
import base64
import binascii
import gzip
import hashlib
import json
import re
import sys
import zlib
from collections import Counter
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROOFS = ["benchmark_38220_live.json", "benchmark_44745_real_measured.json",
          "benchmark_169745_real_measured.json", "benchmark_412972_real_measured.json",
          "benchmark_500002_real_measured.json"]


class Topics(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id") is not None and "real" in (attrs.get("class") or "").split():
            self.ids.append(attrs["id"])


def hash_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def classify(value):
    if value.startswith("[STRIPPED"):
        return "stripped"
    try:
        image = base64.b64decode(value, validate=True)
    except (binascii.Error, ValueError):
        return "legacy_opaque"
    return ("base64_png_candidate" if image.startswith(b"\x89PNG\r\n\x1a\n")
            else "legacy_opaque")


def positive(value):
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return number


def scan(path, max_record, max_expanded, count_topics, topic_cap):
    opener = gzip.open if path.suffix.lower() == ".gz" else open
    counts = Counter()
    visions = Counter()
    examples = []
    topics = set()
    topic_cap_exceeded = False
    digest = hashlib.sha256()
    with opener(path, "rb") as source:
        while True:
            raw = source.readline(max_record + 1)
            if not raw:
                break
            if len(raw) > max_record:
                raise ValueError("Record exceeds configured byte ceiling")
            counts["decoded_bytes"] += len(raw)
            if counts["decoded_bytes"] > max_expanded:
                raise ValueError("Decoded data exceeds configured byte ceiling")
            digest.update(raw)
            counts["physical_records"] += 1
            number = counts["physical_records"]
            issues = []
            if not raw.endswith(b"\n"):
                issues.append("missing_lf")
            record = raw[:-1] if raw.endswith(b"\n") else raw
            counts["nonempty_records"] += bool(record)
            if b"\r" in record:
                issues.append("raw_cr")
            if record.startswith(b"\xef\xbb\xbf"):
                issues.append("bom")
            if not record:
                issues.append("empty_record")
            try:
                text = record.decode("utf-8", errors="strict")
            except UnicodeDecodeError:
                counts["invalid_utf8_records"] += 1
                issues.append("invalid_utf8")
                text = None
            if text is not None:
                fields = text.split("|", 3)
                if len(fields) != 4 or any(not field for field in fields):
                    issues.append("field_framing")
                elif not issues:
                    counts["framing_valid_records"] += 1
                    vision, dom, action, reasoning = fields
                    visions[classify(vision)] += 1
                    counts["annotation_marker_matches"] += (
                        reasoning.startswith("reasoning holds ")
                        and "pattern_learn + generate = master" in reasoning
                        and "coherence 1.0 UNIFIED" in reasoning
                        and reasoning.endswith("result_success when true")
                    )
                    if count_topics:
                        parser = Topics()
                        parser.feed(dom)
                        parser.close()
                        if len(parser.ids) != 1:
                            counts["topic_extraction_invalid_records"] += 1
                        elif re.fullmatch(r"[A-Za-z0-9_]+", parser.ids[0]) is None:
                            counts["topic_extraction_invalid_records"] += 1
                        else:
                            counts["topic_extraction_valid_records"] += 1
                            topic = parser.ids[0]
                            if topic not in topics:
                                if len(topics) < topic_cap:
                                    topics.add(topic)
                                else:
                                    topic_cap_exceeded = True
            if issues:
                counts["invalid_records"] += 1
                if len(examples) < 20:
                    examples.append({"source_line": number, "issues": issues})
    required = ["decoded_bytes", "physical_records", "nonempty_records",
                "invalid_utf8_records", "framing_valid_records", "invalid_records",
                "annotation_marker_matches"]
    return {
        "counts": {key: counts[key] for key in required},
        "decoded_sha256": digest.hexdigest(),
        "vision_classification_counts": dict(visions),
        "full_image_decode_completed": False,
        "topic_inventory": {
            "enabled": count_topics,
            "rule": "one id on an element carrying class token real; case preserved",
            "valid_records": counts["topic_extraction_valid_records"] if count_topics else None,
            "invalid_records": counts["topic_extraction_invalid_records"] if count_topics else None,
            "unique_ids_retained": len(topics) if count_topics else None,
            "unique_count_exact": len(topics) if count_topics and not topic_cap_exceeded else None,
            "memory_cap_ids": topic_cap if count_topics else None,
            "cap_exceeded": topic_cap_exceeded,
            "REAL_provenance_verified": False,
        },
        "issue_examples": examples,
        "source_read_to_decoded_eof": True,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--release-id", default="V25 500002 BEYOND â DATA ONLY")
    parser.add_argument("--expected-records", type=positive, default=500002)
    parser.add_argument("--expected-raw-bytes", type=positive, default=1147108255)
    parser.add_argument("--expected-gz-bytes", type=positive, default=19785162)
    parser.add_argument("--max-record-bytes", type=positive, default=1024 * 1024)
    parser.add_argument("--max-expanded-bytes", type=positive, default=2 * 1024**3)
    parser.add_argument("--count-topics", action="store_true")
    parser.add_argument("--max-topics", type=positive, default=100000)
    args = parser.parse_args(argv)
    repo = args.root.resolve()
    source = args.input or (repo / "b.yoihen.gz" if (repo / "b.yoihen.gz").is_file()
                            else repo / "b.yoihen")
    source = source.resolve()
    output_dir = (args.output_dir or repo).resolve()
    created = []
    try:
        if not source.is_file():
            raise FileNotFoundError(source)
        output_dir.mkdir(parents=True, exist_ok=True)
        targets = [output_dir / "MANIFEST.json", output_dir / "SHA256SUMS"]
        if any(target.exists() or target.is_symlink() for target in targets):
            raise FileExistsError("Manifest output already exists; use a new --output-dir")
        if source in [target.resolve() for target in targets]:
            raise ValueError("Output cannot replace input")
        before = source.stat()
        measured = scan(source, args.max_record_bytes, args.max_expanded_bytes,
                        args.count_topics, args.max_topics)
        source_hash = hash_file(source)
        after = source.stat()
        if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
            raise ValueError("Source changed during measurement")
        compressed = source.suffix.lower() == ".gz"
        counts = measured["counts"]
        checks = {
            "record_count": counts["physical_records"] == args.expected_records,
            "nonempty_count": counts["nonempty_records"] == args.expected_records,
            "raw_bytes": counts["decoded_bytes"] == args.expected_raw_bytes,
            "framing_utf8": counts["invalid_records"] == 0,
        }
        if compressed:
            checks["gzip_bytes"] = before.st_size == args.expected_gz_bytes
        if args.count_topics:
            checks["topic_extraction"] = measured["topic_inventory"]["invalid_records"] == 0
            checks["topic_count_not_truncated"] = not measured["topic_inventory"]["cap_exceeded"]
        identities = []
        for name in PROOFS:
            path = repo / "proof" / name
            if path.is_file():
                identities.append({"path": "proof/" + name,
                                   "bytes": path.stat().st_size,
                                   "sha256": hash_file(path)})
        reduction = (100 * (1 - before.st_size / counts["decoded_bytes"])
                     if compressed and counts["decoded_bytes"] else None)
        report = {
            "schema": "yoihen.release_manifest.v1",
            "release_id": args.release_id,
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "generator": {"path": "scripts/build_manifest.py",
                          "sha256": hash_file(Path(__file__)),
                          "declared_checks_only": True},
            "input": {"path": str(source), "filename": source.name,
                      "bytes": before.st_size, "sha256": source_hash,
                      "compressed": compressed},
            "expected": {"records": args.expected_records,
                         "raw_bytes": args.expected_raw_bytes,
                         "gzip_bytes": args.expected_gz_bytes},
            "observed": measured, "checks": checks,
            "passed_declared_checks": all(checks.values()),
            "compression_reduction_percent": reduction,
            "proof_file_identities": identities,
            "licence_reference": "LICENSE.md",
            "not_verified": ["publisher_authentication", "full_image_decode",
                "strict_HTML_conformance", "action_execution", "REAL_provenance",
                "exact_or_semantic_duplicates", "benchmark_reproduction",
                "third_party_rights", "model_training", "self_replication"],
            "checksum_file_scope": "selected existing input only, relative to its original directory",
        }
        manifest_bytes = (json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        # GNU checksum notation escapes newlines/backslashes in unusual filenames.
        filename = source.name
        if "\n" in filename or "\\" in filename:
            escaped = filename.replace("\\", "\\\\").replace("\n", "\\n")
            checksum_text = "\\" + source_hash + "  " + escaped + "\n"
        else:
            checksum_text = source_hash + "  " + filename + "\n"
        for target, content in [(targets[0], manifest_bytes),
                                (targets[1], checksum_text.encode("utf-8"))]:
            handle = target.open("xb")
            created.append(target)
            with handle:
                handle.write(content)
        print(json.dumps({"checks": checks, "observed": counts,
                          "source_sha256": source_hash}, indent=2))
        print("[INFO] Local measurements only. No actions or benchmark executed.")
        print("[INFO] SHA256SUMS refers to the selected input filename, not every release asset.")
        return 0 if all(checks.values()) else 1
    except (OSError, EOFError, ValueError, zlib.error) as exc:
        for path in reversed(created):
            path.unlink(missing_ok=True)
        print(f"[FAIL] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
