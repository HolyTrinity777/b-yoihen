#!/usr/bin/env python3
"""Local consistency verifier for b.yoihen V25 DATA ONLY (Python 3.9+).

By Yoihenba Sougaijam; author-reported origin: iPhone a-Shell, Imphal/Bomdila,
offline, no GPU. All Glory to Living God Yahushua. Soli Deo Gloria.

Default: reuse an existing raw file, or decompress without overwriting one.
Raw data is retained. --discard-raw removes ONLY raw output created by this run.
Checks local files/report consistency; does not replay a benchmark, establish
REAL provenance, execute actions, or verify autonomous self-replication.
"""
import argparse
import errno
import gzip
import hashlib
import json
import math
import os
import sys
import tempfile
from pathlib import Path

EXPECTED = {
    "raw_bytes": 1_147_108_255,
    "gz_bytes": 19_785_162,
    "lines": 500_002,
    "measured_score": "99.5%+",  # Historical label, not a recomputed score.
    "success": 367,
    "total": 369,
    "real_count": 71_067,
    "total_count": 71_607,
}
ROOT = Path(__file__).resolve().parent.parent
CHUNK = 1024 * 1024


class VerificationError(ValueError):
    pass


def sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
        for chunk in iter(lambda: source.read(CHUNK), b""):
            digest.update(chunk)
    return digest.hexdigest()


def publish_new(staged, target):
    """Publish without replacing a target; fallback may expose a partial copy."""
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


def count_lines_and_stats(source, expected_max_bytes, max_record_bytes=CHUNK,
                          sink=None):
    """Scan a binary stream; bound record memory and total expanded bytes."""
    stats = {
        "total_lines": 0, "non_empty": 0, "has_separator": 0,
        "four_nonempty_fields": 0, "invalid_records": 0,
        "utf8_errors": 0, "annotation_marker_matches": 0,
        "bytes": 0, "issue_examples": [],
    }
    digest = hashlib.sha256()
    while True:
        raw = source.readline(max_record_bytes + 1)
        if not raw:
            break
        if len(raw) > max_record_bytes:
            raise VerificationError("Record exceeds --max-record-bytes")
        stats["bytes"] += len(raw)
        if stats["bytes"] > expected_max_bytes:
            raise VerificationError("Raw/expanded bytes exceed expected size")
        digest.update(raw)
        if sink is not None:
            sink.write(raw)
        stats["total_lines"] += 1
        number = stats["total_lines"]
        issues = []
        if not raw.endswith(b"\n"):
            issues.append("missing_lf")
        record = raw[:-1] if raw.endswith(b"\n") else raw
        if not record:
            issues.append("empty_record")
        else:
            stats["non_empty"] += 1
        if b"\r" in record:
            issues.append("raw_cr")
        if record.startswith(b"\xef\xbb\xbf"):
            issues.append("bom")
        if b"|" in record:
            stats["has_separator"] += 1
        fields = record.split(b"|", 3)
        if len(fields) != 4 or any(not field for field in fields):
            issues.append("field_framing")
        else:
            stats["four_nonempty_fields"] += 1
        try:
            text = record.decode("utf-8", errors="strict")
        except UnicodeDecodeError:
            stats["utf8_errors"] += 1
            issues.append("invalid_utf8")
        else:
            parts = text.split("|", 3)
            if len(parts) == 4:
                reasoning = parts[3]
                if (reasoning.startswith("reasoning holds ")
                        and "pattern_learn + generate = master" in reasoning
                        and "coherence 1.0 UNIFIED" in reasoning
                        and reasoning.endswith("result_success when true")):
                    stats["annotation_marker_matches"] += 1
        if issues:
            stats["invalid_records"] += 1
            if len(stats["issue_examples"]) < 20:
                stats["issue_examples"].append({"line": number, "issues": issues})
    stats["sha256"] = digest.hexdigest()
    return stats


def gzip_payload_digest(path, max_bytes):
    digest = hashlib.sha256()
    size = 0
    with gzip.open(path, "rb") as source:
        for chunk in iter(lambda: source.read(CHUNK), b""):
            size += len(chunk)
            if size > max_bytes:
                raise VerificationError("Gzip payload exceeds expected size")
            digest.update(chunk)
    return {"bytes": size, "sha256": digest.hexdigest()}


