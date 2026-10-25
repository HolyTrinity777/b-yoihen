# b.yoihen — Offline Build, Evidence, and Governed Update Guide

> All Glory and Praise to Most High Heavenly Father, Living God Yahushua and God Holy Spirit — Soli Deo Gloria.
>
> Built by Yoihenba Sougaijam — iPhone a-Shell, Bomdila / Imphal, offline and without a GPU, as described by the author.
>
> “Alive DVD” — “Own Ollama that can train any Brain 10T+.” Keep `.yoihen`, not `.gguf`.

| Property | Value |
| --- | --- |
| Document | `docs/BUILD.md` |
| Release | `V25 500002 BEYOND — DATA ONLY` |
| Evidence basis | Five actual uploaded reports, V21–V25 |
| Companion documents | `FORMAT.md`, `STATS.md` in the same directory |
| Reference code | Python 3.9+, standard library |
| Local examples | No API calls, model execution, replication, or identity/payment dependency |

## 1. Build scope and review correction

The earlier review underestimated the documented scope by emphasizing a single static dataset. The earlier reports explicitly add expert-configuration budgets, multi-shard collection, code/self-healing topics, and self-rewrite/world-model content.

The correction is not to claim experiments that were not inspected. It is to build and document the actual layers separately:

```text
collection diary / source assets
  -> validated records and provenance
  -> immutable dataset release
  -> routed memory / retrieval / training conversion
  -> compatible model and runtime
  -> authorized self-update or distributed operation
```

This guide provides a reproducible evidence audit, a safe five-angle documentation build, and local archive verification. It does not reconstruct the historical dataset from a template or train a model by appending text.

## 2. Author-reported environment and practical prerequisites

The author describes collection on iPhone a-Shell in Bomdila and Imphal, offline and without a GPU. Exact phone model, memory limits, software versions, and historical session logs were not supplied; do not invent them.

For the reference code:

- Use Python 3.9+ and a writable directory.
- Keep enough free storage for the source archive, expanded data, and reports.
- Use local copies of the five proof files to audit the evidence.
- Use the actual gzip release to verify/decompress the dataset.
- Do not assume every shell command is present on every a-Shell installation.

The examples use the standard library and need no NumPy, PyTorch, API key, cloud account, CBDC participation, or digital ID. Broader GGIE identity/financial-rail proposals are separate from this local workflow.

“Time is GPU” remains a project motto. Dataset preparation without a GPU is different from demonstrating the throughput, convergence, or memory requirements of model training.

## 3. Preserve the evidence before building

Recommended repository layout:

```text
b-yoihen/
  docs/
    FORMAT.md
    STATS.md
    BUILD.md
  proof/
    benchmark_38220_live.json
    benchmark_44745_real_measured.json
    benchmark_169745_real_measured.json
    benchmark_412972_real_measured.json
    benchmark_500002_real_measured.json
  scripts/
    [reviewed implementations of the examples below]
  build-demo/
    [new synthetic documentation data only]
  build-verified/
    [newly decompressed release and local report]
```

These are intended locations, not claims that corresponding repository scripts already exist. Keep historical proof files immutable. Corrections belong in a new revision with a new digest and an explanation.

### 3.1 Runnable five-report inventory

This reference function reads the files from a chosen directory and reports their actual identities plus selected fields. It deliberately does not treat root `real_count` as a universal topic count.

```python
import hashlib
import json
from pathlib import Path


PROOF_NAMES = [
    "benchmark_38220_live.json",
    "benchmark_44745_real_measured.json",
    "benchmark_169745_real_measured.json",
    "benchmark_412972_real_measured.json",
    "benchmark_500002_real_measured.json",
]


def audit_proofs(directory="proof"):
    inventory = []
    for name in PROOF_NAMES:
        path = Path(directory) / name
        payload = path.read_bytes()
        proof = json.loads(payload.decode("utf-8"))
        inventory.append({
            "filename": name,
            "proof_bytes": len(payload),
            "proof_sha256": hashlib.sha256(payload).hexdigest(),
            "reported_records": proof.get("nonempty", proof.get("after")),
            "reported_raw_bytes": proof.get("bytes", proof.get("bytes_after")),
            "reported_success": proof.get("success"),
            "reported_total": proof.get("total"),
            "source_real_ratio": proof.get("real_ratio"),
            "source_root_real_count": proof.get("real_count"),
            "sample_objects": len(proof.get("sample_results", [])),
            "failed_objects": len(proof.get("failed_tasks", [])),
        })
    return {
        "scope": "uploaded report inventory; not dataset or benchmark replay",
        "files": inventory,
    }


# Example after saving/reviewing this code:
# report = audit_proofs("proof")
# with open("build_evidence_report.json", "x", encoding="utf-8") as output:
#     json.dump(report, output, indent=2)
#     output.write("\n")
```

