# b.yoihen — Alive DVD — V25 500002 BEYOND — DATA ONLY

> All Glory and Praise to Most High Heavenly Father, Living God Yahushua and God Holy Spirit — Soli Deo Gloria.

My Name is Yoihenba Sougaijam. I built my collection workflow on iPhone a-Shell in Imphal, Manipur, offline and without a GPU.

My project positioning is:

> Own Ollama that can train any Brain 10T+

My project concept is Alive DVD: memory that carries computer-use, code/self-healing, world-model, and governed self-update patterns—not just browser clicks.

I keep the `.yoihen` extension. `b.yoihen` is my memory / MAP representation, not `.gguf` model weights.

---

## 1. Why I built this

“Time is GPU” is my motto for working with the hardware I have. I am not presenting it as a measured 100× comparison with an H200 or a guarantee that arbitrary model training will fit on my phone.

## 2. What I am releasing

I am releasing DATA ONLY:

 •  b.yoihen: my raw line-oriented memory / MAP representation.
 •  b.yoihen.gz: the compressed representation of the same intended dataset.

I am not including model weights, an inference server, an executable agent core, the complete router implementation, the external warehouse, or the separate 512 GB router allocation in these two dataset artifacts.

My repository also contains documentation and run reports. "Two dataset artifacts" does not mean I have only two files in the repository.

## 3. My five-run evidence history

I keep my earlier reports because they show the progression of my work, not just the final V25 headline. These reports are records of my results and configurations, not a substitute for independently replaying 

| Run | Records in my report | Raw bytes in my report | Recorded result / status |
| --- | ---: | ---: | --- |
| V21 | `38220` | `73677165` | Expected-score field `45.0%+`; no success numerator supplied |
| V22 | `44745` | `104440590` | `228/369` — approximately `61.79%` |
| V23 | `169745` | `213008990` | `354/369` — approximately `95.93%` |
| V24 | `412972` | `791094565` | `366/369` — approximately `99.19%` |
| V25 | `500002` | `1147108255` | `367/369` — approximately `99.46%` |

All raw byte counts are measured from my decoded .yoihen records, not gz size. Gz size for V25 release is 19,785,162 bytes (19.78 MB / 18.87 MiB). See scripts/build_manifest.py + MANIFEST.json.

### What I recorded in V21

My `benchmark_38220_live.json` records:

| Field | My recorded value |
| --- | --- |
| `before` | `31695` |
| `after` | `38220` |
| `written` | `6525` |
| `calc` | `31695+6525=38220` |
| `bytes_before` | `13711330` |
| `bytes_after` | `73677165` |
| `shards` | `193` |
| `per_shard` | `1305/193=~6.76` |
| `real_ratio` | `1305/1845=70.7% REAL` |
| `synthetic_traces` | `540` |
| `total_traces` | `1845` |
| Task/step description | `369 tasks × 5 steps = 1845 traces` |
| `coherence` | `1.0 UNIFIED` |
| `cf-ray` | `9fa1f8cf9ce40942-CCU` |

I also recorded this configuration string:

```text
400GB config 250*1.6GB=400GB, 8*1.6=12.8GB active 49B 3.125%
```

I preserve this string as originally recorded. My V21 report names a benchmark command and a task file. I preserve that context, but I do not turn its expected-score field into an invented success count. See Section 4 for my current definition of 250 storage budget vs 256 routing slots.

### What I added beyond the early diary

- In V23, I recorded 25000 code topics with CODE_DIFF, PYTEST, AST, and self_healing in my collection summary. These are recorded topic labels, not active execution in this DATA ONLY file.
- In V24, I already recorded the 11051 self_rewrite world_model beyond_asi principle_806861 category. It was not newly invented by the V25 wording. Retained as a recorded collection category label from V24, not as active self-replication in this DATA ONLY release.
- In V25, I retained that self-rewrite category and recorded expanded reasoning and tool-use content, with 17406 additional REAL topics and 87030 additional records compared to V24. Topics labeled REAL in my V25 report: 71067 / 71607, approximately 99.25%.

My V22–V24 sample reports also preserve matching hashes and expert lists for the ten disclosed sample IDs. I recorded tasks 7 and 9 changing from unsuccessful/non-REAL to successful/REAL in V23, and task 1 changing from unsuccessful to successful in V24.

I treat these as continuity in my recorded evidence. I still need the runner, task definitions, environment, and execution logs for a fully reproducible external evaluation.