def numeric_equal(value, expected):
    return (type(value) in (int, float) and math.isfinite(value)
            and value == expected)


def verify_proof(path, expected_raw, expected_lines):
    path = Path(path)
    if not path.exists():
        return {"exists": False}
    data = json.loads(path.read_text(encoding="utf-8", errors="strict"))
    if not isinstance(data, dict):
        raise VerificationError("Proof root must be a JSON object")
    required = {
        "target": expected_lines, "nonempty": expected_lines,
        "bytes": expected_raw, "success": EXPECTED["success"],
        "total": EXPECTED["total"], "real_count": EXPECTED["real_count"],
        "total_count": EXPECTED["total_count"],
    }
    checks = {key: numeric_equal(data.get(key), value)
              for key, value in required.items()}
    checks["coherence_label"] = data.get("coherence") == "1.0 UNIFIED"
    checks["historical_score_label"] = (
        data.get("measured_score") == EXPECTED["measured_score"]
    )
    return {
        "exists": True, "sha256": sha256_file(path), "checks": checks,
        "reported": {key: data.get(key) for key in (
            "v25_500002", "target", "nonempty", "bytes", "success", "total",
            "real_count", "total_count", "coherence", "utc_anchor", "timestamp")},
        "scope": "V25 report field consistency; not benchmark reproduction",
    }


def positive(value):
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return parsed