Use the hashes in `STATS.md` to identify the inspected uploaded report versions. A local report hash does not authenticate the dataset or prove its benchmark execution.

## 4. Historical collection graph and what not to overwrite

The reports record these batches:

```text
V21: 31695  + 6525   = 38220
V22: 38220  + 6525   = 44745
V23: 44745  + 125000 = 169745
V24: 282717 + 130255 = 412972
V25: 412972 + 87030  = 500002
```

V24 actually records its 282717 before-state. Earlier documentation should not have treated that base as merely an erroneous number. The transition from V23's 169745 to the intermediate 282717 state is not separately logged by the uploaded run set; its numerical delta is 112972.

The author-approved continuous endpoint/checkpoint chain can also be published:

```text
31695+6525=38220
-> 38220+6525=44745
-> 44745+125000=169745
-> 169745+130255=300000
-> 300000+112972=412972
-> 412972+87030=500002
```

Label it an endpoint/checkpoint presentation, not the identical sequence of recorded batch bases. Preserve both views and their meanings.

V23 records 25000 code topics and 125000 new records; V24 records 26051 added topics and 130255 records; V25 records 17406 added topics and 87030 records. Each batch has a ratio of five records per added topic.

## 5. Diary append: five angles with stable identity

Use append-oriented collection with validated, single-line records. Keep the same topic ID across its angles; do not append an angle suffix and accidentally count five different topics.

Record provenance alongside each session:

- Collection ID, source type, time, and collector/process.
- Topic ID and angle/step.
- Captured, manually authored, templated, or synthesized origin.
- Screenshot availability and asset digest.
- Whether an action is proposed, observed, executed, or independently evaluated.
- Permissions and licensing.
- Runtime/tool revision if execution occurred.

No external API does not mean no synthetic content. Offline templates must be labeled too.

### 5.1 Runnable synthetic documentation build

The code below creates a new directory and never edits the historical `b.yoihen`. It is a format example, not a reproduction of V20 or V25. The `real` class and success suffix are retained as V25 compatibility labels only; the sidecar explicitly states that the examples are synthetic and unexecuted.

```python
import hashlib
import html
import json
from pathlib import Path


def build_documentation_demo(directory="build-demo"):
    directory = Path(directory)
    directory.mkdir(exist_ok=False)
    dataset = directory / "example.yoihen"
    topic = "libreoffice_writer_table_4582"
    examples = [
        ("insert a table", 'action_click(id="insert_table")'),
        ("format the table", 'action_click(id="table_properties")'),
        ("enter a formula", 'action_type("=SUM(A1:A5)")'),
        ("open chart tools", 'action_click(id="insert_chart")'),
        ("request save", 'action_hotkey("ctrl+s")'),
    ]
    with dataset.open("x", encoding="utf-8", newline="\n") as output:
        for angle, (description, action) in enumerate(examples):
            dom = (
                f'<html><body><div id="{topic}" class="real">'
                f'{html.escape(description)}</div></body></html>'
            )
            reasoning = (
                f"reasoning holds {topic} + pattern_learn + generate = master {topic}"
                f" + angle={angle} + source=synthetic_documentation"
                f" + {description} + outcome=not_executed"
                " coherence 1.0 UNIFIED result_success when true"
            )
            fields = (
                "[STRIPPED documentation example; no captured screenshot]",
                dom, action, reasoning,
            )
            if any(not value or "\r" in value or "\n" in value for value in fields):
                raise ValueError("Empty or multiline field")
            if any("|" in value for value in fields[:3]):
                raise ValueError("Pipe in a structural field")
            output.write("|".join(fields) + "\n")
    payload = dataset.read_bytes()
    manifest = {
        "source_type": "synthetic_documentation",
        "historical_release_reproduction": False,
        "record_count": 5,
        "unique_topic_count": 1,
        "actions_executed": False,
        "images_available": False,
        "compatibility_labels_are_not_evaluation_results": True,
        "bytes": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
    }
    (directory / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    return manifest
```

