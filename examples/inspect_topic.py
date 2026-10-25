#!/usr/bin/env python3
"""Read-only b.yoihen inspection. No model calls, action execution, or writes."""
import argparse
import base64
import binascii
import gzip
import hashlib
import json
import sys
import zlib
from html.parser import HTMLParser
from pathlib import Path


class Topics(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id") is not None and "real" in (attrs.get("class") or "").split():
            self.ids.append(attrs["id"])


def digest_file(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def vision_status(value):
    if value.startswith("[STRIPPED"):
        return "stripped"
    try:
        decoded = base64.b64decode(value, validate=True)
    except (binascii.Error, ValueError):
        return "legacy_opaque"
    return ("base64_png_candidate" if decoded.startswith(b"\x89PNG\r\n\x1a\n")
            else "legacy_opaque")


def positive(value):
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return parsed


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("examples/proof_sample.yoihen"))
    parser.add_argument("--topic", help="Exact case-sensitive topic ID")
    parser.add_argument("--limit", type=positive, default=3, help="Maximum matching records")
    parser.add_argument("--max-record-bytes", type=positive, default=1024 * 1024)
    args = parser.parse_args(argv)
    try:
        sidecar_path = args.input.with_suffix(".manifest.json")
        sidecar = None
        entries = {}
        if sidecar_path.is_file():
            sidecar = json.loads(sidecar_path.read_text(encoding="utf-8"))
            if sidecar.get("schema") != "yoihen.proof_sample.v1":
                raise ValueError("Unsupported sample sidecar schema")
            if digest_file(args.input) != sidecar["sample"]["sha256"]:
                raise ValueError("Sample SHA-256 differs from sidecar")
            entries = {item["sample_line"]: item for item in sidecar["records"]}
            source_proof = args.input.parent.parent / sidecar["source"]["repository_path"]
            if source_proof.is_file() and digest_file(source_proof) != sidecar["source"]["sha256"]:
                raise ValueError("Local source proof differs from sample provenance")
        opener = gzip.open if args.input.suffix.lower() == ".gz" else open
        matched = 0
        scanned = 0
        with opener(args.input, "rb") as source:
            while matched < args.limit:
                raw = source.readline(args.max_record_bytes + 1)
                if not raw:
                    break
                scanned += 1
                if len(raw) > args.max_record_bytes:
                    raise ValueError("Record exceeds configured limit")
                if not raw.endswith(b"\n") or b"\r" in raw:
                    raise ValueError(f"Invalid line ending at line {scanned}")
                text = raw[:-1].decode("utf-8", errors="strict")
                if text.startswith("\ufeff"):
                    raise ValueError(f"BOM at line {scanned}")
                fields = text.split("|", 3)
                if len(fields) != 4 or any(not field for field in fields):
                    raise ValueError(f"Invalid framing at line {scanned}")
                screenshot, dom, action, reasoning = fields
                topic_parser = Topics()
                topic_parser.feed(dom)
                topic_parser.close()
                topic = topic_parser.ids[0] if len(topic_parser.ids) == 1 else None
                entry = entries.get(scanned)
                if sidecar is not None:
                    if entry is None or hashlib.sha256(raw).hexdigest() != entry["record_sha256_including_lf"]:
                        raise ValueError(f"Sample record digest mismatch at line {scanned}")
                if args.topic is not None and topic != args.topic:
                    continue
                record = {
                    "input_line": scanned, "topic": topic,
                    "vision_status": vision_status(screenshot),
                    "screenshot_base64": screenshot, "dom": dom,
                    "action": action, "reasoning": reasoning,
                    "actions_executed": False,
                }
                if entry:
                    record["reported_evaluation"] = {
                        "source_object": entry["source_object"],
                        "success": entry["reported_success"],
                        "result": entry["reported_result"],
                        "independently_executed_here": False,
                    }
                # JSON escaping prevents raw control characters from reaching the terminal.
                print(json.dumps(record, ensure_ascii=True))
                matched += 1
        print(f"[INFO] {matched} matching record(s); {scanned} scanned. "
              "Inspection only; full-release integrity and benchmark not verified.", file=sys.stderr)
        return 0 if matched else 1
    except (OSError, EOFError, ValueError, KeyError, TypeError, zlib.error) as exc:
        print(f"[FAIL] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