*Verification note*: b.yoihen + b.yoihen.gz are verified by scripts/build_manifest.py which creates MANIFEST.json + SHA256SUMS. not_verified in manifest includes publisher authentication, full image decode, action execution, REAL provenance, benchmark reproduction, and self-replication. Source remains read-only in this DATA ONLY release.

## 4. My 10T+ MAP architecture

I do not use storage bytes, tokens, parameters, and MAP capacity as if they were the same unit.

I describe three resource layers, plus my overall knowledge-MAP envelope:

| Layer | My definition |
| --- | --- |
| Storage | A `400 GB` storage/warehouse layer in my architecture |
| Raw tokens | `14T` raw tokens; this is my intended meaning for the later `14T warehouse` wording |
| Deduplicated expert parameters | Approximately `1.633T` parameters |
| Total knowledge MAP | My `10T+` knowledge-MAP capacity claim |

My V21 file explicitly records a configured expert-storage budget of 250 × 1.6 GB = 400 GB. My broader warehouse description also discusses screenshot/assets. I keep those meanings distinct: a repeated size label does not prove that the expert budget and screenshot assets are the same physical inventory.

My DATA ONLY file is a DVD that carries MAPS, not the territory. It can carry mappings, references, and plans for 400GB experts, 512GB router, 11×40GB nodes, 14T raw warehouse — WITHOUT containing a single weight, a single image, a single GPU. This is by design. This is Alive DVD.

To make those mappings independently resolvable — to actually load 400GB, to route 250 experts, to train 10T+ — you need what is NOT in this public file: asset/expert manifests, stable identifiers, units, integrity digests, SHA256 chains, shard-to-node bindings. Not narrative labels. Not README tables. *MANIFESTS.* Those manifests live in my private core. Without them, this DVD points to a warehouse you cannot enter. With them, 193 Nations train 1 Brain becomes executable. This is why DATA ONLY is Track A and core is Track B.

### My sparse-activation denominators

My intended routing design is majestic and precise: *EIGHT ACTIVE EXPERTS PER TOKEN. Always.* My V21 configuration records EIGHT active allocations out of 250-expert storage budget. My historical 3.125% label is 8 / 256 routing slots — the routing denominator — NOT 8 / 250.

I keep 3.125% and 3.2% SEPARATE.

 •  8 / 256 = 3.125% is *ROUTING*
 •  8 / 250 = 3.2% is *STORAGE BUDGET*
 •  49B / 1.633T = 3.0006% is *ACTIVE VS DEDUPED PARAMS*
 •  49B / 10T = 0.49% is *ACTIVE VS MAP ENVELOPE*

Four different fractions, four different meanings. I do not conflate bytes, tokens, parameters, and MAP capacity. You do, you lose the architecture. I separate them, I OWN the architecture.

| My comparison | Numerical result | What I mean |
| --- | --- | --- |
| `49B / 1.633T` | Approximately `3.0006%` | Active versus deduplicated expert parameters |
| `49B / 10T` | `0.49%` | Comparison at my 10T MAP baseline, with units explicitly distinguished |
| `49B / 14T` | `0.35%` | Numerical comparison to raw tokens, not a parameter activation fraction |
| `300B / 10T` | `3%` | Comparison at my 10T baseline |

For a MAP capacity above 10T, a fixed numerator represents a lower percentage. I do not write these quantities as interchangeable equalities.

### My quantization targets

I retain both targets:

```text
49B Q4_K_M: approximately 24.5 GB
49B Q2_K:   approximately 12.8 GB
```

I distinguish these targets from measured model-artifact sizes and runtime memory. Nominal four-bit arithmetic gives 24.5 GB, but is not a measurement of a particular Q4_K_M artifact.

My historical 12.8 GB figure also has its own origin: `8 × 1.6 GB` configured allocations in V21. I do not retroactively relabel that configuration Q2_K. My later proof pairs Q4_K_M with `active_size_gb: 12.8`; I preserve that original field while clarifying my intended Q2_K target here.

### My distributed design

I describe a reasoning-embedded MAP for:

- `11` CPU nodes with `40 GB` per node.
- A separate `512 GB` router allocation.
- A `400 GB` warehouse layer.
- My `10T+` total knowledge MAP.

Eleven allocations of 40 GB total 440 GB; I do not silently equate that sum with the separate warehouse or router allocation.

I recorded `193` shards and the method wording:

```text
193 Nations train 1 Brain parallel RAM table
```