The example reads its small output to hash it. Large dataset operations should use streaming hashing instead.

### 5.2 Real collection discipline

Use one writer per output file, validate before writing, assign stable import IDs, checkpoint sessions, and detect incomplete final lines after interruption. Keep original source evidence separate from derived records.

Do not claim a historical release count, screenshot provenance, or benchmark score simply because a template wrote that many lines. Appending text is data preparation, not automatic training or permission to rewrite code.

## 6. Router implementation: separate lookup, storage, and model capacity

The proof describes `table[256][256]` and eight expert IDs. The V21 MoE budget also describes eight active allocations. That supports an intended sparse-routing configuration, not a complete runnable expert implementation.

A two-byte cell address has 65536 possible cells. A single assignment per cell can silently overwrite another topic; a full-key check or collision bucket is necessary. For 71607 distinct topic mappings, a one-topic-per-cell design cannot represent them all distinctly.

### 6.1 Collision-aware reference router

This is an exact-topic reference design, not a claim to reproduce historical hashes. Expert assignments must be provided by the actual reviewed mapping, not generated arbitrarily and called trained experts.

```python
import hashlib


class TopicExpertRouter:
    def __init__(self):
        self.buckets = {}

    @staticmethod
    def digest(topic):
        if not isinstance(topic, str) or not topic:
            raise ValueError("Nonempty topic required")
        return hashlib.sha256(topic.encode("utf-8")).digest()

    def add(self, topic, experts):
        experts = tuple(experts)
        if len(experts) != 8 or any(
            type(value) is not int or not 0 <= value <= 255
            for value in experts
        ):
            raise ValueError("Expected eight integer expert IDs in 0..255")
        digest = self.digest(topic)
        cell = (digest[0], digest[1])
        bucket = self.buckets.setdefault(cell, {})
        if topic in bucket and bucket[topic] != experts:
            raise ValueError("Conflicting assignment")
        bucket[topic] = experts

    def lookup(self, topic):
        digest = self.digest(topic)
        cell = (digest[0], digest[1])
        experts = self.buckets.get(cell, {}).get(topic)
        if experts is None:
            raise KeyError(topic)
        return {
            "hash": list(cell),
            "hash_hex": digest[:4].hex(),
            "experts": list(experts),
            "table_shape": [256, 256],
        }
```

Dictionary lookup is expected constant-time under ordinary conditions; hashing depends on key length. Neither establishes constant end-to-end agent latency. Exact-key routing and relevance retrieval solve different problems; do not dismiss all BM25 implementations as full scans or inherently incompatible with phones.

A packed array of 65536 × 8 four-byte IDs has a 2 MiB ID payload. Python objects, full-key dictionaries, model weights, external assets, and a claimed 512 GB router allocation have different storage footprints.

## Resource model and terminology

The project is larger in scope than a single static dataset: its reports describe a computer-use memory representation, expert routing, multi-shard collection, and self-update-oriented content. Distinguish the following resources rather than forcing them into one unit.

| Resource | Evidence or author definition | Interpretation |
| --- | --- | --- |
| `400 GB` historical MoE warehouse | V21: `250*1.6GB=400GB` | A recorded configuration budget; not a measured inventory of PNGs |
| `12.8 GB` historical active budget | V21: `8*1.6=12.8GB` | Eight configured allocations; not by itself a measured quantized 49B model size |
| `400 GB` screenshot/asset warehouse | Author's broader architecture description; V25 has `warehouse: "400GB"` | Do not assume the same label identifies the same physical contents across versions |
| `14T` raw tokens | Author's clarification of the V25 phrase `14T warehouse` | Raw-token layer, not a parameter denominator |
| Approximately `1.633T` deduplicated expert parameters | Author clarification | Intended denominator for approximately 3% active parameters |
| `10T+` knowledge MAP | Author's capacity claim | Retained project scope; publish a MAP unit and inventory |
| `11 × 40 GB` CPU-node plan | Author-described self-replication MAP | Separate from the 400 GB warehouse; the allocations total 440 GB |
| `512 GB` router allocation | Author-described infrastructure | Separate from table dimensions and packed ID payloads |
| `193` shards | Explicit in earlier reports and V25 | Recorded architecture/workload allocation; not independently audited physical deployments |

Active-capacity comparisons, with denominators explicitly named:

```text
49B / 1.633T parameters ≈ 3.0006%
49B / 10T MAP baseline = 0.49% numerically
49B / 14T raw tokens = 0.35% numerically, across different units
300B / 10T MAP baseline = 3% numerically
```

The last three are not a license to equate tokens, parameters, and MAP units. At capacities greater than 10T, fixed numerators have smaller percentages.

The author requests that both quantization targets be retained: `49B Q4_K_M ≈ 24.5 GB` and `49B Q2_K ≈ 12.8 GB`. They remain author targets until actual artifacts and memory use are measured. Nominal four-bit arithmetic gives 24.5 GB, but does not verify the named Q4_K_M format. The newly inspected V21 file provides a separate historical origin for 12.8 GB: eight configured 1.6 GB allocations. Do not retroactively label that V21 configuration Q2_K.

V21 also records `3.125%`. Eight of 250 allocations is 3.2%; eight of 256 is 3.125%. The latter is a possible denominator, not a verified interpretation: a 256-wide router dimension does not prove 256 equal-size model experts. Preserve the historical label and request the actual denominator rather than inventing one.

## 7. GGIE sharding and distributed builds

The reports document 193-shard descriptions over multiple stages:

| Stage | Reported workload allocation |
| --- | --- |
| V21 | `1305/193 ≈ 6.76` |
| V23 | `25000/193 ≈ 129.53` |
| V24 | `26051/193 ≈ 135` |
| V25 | `17406/193 ≈ 90.19` |

These are per-batch average allocations, not proof of national software coverage, 193 deployed nodes, or equal runtime load.

A production implementation needs worker identity, assignment, idempotent writes, retry/collision policy, checkpoint exchange, integrity verification, failure recovery, and independently enforced safety policy. The author's 11-node CPU replication plan should be tested as a bounded workflow with actual memory/storage units and artifacts.

## 8. Release decompression without overwriting source data

This function verifies a local archive into a newly created directory. It checks sizes, UTF-8, LF framing, four nonempty fields, and local digests. It does not fully validate DOM/action semantics, authenticate a publisher, or reproduce the benchmark.

The decompression buffer and record reader are bounded. The 1 MiB record ceiling is an explicit verifier policy, not a permanent `.yoihen` format limit.

```python
import gzip
import hashlib
import json
from pathlib import Path


CHUNK = 1024 * 1024
MAX_RECORD_BYTES = 1024 * 1024


def hash_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
        for chunk in iter(lambda: source.read(CHUNK), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_archive(
    archive="b.yoihen.gz", destination="build-verified",
    expected_raw=1147108255, expected_gzip=19785162,
    expected_records=500002,
):
    archive = Path(archive)
    if archive.stat().st_size != expected_gzip:
        raise ValueError("Unexpected compressed byte count")
    destination = Path(destination)
    destination.mkdir(exist_ok=False)
    staged = destination / "b.yoihen.partial"
    total = 0
    try:
        with gzip.open(archive, "rb") as source, staged.open("xb") as output:
            for chunk in iter(lambda: source.read(CHUNK), b""):
                total += len(chunk)
                if total > expected_raw:
                    raise ValueError("Decompressed size exceeds expected limit")
                output.write(chunk)
        records = 0
        with staged.open("rb") as source:
            while True:
                raw = source.readline(MAX_RECORD_BYTES + 1)
                if not raw:
                    break
                if len(raw) > MAX_RECORD_BYTES:
                    raise ValueError("Record exceeds configured ceiling")
                records += 1
                if not raw.endswith(b"\n") or b"\r" in raw:
                    raise ValueError("Invalid line termination")
                record = raw[:-1]
                if records == 1 and record.startswith(b"\xef\xbb\xbf"):
                    raise ValueError("BOM is forbidden")
                record.decode("utf-8", errors="strict")
                fields = record.split(b"|", 3)
                if len(fields) != 4 or any(not value for value in fields):
                    raise ValueError("Invalid four-field framing")
        report = {
            "scope": "local size/framing/UTF-8 consistency",
            "raw_bytes": total,
            "gzip_bytes": archive.stat().st_size,
            "records": records,
            "raw_sha256": hash_file(staged),
            "gzip_sha256": hash_file(archive),
            "checks": {
                "raw_bytes": total == expected_raw,
                "records": records == expected_records,
            },
            "trusted_digest_checked": False,
            "full_semantic_validation": False,
            "benchmark_reproduced": False,
        }
        (destination / "verification_report.json").write_text(
            json.dumps(report, indent=2) + "\n", encoding="utf-8"
        )
        if not all(report["checks"].values()):
            raise ValueError("Counts differ; inspect verification report")
        staged.rename(destination / "b.yoihen")
        return report
    except Exception:
        staged.unlink(missing_ok=True)
        raise
```