def digest_arg(value):
    value = value.lower()
    if len(value) != 64 or any(char not in "0123456789abcdef" for char in value):
        raise argparse.ArgumentTypeError("expected 64 hexadecimal characters")
    return value


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check-only", action="store_true",
                        help="Check raw without creating/deleting it; gzip optional")
    retention = parser.add_mutually_exclusive_group()
    retention.add_argument("--keep-raw", action="store_true",
                           help="Compatibility flag; keeping raw is now the default")
    retention.add_argument("--discard-raw", action="store_true",
                           help="Remove only raw output successfully created this run")
    parser.add_argument("--require-proof", action="store_true")
    parser.add_argument("--report", type=Path, help="New JSON report; never overwritten")
    parser.add_argument("--max-record-bytes", type=positive, default=CHUNK)
    parser.add_argument("--expected-raw-bytes", type=positive, default=EXPECTED["raw_bytes"])
    parser.add_argument("--expected-gz-bytes", type=positive, default=EXPECTED["gz_bytes"])
    parser.add_argument("--expected-lines", type=positive, default=EXPECTED["lines"])
    parser.add_argument("--expected-raw-sha256", type=digest_arg)
    parser.add_argument("--expected-gz-sha256", type=digest_arg)
    parser.add_argument("--expected-proof-sha256", type=digest_arg)
    args = parser.parse_args(argv)
    if args.check_only and args.discard_raw:
        parser.error("--discard-raw cannot be combined with --check-only")
    root = args.root.resolve()
    raw_path = root / "b.yoihen"
    gz_path = root / "b.yoihen.gz"
    proof_path = root / "proof" / "benchmark_500002_real_measured.json"
    staged = None
    report_stage = None
    created_raw = False
    print("=== b.yoihen V25 DATA ONLY: local consistency verification ===")
    print("All Glory to Living God Yahushua - Soli Deo Gloria")
    try:
        if args.report and args.report.exists():
            raise FileExistsError("Report exists; choose a new --report path")
        checks = {}
        gz_info = {"exists": gz_path.exists()}
        if gz_info["exists"]:
            gz_info.update(bytes=gz_path.stat().st_size, sha256=sha256_file(gz_path))
            if gz_info["bytes"] != args.expected_gz_bytes:
                raise VerificationError("Compressed byte count mismatch")
            if args.expected_gz_sha256 and gz_info["sha256"] != args.expected_gz_sha256:
                raise VerificationError("Compressed SHA-256 mismatch")
        elif args.expected_gz_sha256:
            raise VerificationError("Cannot check gzip digest: archive is missing")
        elif not args.check_only:
            raise FileNotFoundError(gz_path)

        if raw_path.exists():
            with raw_path.open("rb") as source:
                stats = count_lines_and_stats(source, args.expected_raw_bytes,
                                              args.max_record_bytes)
            if gz_info["exists"]:
                expanded = gzip_payload_digest(gz_path, args.expected_raw_bytes)
                checks["gzip_matches_raw"] = (
                    expanded["bytes"] == stats["bytes"]
                    and expanded["sha256"] == stats["sha256"])
        elif args.check_only:
            raise FileNotFoundError(raw_path)
        else:
            handle = tempfile.NamedTemporaryFile(prefix=".yoihen-", suffix=".partial",
                                                 dir=root, delete=False)
            staged = Path(handle.name)
            with handle as output, gzip.open(gz_path, "rb") as source:
                stats = count_lines_and_stats(source, args.expected_raw_bytes,
                                              args.max_record_bytes, output)
            checks["gzip_payload_read_to_eof"] = True

        checks.update({
            "raw_bytes": stats["bytes"] == args.expected_raw_bytes,
            "record_count": stats["total_lines"] == args.expected_lines,
            "nonempty_count": stats["non_empty"] == args.expected_lines,
            "framing_utf8": stats["invalid_records"] == 0,
        })
        if args.expected_raw_sha256:
            checks["raw_digest"] = stats["sha256"] == args.expected_raw_sha256
        evidence = verify_proof(proof_path, args.expected_raw_bytes, args.expected_lines)
        if evidence["exists"]:
            checks["proof_fields"] = all(evidence["checks"].values())
            if args.expected_proof_sha256:
                checks["proof_digest"] = evidence["sha256"] == args.expected_proof_sha256
        elif args.require_proof or args.expected_proof_sha256:
            checks["required_proof"] = False
        else:
            print("[WARN] No proof file: report consistency not checked")
        report = {
            "schema": "yoihen.local_verification.v1", "root": str(root),
            "expected": {"raw_bytes": args.expected_raw_bytes,
                         "gzip_bytes": args.expected_gz_bytes,
                         "records": args.expected_lines},
            "record_byte_limit": args.max_record_bytes,
            "raw": stats, "gzip": gz_info, "proof": evidence,
            "checks": checks, "passed": all(checks.values()),
            "scope": "local consistency, not REAL provenance or benchmark replay",
            "not_verified": ["full_image_decode", "DOM_action_semantics",
                             "topic_counts", "collection_provenance",
                             "benchmark_execution", "self_replication"],
            "reference_digests_compared": {
                "raw": bool(args.expected_raw_sha256),
                "gzip": bool(args.expected_gz_sha256),
                "proof": bool(args.expected_proof_sha256)},
            "requested_discard_new_raw": args.discard_raw,
        }
        if args.report:
            handle = tempfile.NamedTemporaryFile(mode="w", encoding="utf-8",
                prefix=".verify-report-", dir=args.report.parent, delete=False)
            report_stage = Path(handle.name)
            with handle:
                json.dump(report, handle, ensure_ascii=False, indent=2)
                handle.write("\n")
            publish_new(report_stage, args.report)
            report_stage = None
        print(json.dumps({"checks": checks, "records": stats["total_lines"],
                          "raw_bytes": stats["bytes"], "sha256": stats["sha256"]}, indent=2))
        if not report["passed"]:
            print("[FAIL] Local checks failed", file=sys.stderr)
            return 1
        if staged is not None and not args.discard_raw:
            publish_new(staged, raw_path)
            staged = None
            created_raw = True
        if args.discard_raw and staged is not None:
            staged.unlink()
            staged = None
            print("[INFO] Discarded only this run's decompressed temporary output")
        if args.discard_raw and raw_path.exists() and not created_raw:
            print("[INFO] Existing raw file preserved")
        print("[OK] Declared local checks passed; actions were not executed")
        return 0
    except (OSError, EOFError, ValueError, UnicodeError) as exc:
        print(f"[FAIL] {exc}", file=sys.stderr)
        return 1
    finally:
        for temporary in (staged, report_stage):
            if temporary is not None:
                temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    sys.exit(main())