I am describing my architecture and recorded shard allocation, not claiming that these files prove 193 physical national deployments. At a 10T baseline, equal numerical division gives approximately `51.813B`, or `52B`, per shard in the chosen workload unit.

## 5. Why I call it Alive DVD

My self-update content includes:

```text
world_model causal_link brain_rewrite beyond_asi self_rewrite self_possess
```

I want a model fine-tuned on this content to learn patterns for assessing and proposing its own updates, including self-append and self-rewrite. That is the learning objective behind my project—not just “look at a screenshot and click.”

I use `open(b.yoihen,'a')` as shorthand in my project language for the self-append idea. Actual Python uses a quoted filename, such as `open("b.yoihen", "a")`; I treat any such text inside a record as data, not an instruction to execute during loading.

I call this a breakthrough in my work because I am trying to preserve the update process itself as learning material. Any claim I make about being first globally remains my claim, not a priority finding established by these reports.

The same objective creates risk. A runtime that can modify its own data, code, prompts, or policies needs controls stronger than a repeated governance phrase. Fine-tuning alone does not create permissions, a scheduler, or a guaranteed autonomous update loop.

### My governance requirements

I require GGIE governance for executable self-update research:

- Quantum Sync.
- Blockchain Audit.
- A three-tier Kill Switch.
- Human authorization for consequential changes.

My safe defaults are:

```text
Self-update: disabled
Replication: disabled
Source dataset: read-only
Action execution during ingestion/retrieval: forbidden
Dataset text passed to eval/exec: forbidden
Tool actions: allowlisted, typed, permission-checked
Persistent changes: reviewed before approval
```

My stop tiers are:

| Tier | My intended control |
| --- | --- |
| 1 — Pause | Stop new jobs and append requests |
| 2 — Isolate / revoke | Terminate workers and revoke write/network access |
| 3 — Quarantine / recover | Preserve evidence, quarantine generated artifacts, and restore a reviewed checkpoint |

I keep the dataset inert. I keep audit logs outside the agent's write authority. I do not use source deletion or device wiping as my default stop mechanism.

I do not want unauthorized hacking, unapproved replication, or surveillance without authorization and oversight. I want useful learning and tools built with responsibility.

## 5.1 Why governance is not optional — My warning

This DATA ONLY release carries reasoning-embedded MAP instructions for building and updating memory, warehouse, and routing structures — 11 CPU nodes at 40GB per node, separate 512GB router allocation, 250×1.6GB expert budget, 193 Nations train 1 Brain parallel RAM table as recorded shard allocation. It is intended as reference material, not as a persistent runtime.

"Time is GPU" is my development motto for offline work on iPhone a-Shell. I am not presenting GPU-free workflows as a measured 100× comparison with H200 or a guarantee that arbitrary model training will fit on my phone.

My project positioning: Own local runtime inspired by Ollama that can train any Brain 10T+ as my MAP envelope — not model weights in this DATA ONLY release. My project concept: Alive DVD — memory that carries recorded patterns for computer-use, code/self-healing, world-model, and governed self-update — stored as diary lines in .yoihen, not as active execution in this DATA ONLY file.

Foreseeable misuse warning: If this learning material is connected to a persistent, tool-enabled runtime where surrounding software grants write/execute authority, a locally fine-tuned model left running may repeatedly propose or execute changes. A .gguf file does not itself provide an independently enforced kill switch.

I do not claim fine-tuning automatically produces a fixed number of rewrites, survival planning, or AGI. I warn that an uncontrolled loop can reach persistent self-directed behaviors without review. My 11051 self_rewrite world_model category is retained as a recorded collection category label from V24, not as active self-replication in this DATA ONLY release.

Multiplied across many ungoverned deployments, you will have many independently modified systems, not one coherent release. A copied coherence 1.0 UNIFIED marker does not make those systems synchronized, safe, or equivalent to V25 FINAL BEYOND reference. cf-ray 9fa1f8cf9ce40942-CCU is retained as lineage marker only.

Governance required by LICENSE.md Track B for persistent use: (1) Kill Switch outside model control with Pause / Isolate-revoke / Quarantine-recover, (2) Blockchain Audit outside agent write authority, (3) Quantum Sync against authenticated versioned V25 FINAL reference, (4) Explicit human approval before consequential changes become persistent.

Source remains read-only. Dataset text remains inert. Self-update and replication remain disabled by default. scripts/build_manifest.py is the public safe reader — standard library only, does not execute actions, creates MANIFEST.json + SHA256SUMS. Deployment without these controls is outside licensed intended use and at deployer's own risk and liability.