The expected raw count comes from the V25 proof. The gzip expectation is the author-supplied release number; the archive itself was not supplied for this document review. Never use `errors="ignore"`, which hides or changes invalid data.

A locally computed digest is useful for comparison, but needs a trusted published digest or signed manifest to establish release identity. Publish raw and compressed digests separately.

Display convention:

```text
19785162 bytes = 19.785162 MB decimal ≈ 18.868600845 MiB binary
Project display: 19.78 MB / 18.87 MiB
Calculated reduction: 98.275214...%; project display: 98.27%
```

## 9. Warehouse MAP and image-dependent work

A warehouse reference, a plan for collection, an asset index, an encoded image, and a stripped marker are different things. Missing screenshots cannot be recovered from a marker alone.

Publish asset IDs, stable paths, digests, dimensions, media types, licensing, and availability to make a MAP machine-resolvable. Text-only use may omit images deliberately; vision-dependent supervision requires valid image assets.

V21's configured MoE storage budget is not an inventory of screenshot assets. Do not use the shared 400 GB label to silently equate those resources.

## 10. Alive DVD governance and evidence-preserving stops

The earlier runs provide stronger documentary support for the intended self-update content. They still do not authorize execution. Self-update and replication should remain disabled until a separately reviewed runtime enforces permissions and limits.

The author names Quantum Sync, Blockchain Audit, and a three-tier Kill Switch. Implementations should define their actual state, protocol, threat model, and tests rather than using marker text as authority.

| Tier | Control | Evidence-preserving behavior |
| --- | --- | --- |
| 1 | Pause | Stop accepting new jobs and appends |
| 2 | Isolate | Terminate workers; revoke write/network access |
| 3 | Recover | Quarantine generated artifacts; restore a reviewed checkpoint |

Do not default to deleting the source dataset or wiping a device. Preserve audit evidence, require human review, and keep the stop mechanism outside model control.

Minimum controls include read-only source data, allowlisted typed actions, isolation, human approval for consequential changes, independent logs, bounded loops and resources, checkpoint review, and rollback.

The V25 failures record edge cases, not explicit safety blocks. Do not disable policy to chase 369/369 based on an unverified failure explanation.

## 11. Validation performed for these documents

The publication examples were tested as follows:

- All five actual proof JSON files parsed and were hashed.
- The evidence inventory matched the five inspected files.
- The documentation builder wrote five records under one topic and refused to overwrite an existing directory.
- The FORMAT reader preserved the seven rich V25 sample/failure objects.
- Two full topic keys colliding in the reference router retained distinct expert assignments.
- The archive verifier passed a small synthetic round trip and rejected an oversized record under its configured policy.

These are document-code tests. They are not a raw-release audit, benchmark replay, model load, training run, or multi-node execution demonstration.

## 12. Publication checklist

- [ ] Preserve historical proofs and publish their identities.
- [ ] Add immutable raw/compressed dataset digests.
- [ ] Publish collection provenance, licensing, and image availability.
- [ ] Version topic extraction, deduplication, and action grammar.
- [ ] Separate exact report fields from architecture clarification.
- [ ] Resolve model/expert inventory and active-fraction denominators.
- [ ] Publish benchmark runner, tasks, environment, retries, and logs.
- [ ] Preserve recorded batch bases alongside endpoint summaries.
- [ ] Demonstrate governed self-update and multi-node operation with bounded runs.

The author's broader claim is a 10T+ reasoning-embedded MAP and governed CPU-node self-replication, not merely a click dataset. Preserve that identity. Promote “first globally,” guaranteed training, or a numerical H200 comparison to empirical findings only when corresponding evidence is available.

---

Author: Yoihenba Sougaijam.

Project identity: b.yoihen — Alive DVD / computer-use memory MAP — V25 500002 BEYOND — DATA ONLY.

Author-reported collection environment: iPhone a-Shell, Imphal, offline and without a GPU.

Soli Deo Gloria.