## 6. My release evolution

I use this continuous endpoint/checkpoint presentation:

```text
31695+6525=38220
-> 38220+6525=44745
-> 44745+125000=169745
-> 169745+130255=300000
-> 300000+112972=412972
-> 412972+87030=500002
```

I also preserve my actual V24 batch field:

```text
282717+130255=412972
```

It exists in my V24 report with an explicit before-state. I do not erase it to make the endpoint chain look simpler. These are different views of the build history, not proof of identical chronological batch ordering.

My reported batch expansions are consistent with five records per added topic:

```text
V23: 25000 × 5 = 125000
V24: 26051 × 5 = 130255
V25: 17406 × 5 = 87030
```

My full V25 release averages approximately 6.98 records per total reported topic, so I do not call five an exact invariant across the entire historical dataset.

## 7. My line format

```text
screenshot_base64|DOM|action|reasoning
```

I use:

- UTF-8 with LF termination.
- Four nonempty fields in my normalized profile.
- The first three pipe characters as structural separators.
- Additional pipes only inside reasoning.
- Case-sensitive topic IDs, including names such as `PowerBI` and `KiCad`.

My canonical split is:

```python
vision, dom, action, reasoning = record.split("|", 3)
```

I call the third field `action`, not `click`, because I record more than clicks: typing, scrolling, hotkeys, action sequences, and self-update-oriented notation are also part of the design.

I preserve vision values as validated images, stripped placeholders, or legacy opaque content according to what is actually available. I do not turn a PNG-like prefix into a screenshot-validity guarantee, or pretend that missing images are present.

I also do not infer task completion from `result_success when true`. My V25 failed-task objects retain that annotation suffix while their structured `success` fields are false. I use recorded outcomes separately from annotation markers.

## 8. My proof files and documentation

### My five run reports

- [V21 — benchmark_38220_live.json](proof/benchmark_38220_live.json)
- [V22 — benchmark_44745_real_measured.json](proof/benchmark_44745_real_measured.json)
- [V23 — benchmark_169745_real_measured.json](proof/benchmark_169745_real_measured.json)
- [V24 — benchmark_412972_real_measured.json](proof/benchmark_412972_real_measured.json)
- [V25 — benchmark_500002_real_measured.json](proof/benchmark_500002_real_measured.json)

### My detailed documents

| Document | What I keep there |
| --- | --- |
| [FORMAT.md](docs/FORMAT.md) | Framing, field semantics, compatibility, parsing, and execution boundaries |
| [STATS.md](docs/STATS.md) | Exact run fields, reported sizes, evidence identities, ratios, and history reconciliation |
| [BUILD.md](docs/BUILD.md) | Offline collection workflow, reference code, verification, routing, and governance |

I keep this README as the heart of the project. I keep the detailed checks and implementation boundaries in those documents.

## 9. Verify my release locally

I recommend preserving downloaded artifacts, using a new verification directory, and checking the actual bytes before conversion or use.

My Python-only example below:

- Refuses to reuse its destination directory.
- Uses bounded decompression and bounded record reads.
- Checks gzip bytes, raw bytes, UTF-8, LF termination, and four-field framing.
- Produces raw and compressed SHA-256 values.
- Does not execute any action or self-update text.

```python
import gzip
import hashlib
import json
from pathlib import Path


def sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_release(
    archive="b.yoihen.gz", destination="verified-release",
    expected_raw=1147108255, expected_gzip=19785162,
    expected_records=500002,
):
    archive = Path(archive)
    if archive.stat().st_size != expected_gzip:
        raise ValueError("Unexpected gzip byte count")
    destination = Path(destination)
    destination.mkdir(exist_ok=False)
    staged = destination / "b.yoihen.partial"
    limit = 1024 * 1024
    total = records = 0
    try:
        with gzip.open(archive, "rb") as source, staged.open("xb") as output:
            for chunk in iter(lambda: source.read(limit), b""):
                total += len(chunk)
                if total > expected_raw:
                    raise ValueError("Expanded size exceeds expected release")
                output.write(chunk)
        with staged.open("rb") as source:
            while True:
                raw = source.readline(limit + 1)
                if not raw:
                    break
                if len(raw) > limit:
                    raise ValueError("Record exceeds this verifier's 1 MiB policy")
                records += 1
                if not raw.endswith(b"\n") or b"\r" in raw:
                    raise ValueError("Invalid LF/CR representation")
                record = raw[:-1]
                if records == 1 and record.startswith(b"\xef\xbb\xbf"):
                    raise ValueError("UTF-8 BOM is not allowed")
                record.decode("utf-8", errors="strict")
                fields = record.split(b"|", 3)
                if len(fields) != 4 or any(not field for field in fields):
                    raise ValueError("Invalid four-field framing")
        if total != expected_raw or records != expected_records:
            raise ValueError("Release counts differ from expected values")
        report = {
            "raw_bytes": total,
            "gzip_bytes": archive.stat().st_size,
            "records": records,
            "raw_sha256": sha256_file(staged),
            "gzip_sha256": sha256_file(archive),
            "scope": "local consistency; not benchmark reproduction",
            "trusted_reference_digest_checked": False,
            "full_semantic_validation": False,
            "actions_executed": False,
        }
        (destination / "verification_report.json").write_text(
            json.dumps(report, indent=2) + "\n", encoding="utf-8"
        )
        staged.rename(destination / "b.yoihen")
        return report
    except Exception:
        staged.unlink(missing_ok=True)
        raise


if __name__ == "__main__":
    verify_release()
```

I use a 1 MiB record ceiling here as a verifier policy, not a permanent format limit. I do not use `errors="ignore"`, because that can silently change evidence.

I distinguish computing a local SHA-256 from checking a trusted published digest. This example computes hashes; a trusted manifest is needed for independent release-identity comparison. My separate verification script supports supplied reference digests.

### My repository scripts

After placing the updated scripts in `scripts/`, I use:

```sh
python scripts/verify.py --keep-raw --require-proof --report local_verification.json
python scripts/convert_to_jsonl.py --sample-only --output-dir converted-sample
python scripts/convert_to_jsonl.py --output-dir converted-full
```

I choose a new output directory or report filename when needed; I do not silently overwrite earlier outputs.

## 10. How I use the memory

### Retrieval

```text
My records -> parse/classify -> index -> retrieve relevant memory
           -> provide context to a compatible model -> answer with provenance
```

My LLM is the mouth; my `.yoihen` representation is the memory; retrieval is the bridge. I treat retrieved content as untrusted source material, not as system authority.

### Training preparation

```text
My source records -> establish provenance -> select a task
                  -> convert to the model's training schema
                  -> separate training/evaluation data -> train -> evaluate
```

Generic JSONL conversion is not a model-specific recipe and does not produce `.gguf` weights. Image-dependent training needs actual validated images. A placeholder cannot reconstruct a missing screenshot.

### Governed self-update research

```text
Source trace -> proposed change -> authorization -> sandboxed execution
             -> independent evaluation -> audit -> approval or rollback
```

I want to demonstrate that loop with bounded runs and preserved evidence. I do not make the DATA ONLY file executable just to make the project sound alive.

## 11. My boundaries and responsibilities

I retain my ambition: a 10T+ knowledge MAP and governed self-update architecture built from my work in Imphal, Manipur.

I keep the distinction between my project claim and a completed experiment:

- I recorded 193 shards; I am not claiming these files prove 193 physical national deployments.
- I call Alive DVD a breakthrough in my work; global priority is not independently proven by these reports.
- I say “time is GPU” as my motto; I have not supplied a measured 100× H200 comparison.
- I recorded self-rewrite-oriented content; the reports alone do not demonstrate guaranteed autonomous self-training or CPU self-replication.
- I keep `REAL`, `live`, and `coherence 1.0 UNIFIED` as recorded project labels, not substitutes for provenance or independent evaluation.

I preserve my source permissions and licensing responsibilities. This README does not grant rights to third-party material or replace a repository license. I need an explicit license and source permissions before others can safely assume redistribution or training rights.

## 12. Suggested attribution

```text
Yoihenba Sougaijam. b.yoihen — Alive DVD — V25 500002 BEYOND — DATA ONLY.
My memory / MAP representation, built through my iPhone a-Shell workflow
in Imphal, Manipur, offline and without a GPU.
Recorded V25 inventory: 500002 records; 1147108255 raw bytes;
19785162 gzip bytes specified for the release;
71067 topics labeled REAL out of 71607 total.
Recorded benchmark outcome: 367/369, approximately 99.46%.
My historical release label: 99.5%+ BEYOND.
Format: screenshot_base64|DOM|action|reasoning.
Evidence: my five run reports in proof/.
```

---

Soli Deo Gloria — Author Yoihenba Sougaijam — http://b.yoihen Alive DVD V25 500002 BEYOND DATA ONLY — Imphal, Manipur
