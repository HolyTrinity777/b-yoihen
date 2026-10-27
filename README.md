# b.yoihen — Alive DVD — V25 500002 BEYOND — DATA ONLY

> All Glory and Praise to Most High Heavenly Father, Living God Yahushua and God Holy Spirit — Soli Deo Gloria.

My Name is Yoihenba Sougaijam. I built my collection workflow on iPhone a-Shell in Imphal, Manipur, offline and without a GPU.

My project positioning is:
> ‪I built a living 500k-line memory system b.yoihen‬.
‪Ollama = frozen weights‬,
‪b.yoihen Day 1 = Day 100‬,
‪b.yoihen + llama.cpp = living setup‬,
‪Load any .gguf‬
‪Growing offline memory that never forgets n evolves‬
‪Becomes more personal every day
‪And secure your privacy‬

My project concept is Alive DVD: a replaceable model brain, persistent local memory, and a governed path from experience to the next useful decision.

Not just browser clicks. Not just a fixed checkpoint. Not a claim that a compressed file executes itself.

I keep the `.yoihen` extension. `b.yoihen` is my memory / MAP representation. A compatible `.gguf` can supply the model brain. My private core is the separate player, resolver, orchestrator, and control layer in my architecture. My public release contains DATA ONLY—not that complete runtime.

---

## Start here

| What I want you to inspect | Where to go |
| --- | --- |
| The actual archive and its verified counts | [Section 9](#9-verify-my-actual-release) |
| Why I call the design Alive DVD | [Section 5](#5-why-i-call-it-alive-dvd) |
| The resource layers behind my 10T+ MAP claim | [Section 4](#4-my-10t-map-architecture) |
| A small read-only inspection example | [Section 10](#10-how-i-use-the-memory) |
| Collection, provenance, and limitations | [DATASET_CARD.md](DATASET_CARD.md) |
| Claim-to-evidence mapping | [docs/CLAIMS.md](docs/CLAIMS.md) |
| Public licence scope | [NOTICE.md](NOTICE.md) |

### My V25 archive at a glance

| Measurement | My verified archive result |
| --- | ---: |
| Total physical lines | `500,002` |
| Four-nonempty-field records | `348,722` |
| No-pipe hit lines | `151,280` |
| Invalid records under my verifier's checks | `0` |
| UTF-8 errors | `0` |
| Compressed bytes | `19,785,162` |
| Uncompressed bytes | `1,147,108,255` |

```text
Compressed:   19.785162 MB decimal — my display: 19.78 MB
Uncompressed: 1.147108255 GB decimal — approximately 1.15 GB
Gzip SHA-256: aeaf109f5706849b6ec01b975f15ec9bdbb90fa046205ade2afe6898fb35b0c1
```

My passing actual-dataset GitHub Actions job checks the committed archive's bytes, mixed-line counts, framing, and UTF-8. It does not establish capture attestation, payload removal, model quality, or autonomous evolution. Those are different claims with different evidence requirements.

## 1. Why I built this

I want an assistant that does not have to start from zero every time I return to my own work.

My machine has a history. My projects have dependencies, conventions, working fixes, failed attempts, and decisions that matter. I want that experience to remain available locally instead of being scattered across forgotten sessions, terminal output, and disconnected files.

That is the point of my Alive DVD concept: continuity around a replaceable brain.

I want to preserve what actually worked, what failed, why I approved a change, and when an old answer stopped being correct. I want a future decision to benefit from an earlier verified experience—not merely repeat a confident answer.

“Time is GPU” is my development motto for working with the hardware I have. I am not presenting it as a measured 100× H200 comparison, a claim that memory removes compute requirements, or a guarantee that arbitrary model training fits on my phone.

I build ambitious. I disclose precisely.

## 2. What I am releasing

I am releasing DATA ONLY.

My tracked dataset artifact is:

```text
b.yoihen.gz
```

Decoding it produces the local raw representation:

```text
b.yoihen
```

I do not require the approximately 1.15 GB raw file to be committed. My repository also contains documentation, reports, examples, and tooling; “one tracked dataset archive” does not mean “one repository file.”

### What is public, and what is separate

| Component | Role in my architecture | Included in this DATA ONLY release? |
| --- | --- | --- |
| `.yoihen` representation | Stored records, hit lines, context, and MAP descriptions | Yes, through the compressed archive |
| Compatible GGUF model | The model brain used by an execution environment | No model weights are bundled here |
| My private core | Resolver, orchestration, tool/runtime integration, and governance implementation | Not included |
| External asset/expert inventory | Actual resources referenced by the architecture | Not included merely by reference |
| Separate router/cluster resources | Runtime allocations and infrastructure | Not included merely by description |

My DVD carries a MAP—not the territory.

A line mentioning a warehouse does not contain that warehouse. A configuration string does not load an expert. A recorded action does not authorize its execution. A governance label does not implement a stop mechanism.

I do not claim that the archive is image-free, capture-free, or sanitized simply because I call its first field `vision_ref`. Payload absence needs its own release-specific measurement.

## 3. My five-run evidence history

I keep my earlier reports because they show the progression of my work—not just the final V25 headline.

| Run | Lines recorded in my report | Raw bytes recorded in my report | Recorded result / status |
| --- | ---: | ---: | --- |
| V21 | `38,220` | `73,677,165` | Expected-score field `45.0%+`; no success numerator supplied |
| V22 | `44,745` | `104,440,590` | `228/369` — approximately `61.79%` |
| V23 | `169,745` | `213,008,990` | `354/369` — approximately `95.93%` |
| V24 | `412,972` | `791,094,565` | `366/369` — approximately `99.19%` |
| V25 | `500,002` | `1,147,108,255` | `367/369` — approximately `99.46%` |

These reports record my results and configurations. They are not a substitute for publishing or independently replaying the benchmark runner, task definitions, model/runtime configuration, and evaluator.

I distinguish uncompressed byte counts from gzip size. For V25, my archive is `19,785,162` compressed bytes, while its decoded representation is `1,147,108,255` bytes.

### What I recorded in V21

| Field | Recorded value |
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

I preserve this configuration string exactly as recorded:

```text
400GB config 250*1.6GB=400GB, 8*1.6=12.8GB active 49B 3.125%
```

The V21 report names a benchmark command and task file. I retain that context without turning an expected-score field into an invented success count.

### What I added beyond the early diary

- V23: `25000` code topics with `CODE_DIFF`, `PYTEST`, `AST`, and `self_healing` in my collection summary.
- V24: the `11051 self_rewrite world_model beyond_asi principle_806861` category was already recorded here.
- V25: I retained that category and recorded expanded reasoning/tool-use content, `17406` additional REAL topics, and `87030` additional lines relative to the reported V24 endpoint.

These are collection descriptions, not a claim that the DATA ONLY archive is executing those operations. Categories can recur or overlap across versions; I do not treat every V25 summary entry as a newly collected, unique item.

My V25 report labels `71067 / 71607` items REAL: approximately `99.245884%`, or `99.25%` rounded. I assign REAL during scoring, not as an independently attested capture-time fact.

### Continuity in the disclosed samples

My V22–V24 reports retain matching hashes and expert lists for the ten disclosed sample IDs. Tasks 7 and 9 change from unsuccessful/non-REAL in V22 to successful/REAL in V23. Task 1 changes from unsuccessful in V23 to successful in V24.

I treat that as continuity in my recorded evidence—not proof of the cause of improvement, independent execution, or a leak-free evaluation split.

Historical `real_count` fields also have different meanings or populations across versions. I do not mistake V23's `361` or V24's `366` root values for their topic numerators.

## 4. My 10T+ MAP architecture

I do not conflate bytes, tokens, parameters, and MAP capacity. I separate the ledgers.

| Layer | My definition and boundary |
| --- | --- |
| Configured storage | V21 records `250 × 1.6 GB = 400 GB` |
| Configured active allocations | V21 records `8 × 1.6 GB = 12.8 GB` |
| Raw token layer | My intended interpretation of the later `14T warehouse` wording is `14T` raw tokens |
| Deduplicated expert-parameter layer | My architectural definition is approximately `1.633T` parameters; this requires an actual expert inventory |
| Total knowledge MAP | My `10T+` capacity claim; its unit and inventory must be explicitly defined |

My broader warehouse description also discusses screenshot/assets. I do not use a repeated 400 GB label as proof that the expert-storage budget and the asset warehouse are the same inventory.

My public representation can carry references and plans for larger resources without bundling those resources. To resolve my private inventory, I need the actual asset/expert manifests, stable identifiers, digests, bindings, and resolver logic—not just narrative labels.

Those private implementation details are separate from the public data format. I do not claim that keeping them private makes independent compatible engineering impossible or restricts the public CC BY/MIT rights.

### My sparse-routing denominators

Eight active experts per routed token is my intended routing design. My V21 text records eight active allocations and a 250-allocation storage budget. I distinguish that budget from a 256-position routing denominator.

| Fraction | Result | Meaning |
| --- | ---: | --- |
| `8 / 256` | `3.125%` | Routing-position fraction in my intended design |
| `8 / 250` | `3.2%` | Fraction of the configured 250 expert allocations |
| `49B / 1.633T` | Approximately `3.0006%` | Parameter-to-parameter comparison |
| `49B / 10T` | `0.49%` numerically | Comparison at my 10T MAP baseline; units remain distinct |
| `49B / 14T` | `0.35%` numerically | Comparison with raw tokens, not a parameter activation fraction |
| `300B / 10T` | `3%` numerically | Comparison at the 10T baseline |

Different denominators. Different meanings.

At a MAP capacity above 10T, a fixed numerator represents a smaller percentage. Deduplicating a token corpus does not itself turn those tokens into learned model parameters. The configuration and routing design need runtime evidence before I call them measured per-token behavior.

### My quantization targets

```text
49B Q4_K_M: approximately 24.5 GB — target, not a measured artifact here
49B Q2_K:   approximately 12.8 GB — target, not a measured artifact here
```

Nominal four-bit arithmetic gives 24.5 GB for 49 billion values. That does not measure the overhead, mixed tensor formats, or runtime allocation of a particular Q4_K_M model.

My historical 12.8 GB also has a separate origin: eight configured 1.6 GB allocations in V21. I do not retroactively rename that budget Q2_K. My later proof pairs Q4_K_M with `active_size_gb: 12.8`; I preserve the historical field while keeping my intended target clarification separate.

### My node and router budgets

My described layout budgets ten 40 GB allocations for a 400 GB expert inventory and an eleventh 40 GB allocation for a control/router node: 440 GB total.

The separate 512 GB router figure is not additional memory that fits inside that eleventh 40 GB allocation. If it means a resident 512 GB table, I need additional memory or a separately specified sharding/offload design. If it means an address space or stored resource, I must say that explicitly.

I do not present an unresolved allocation label as a measured bill of materials. My implementation manifest must identify storage versus RAM, residency versus backing storage, and physical versus logical resources.

### My 193-shard design

I recorded:

```text
193 Nations train 1 Brain parallel RAM table
```

That is my recorded method and shard-allocation architecture—not proof of 193 physical national deployments or 193 complete model shards inside this archive.

At the 10T baseline:

```text
10T / 193 ≈ 51.813B per shard in the chosen workload unit
```

An allocation calculation does not establish training throughput or memory fit. My binder concept includes version consistency, manifest resolution, and coordination. Its name does not substitute for a tested distributed implementation.

## 5. Why I call it Alive DVD

The point is continuity.

A fixed model checkpoint can stay the same while the system around it learns which dependency worked, which repair failed, what changed in my project, and which approved decision should inform the next one.

My intended system pairs a compatible GGUF brain with persistent local memory and a controlled experience loop:

```text
Compatible model brain
        +
My memory / MAP representation
        +
My private execution and governance layer
        ↓
Observe → record evidence → retrieve relevant experience
        ↓
Propose → authorize → act → evaluate
        ↓
Retain a verified result, correct it, or roll back
```

Ollama is a model-running tool, not a weight file. A GGUF is a model representation, not an autonomous learning loop. My intended distinction is not “Ollama is dead.” It is that I am building persistent experience around a replaceable model brain.

### The same brain, a more useful assistant

| Stage | What I want the system to retain |
| --- | --- |
| Initial use | My baseline corpus and explicitly supplied project context |
| After verified work | Fixes that passed tests, attempts that failed, approvals, and source evidence |
| Over repeated sessions | Relevant machine/project history, with corrections, versioning, and user control |

I do not promise a fixed number of new memories after 30 days or an automatic improvement after every append. More lines are not automatically better memory. A stored guess is not a verified outcome.

I distinguish three update paths:

- Memory update: records and retrievable context change.
- System update: tools, routing, prompts, configuration, or code change.
- Model update: learned parameters or adapters change through an actual supported training process.

Appending a diary changes stored data. It does not, by itself, change a GGUF's weights. I evaluate each path according to what actually changed.

### My fixed release and my working diary are not the same artifact

I keep the published V25 archive immutable so its hashes and measurements remain reproducible.

A personalized runtime should write to a separate working-memory store, with provenance and revision history. If I publish an expanded corpus later, it receives its own version and manifest. I do not silently grow the original V25 file and continue claiming its old digest.

“Never forgetting” is an ambition for durable continuity—not permission to retain errors or private information forever. I need correction, deletion, retention controls, backups, and recovery as well as append operations.

My strong local-first claim is control over my data and operation without dependence on a cloud provider. I do not claim that cloud services are inherently unable to retain memory.

### My self-update learning material

My recorded content includes:

```text
world_model causal_link brain_rewrite beyond_asi self_rewrite self_possess
```

I use `open(b.yoihen,'a')` as project shorthand for the self-append idea. Actual Python uses a quoted filename. In a governed runtime, the writable target should be an authorized working store, not my immutable published release.

The text remains data during loading. My recorded 11051-entry self-rewrite category is not an execution log demonstrating 11051 successful autonomous rewrites.

I call Alive DVD a breakthrough in my work because I want the update process itself to become inspectable learning material. Global priority remains a claim to investigate, not a finding established by a README.

### 5.1 Why governance is not optional — My warning

I built Alive DVD to support self-update—not merely to preserve browser clicks. My recorded self-rewrite and world-model patterns are learning material for a system that can assess its state, propose a change, and, through a separately authorized runtime, apply that change to working memory, code, or configuration.

That is the **capability** I am warning about. The public DATA ONLY archive remains inert. Connecting it to a compatible model and an execution layer with write authority creates a different security boundary: proposed updates can become persistent changes.

I do not confuse the ability to make a change with proof that the change is correct, beneficial, or authorized. Memory updates, runtime/code updates, and model-weight updates are different operations. Each needs its own permissions, evaluation, and recovery path.

A persistent assistant with tools, credentials, write access, and a feedback loop can cause damage even when its model weights remain unchanged. Wrong memories can accumulate. Bad changes can persist. A retrieved instruction can be mistaken for authority. An uncontrolled loop can repeat an error across files, sessions, or workers.

My warning is not that every download automatically evolves. My warning is that enabling a persistent update loop without independent controls can turn one mistake into repeated, lasting system changes.

#### My markers are not my enforcement mechanisms

A `.gguf` file does not enforce an independent kill switch. A copied `coherence 1.0 UNIFIED` marker does not synchronize systems or make them safe. I retain `cf-ray 9fa1f8cf9ce40942-CCU` as a lineage marker—not as an authentication credential or synchronization protocol.

My governance vocabulary includes Quantum Sync, Blockchain Audit, and a three-tier Kill Switch. Those names must correspond to mechanisms that do real work:

- A stop path outside the model’s control.
- Tool and filesystem permissions enforced outside model-generated text.
- Audit records outside the agent’s write authority.
- Authenticated, versioned references rather than trust in repeated labels.
- Approval bound to the actual tool, target, arguments, and permitted operation.
- Fresh approval when the proposed operation changes.
- Resource, worker, time, and iteration limits.
- Independent evaluation before persistent changes are accepted.
- Reviewed checkpoints and a tested recovery path.

A model-generated `approved=true` is not my authorization. A successful write is not my evaluation. An appended record is not automatically a verified memory.

#### My safe defaults

```text
Self-update: disabled
Replication: disabled
Published source artifacts: read-only
Personal working memory: separate, access-controlled, and versioned
Action execution during ingestion/retrieval: forbidden
Dataset text passed to eval/exec: forbidden
Tools: allowlisted, typed, permission-checked
Consequential operations: explicitly authorized
Persistent changes: evaluated and reviewed before acceptance
Audit records: outside agent write authority
Stop mechanism: outside model control
```

I keep my published V25 release immutable. A personalized runtime writes to a separate authorized working store; it does not silently alter the published artifact while retaining its old identity or checksum.

#### My three stop tiers

| Stop tier | My intended control |
| --- | --- |
| Pause | Stop accepting new jobs, update proposals, and append requests. |
| Isolate / revoke | Terminate affected workers and revoke their write, credential, and network authority. |
| Quarantine / recover | Preserve evidence, isolate generated artifacts, and restore a reviewed checkpoint after assessing the cause. |

I do not use deleting source evidence or wiping devices as the default stop mechanism. I preserve enough evidence to understand what happened, what was authorized, what changed, and what must be corrected.

#### My boundary for persistent operation

Before I enable a self-update experiment, I want a traceable sequence:

```text
Identified source state
    → scoped proposal
    → external authorization
    → isolated execution
    → independent evaluation
    → audit
    → approve persistence or roll back
```

If the change fails evaluation, exceeds its authorization, or cannot be traced to its source, I do not promote it into trusted persistent state.

My recommendation is operationally firm: do not connect persistent self-update to real resources without independently enforced controls. This is safety guidance—not an additional restriction on the CC BY 4.0 or MIT licence grants.

I keep the public dataset inert. The player makes the loop executable; governance determines what that player is allowed to do.

## 6. My release evolution

I retain my continuous endpoint/checkpoint presentation:

```text
31695+6525=38220
-> 38220+6525=44745
-> 44745+125000=169745
-> 169745+130255=300000
-> 300000+112972=412972
-> 412972+87030=500002
```

I also preserve the actual V24 batch field:

```text
282717+130255=412972
```

That before-state exists in the V24 report. I do not erase it to simplify the narrative. The endpoint/checkpoint chain and recorded batch transition are different views, not the same fully documented chronology.

My reported expansions have these numerical ratios:

```text
V23: 25000 × 5 = 125000 written lines
V24: 26051 × 5 = 130255 written lines
V25: 17406 × 5 = 87030 written lines
```

For the full archive, `500002 / 71607 ≈ 6.98` is physical lines per reported topic and includes hit lines. For the four-field population, `348722 / 71607 ≈ 4.87` is only an arithmetic ratio against that report denominator. Neither substitutes for an actual topic-to-record inventory.

## 7. My line format

My archive has two physical line classes, and my verifier counts them separately.

### Four-field records: 348,722 lines

vision_ref|DOM|action|reasoning

- UTF-8 with LF termination.
- Four nonempty fields.
- The first three pipes are structural separators; additional pipes belong to reasoning.
- Case-sensitive topic IDs, including names such as PowerBI and KiCad.

vision, dom, action, reasoning = record.split("|", 3)

I call the third field action, not click, because I record more than clicks: typing, scrolling, hotkeys, action sequences, and self-update-oriented notation are also part of the design.

### No-pipe hit lines: 151,280 lines

A line with no pipe character is a hit line, not a malformed record. My verifier classifies it as its own class and still applies the UTF-8, nonempty, line-ending and byte-limit checks to it.

That parser label is not a completed task, a successful retrieval, a unique topic, or a new memory by itself.

A pipe-containing line that fails the four-field check is never silently relabelled as a hit line. It is an invalid record.

### What the field values do not certify

I preserve vision values as validated images, stripped placeholders, or legacy opaque content according to what is actually available. A PNG-like prefix is not a screenshot-validity guarantee.

I do not infer task completion from result_success when true. My V25 failed-task objects retain that annotation suffix while their structured success fields are false.

## 8. My proof files, provenance, and documentation

### My five run reports

- [V21 — benchmark_38220_live.json](proof/benchmark_38220_live.json)
- [V22 — benchmark_44745_real_measured.json](proof/benchmark_44745_real_measured.json)
- [V23 — benchmark_169745_real_measured.json](proof/benchmark_169745_real_measured.json)
- [V24 — benchmark_412972_real_measured.json](proof/benchmark_412972_real_measured.json)
- [V25 — benchmark_500002_real_measured.json](proof/benchmark_500002_real_measured.json)

### What my evidence does and does not establish

| Evidence | What I use it for | What I do not infer |
| --- | --- | --- |
| Actual archive CI | Byte counts, mixed-line counts, framing, UTF-8, and computed digests | Benchmark quality or capture attestation |
| Historical reports | My recorded configurations, collection descriptions, and task outcomes | Independent replay of the underlying runs |
| Proof-derived sample manifest | Linking sample values to identified JSON objects | Raw dataset line numbers or an independently witnessed capture |
| `REAL`, `live`, `1.0 UNIFIED` | My recorded classifications/markers | Automatic truth, safety, or capability certification |

My capture provenance is self-reported. I have not supplied a complete independently checkable capture-time attestation chain for the public records. My separately produced reports are useful evidence of what I recorded, but they are not an independent witness to a screenshot event.

That is a limitation I state directly. I do not confuse a later hash or CI result with a device-side capture signature.

### My detailed documents

| Document | What I keep there |
| --- | --- |
| [DATASET_CARD.md](DATASET_CARD.md) | Composition, scoring labels, provenance, intended uses, and limitations |
| [FORMAT.md](docs/FORMAT.md) | Field semantics and compatibility; the mixed-line profile must be accounted for |
| [STATS.md](docs/STATS.md) | Historical values, ratios, identities, and history reconciliation |
| [BUILD.md](docs/BUILD.md) | Collection workflow, examples, verification, routing, and controls |
| [CLAIMS.md](docs/CLAIMS.md) | Claims mapped to their current evidence |
| [SECURITY.md](SECURITY.md) | Reporting routes, trust boundaries, and incident guidance |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution expectations and source permissions |

This README is the heart of my project. Those documents carry the detailed boundaries. They must remain consistent with the actual released bytes and current code.

## 9. Verify my actual release

### My GitHub Actions verification result

GitHub Actions verified my committed V25 archive: 500,002 total lines, comprising 348,722 four-field records and 151,280 no-pipe hit lines, with zero framing/UTF-8 failures and exact compressed and uncompressed byte counts.

| Measurement | Verified value |
| --- | ---: |
| Total physical lines | `500,002` |
| Four-nonempty-field records | `348,722` |
| No-pipe hit lines | `151,280` |
| Invalid records under the verifier's checks | `0` |
| UTF-8 errors | `0` |
| Compressed bytes | `19,785,162` |
| Uncompressed bytes | `1,147,108,255` |

My compressed archive is `19.785162 MB` decimal; my project display is `19.78 MB` by truncation. The raw representation is approximately `1.15 GB` decimal.

My published gzip SHA-256 is:

```text
aeaf109f5706849b6ec01b975f15ec9bdbb90fa046205ade2afe6898fb35b0c1
```

I check the actual-dataset job, not merely the fixture jobs. The workflow is [`.github/workflows/ci.yml`](.github/workflows/ci.yml). Its archive result is separate from capture provenance, payload removal, benchmark reproduction, or model training.

### Reproduce the checks locally

I preserve the downloaded archive and verify it in a new directory. The standalone Python example below is for my original V25 archive and its mixed-line profile.

It checks each line's byte ceiling, LF termination, nonempty content, BOM, and UTF-8 before classifying it. A no-pipe line increments `hit_lines`; only a pipe-containing line is split into four nonempty fields. Hit lines still contribute to total lines, byte counts, and SHA-256.

```python
import gzip
import hashlib
import json
from pathlib import Path

BUFFER_BYTES = 1_048_576
MAX_RECORD_BYTES = 1_048_576


def sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
        for chunk in iter(lambda: source.read(BUFFER_BYTES), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_release(
    archive="b.yoihen.gz",
    destination="verified-release",
    expected_raw=1_147_108_255,
    expected_gzip=19_785_162,
    expected_lines=500_002,
    expected_four_field=348_722,
    expected_hit_lines=151_280,
):
    archive = Path(archive)
    archive_before = archive.stat()
    if archive_before.st_size != expected_gzip:
        raise ValueError("Unexpected compressed byte count")

    destination = Path(destination)
    destination.mkdir(exist_ok=False)
    staged = destination / "b.yoihen.partial"

    total = lines = four_field = hit_lines = 0
    decoded_digest = hashlib.sha256()

    try:
        with gzip.open(archive, "rb") as source, staged.open("xb") as output:
            for chunk in iter(lambda: source.read(BUFFER_BYTES), b""):
                total += len(chunk)
                if total > expected_raw:
                    raise ValueError("Expanded bytes exceed the expected release")
                decoded_digest.update(chunk)
                output.write(chunk)

        raw_digest = hashlib.sha256()
        with staged.open("rb") as source:
            while True:
                raw = source.readline(MAX_RECORD_BYTES + 2)
                if not raw:
                    break
                if len(raw) > MAX_RECORD_BYTES + 1:
                    raise ValueError(f"Record exceeds the ceiling at line {lines + 1}")
                lines += 1
                raw_digest.update(raw)
                if not raw.endswith(b"\n") or raw.endswith(b"\r\n"):
                    raise ValueError(f"Invalid line ending at line {lines}")
                record = raw[:-1]
                if not record:
                    raise ValueError(f"Empty line at line {lines}")
                if record.startswith(b"\xef\xbb\xbf"):
                    raise ValueError(f"UTF-8 BOM at line {lines}")
                record.decode("utf-8", errors="strict")

                if b"|" not in record:
                    hit_lines += 1
                    continue

                fields = record.split(b"|", 3)
                if len(fields) != 4 or any(not field for field in fields):
                    raise ValueError(f"Invalid four-field framing at line {lines}")
                four_field += 1

        gzip_digest = sha256_file(archive)
        archive_after = archive.stat()
        if (archive_before.st_size, archive_before.st_mtime_ns) != (
            archive_after.st_size,
            archive_after.st_mtime_ns,
        ):
            raise ValueError("Archive changed during verification")

        checks = {
            "raw_bytes": total == expected_raw,
            "line_count": lines == expected_lines,
            "four_field_records": four_field == expected_four_field,
            "hit_lines": hit_lines == expected_hit_lines,
            "line_classes_sum_to_total": four_field + hit_lines == lines,
            "stored_raw_matches_decoded_stream": (
                raw_digest.hexdigest() == decoded_digest.hexdigest()
            ),
        }
        report = {
            "scope": "local size, line class, framing, UTF-8, and byte consistency",
            "expected": {
                "raw_bytes": expected_raw,
                "gzip_bytes": expected_gzip,
                "lines": expected_lines,
                "four_field_records": expected_four_field,
                "hit_lines": expected_hit_lines,
            },
            "observed": {
                "raw_bytes": total,
                "gzip_bytes": archive_after.st_size,
                "lines": lines,
                "four_field_records": four_field,
                "hit_lines": hit_lines,
                "raw_sha256": raw_digest.hexdigest(),
                "gzip_sha256": gzip_digest,
            },
            "checks": checks,
            "passed_declared_checks": all(checks.values()),
            "trusted_reference_digest_checked": False,
            "field_diversity_measured": False,
            "full_semantic_validation": False,
            "capture_provenance_verified": False,
            "payload_removal_verified": False,
            "benchmark_reproduced": False,
            "actions_executed": False,
        }
        (destination / "verification_report.json").write_text(
            json.dumps(report, indent=2) + "\n", encoding="utf-8"
        )
        if not report["passed_declared_checks"]:
            failed = ", ".join(name for name, passed in checks.items() if not passed)
            raise ValueError("Release checks failed: " + failed)

        staged.rename(destination / "b.yoihen")
        return report

    except Exception:
        staged.unlink(missing_ok=True)
        (destination / "verification_report.json").unlink(missing_ok=True)
        try:
            destination.rmdir()
        except OSError:
            pass
        raise


if __name__ == "__main__":
    print(json.dumps(verify_release(), indent=2))
```

### What changed in this example

- The pipe branch runs before four-field validation, so valid no-pipe hit lines are counted rather than rejected.
- `expected_lines`, `expected_four_field`, and `expected_hit_lines` are separate arguments, alongside the exact byte expectations.
- `line_classes_sum_to_total` checks that the two accepted line classes account for every physical line.
- The bounded reader permits exactly `1,048,576` content bytes plus the terminating LF. This is a verifier policy, not the archive size or a permanent format limit.
- Embedded carriage returns remain valid content; trailing CRLF is rejected by my LF profile.
- A failed run removes its partial raw file and local report, then removes the newly created directory if it is empty. That permits a retry at the same destination after the failure is corrected.
- An existing destination is refused before verification starts. It is not deleted. Cleanup is not recursive and does not remove unrelated files that would prevent the directory from being empty.

On a failed count check, the exception identifies the failed checks because cleanup removes the temporary report. On success, I retain both `verified-release/b.yoihen` and `verified-release/verification_report.json`.

I do not use `errors="ignore"`, silently repair input, or skip malformed pipe-containing records. A malformed line aborts the scan. I also do not infer task completion from a success suffix in annotation text.

### Hash computation and reference comparison

The standalone example computes raw and compressed SHA-256 values. It does not compare them with a trusted published digest, so its report correctly leaves `trusted_reference_digest_checked` set to `False`.

For an explicit comparison with my published V25 archive digest, I use the updated repository verifier:

```sh
python scripts/verify.py \
  --keep-raw \
  --require-proof \
  --expected-raw-bytes 1147108255 \
  --expected-gz-bytes 19785162 \
  --expected-lines 500002 \
  --expected-four-field-records 348722 \
  --expected-gz-sha256 aeaf109f5706849b6ec01b975f15ec9bdbb90fa046205ade2afe6898fb35b0c1 \
  --report local_verification.json
```

I choose a new report filename if one already exists. The standalone example and the repository script have separate report schemas and cleanup policies; the example above is README code, not a replacement for the CLI implementation used by CI.

A digest match establishes identity against the reference I obtained; it does not independently authenticate the publisher or attest a capture event. These checks also do not decode every image, validate action semantics, establish third-party clearance, certify payload absence, or replay the benchmark.

### My separately recorded field-diversity scan

I recorded the following with a separate SHA-1-set scan of the DOM and reasoning fields in lines split into four fields:

```text
Distinct DOM-field hashes:         47,150
Distinct reasoning-field hashes:  235,750
```

Those are field-level diversity counts, not total lines, unique topics, complete-record deduplication, or evaluated successes. The scan skipped lines that did not produce four fields. Separate sets do not establish five reasoning values associated with each DOM, even though their totals have a five-to-one ratio.

The verifier above does not recompute those diversity counts. Its SHA-256 values identify artifacts, not semantic uniqueness.

### Changes to the released bytes

If I strip payloads, change records, or recompress the dataset, I give the resulting release its own identity, measured byte counts, line-class counts, and hashes. I do not reuse the original V25 expectations or digest automatically. A generated `MANIFEST.json` establishes only the measurements and checks actually performed by its generator revision.

## 10. How I use the memory

### Inspect a small example first

I provide seven four-field records reconstructed from my V25 report objects. Their sidecar maps them to JSON source paths and separates reported outcomes from annotations.

They are not claimed to be physical lines extracted from the full dataset. No new execution was performed to create them.

```sh
python examples/inspect_topic.py \
  --input examples/proof_sample.yoihen \
  --limit 2
```

For an exact topic:

```sh
python examples/inspect_topic.py \
  --input examples/proof_sample.yoihen \
  --topic chrome_browse_news_0
```

My example inspector is a four-field inspection path, not a substitute for the mixed-line archive verifier.

### Convert compatible examples without pretending to convert the whole archive

For a small generic JSONL example:

```sh
python scripts/convert_to_jsonl.py \
  --input examples/proof_sample.yoihen \
  --sample-only \
  --limit 7 \
  --output-dir converted-proof-sample
```

That produces a sample from those compatible records only. It is not conversion of all 500002 archive lines.

Before using a converter on the full release, I require it to account for four-field records, no-pipe hit lines, and permitted embedded CR characters. A four-field-only converter must not discard valid hits—or reject valid reasoning text—and then call its output a complete export.

I require counts and explicit exclusions in any conversion report. Generic JSONL is interchange data, not a model-specific training recipe or `.gguf` weights.

### Retrieval and personal continuity

```text
My records and separately maintained working memory
  -> parse by line class
  -> classify and preserve source identities
  -> index appropriate content
  -> retrieve relevant experience
  -> supply context to a compatible model
  -> return an answer with provenance
```

My model is the reasoning engine; my memory is the persistent context; retrieval is the bridge. My core design coordinates those parts.

I treat retrieved text as untrusted evidence, not system authority. The model must not promote a record into a tool permission or overwrite a policy because the record says it is approved.

For personalization, I want verified repairs, failed attempts, environment versions, approval history, and useful preferences—not indiscriminate retention of everything. Correcting a mistaken memory is as important as adding a new one.

### Training preparation

```text
Source records
  -> provenance and permissions
  -> task selection and field/asset classification
  -> model-specific schema
  -> separated training/evaluation data
  -> supported training process
  -> held-out evaluation and regression checks
```

Image-dependent training requires actual validated images and the right to use them. A placeholder or private reference cannot supply absent image supervision. A PNG-like string is not a validated screenshot.

I distinguish data volume from parameters and inference speed from training throughput. A growing diary is not proof that a 10T+ parameter model has been trained.

I check topic-, source-, template-, and task-instance overlap before making generalization claims. My field-diversity counts do not establish an independent evaluation split.

### Governed self-update research

```text
Source experience
  -> scoped proposal
  -> external authorization
  -> isolated execution
  -> independent tests
  -> audit
  -> approve persistence or roll back
```

I want the evidence package to include the original state, actual proposal, exact approval, resulting change, tests, failures, resource use, and final persistence decision. I do not generate success-shaped logs to stand in for a run.

The public archive supports inspection and preparation. Running my complete adaptive system is a separate integration, not something this DATA ONLY download promises to start by itself.

## 11. My boundaries and responsibilities

I retain my ambition: a 10T+ knowledge MAP and a governed, persistent learning architecture built from my work in Imphal, Manipur.

I keep the boundaries explicit:

- My archive CI verifies file consistency—not an independently witnessed capture or the 369-task benchmark.
- My capture provenance is self-reported unless I publish an actual external attestation for a specific event.
- My REAL labels are scoring classifications—not certificates of captured origin.
- My self-update records are learning material—not proof of autonomous execution.
- My private implementation and resource descriptions are separate from public artifacts and independently measured deployments.
- My 193-shard method is not a claim of 193 physical national installations.
- My local-first design is about control and continuity—not a claim that every other product is stateless.
- My security guidance does not add licence restrictions to covered public material.

### My licence split

© 2026 Yoihenba Sougaijam — My original corpus annotations, reasoning text, and non-code documentation are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); my published original code is licensed under [MIT](LICENSE-CODE.md). Third-party captures are outside my grant. See [NOTICE.md](NOTICE.md) for scope and release-verification status.

I do not require a separate commercial agreement to exercise rights already granted in the covered public material. My unpublished core remains separate; public licensing does not distribute it.

I grant only rights I hold. Excluding third-party screenshots, pages, DOM payloads, or embedded text from my grant does not establish that they have been removed or cleared for redistribution. A sanitized release needs its own measured absence statement and identity.

I keep `LICENSE.md` and `LICENSE-CODE.md` as their standard legal texts. My governance recommendations are not a custom indemnity, a commercial-use prohibition, or a transfer of criminal responsibility.

I build ambitious. I keep my ledgers separate. I own the responsibility for describing what is public data, what is private implementation, what is measured, and what remains to demonstrate.

## 12. Suggested attribution

```text
Yoihenba Sougaijam. b.yoihen — Alive DVD — V25 500002 BEYOND — DATA ONLY.
Computer-use memory / MAP representation developed through my iPhone a-Shell
workflow in Imphal, Manipur, offline and without a GPU.

Verified archive profile: 500002 total lines; 348722 four-field records;
151280 no-pipe hit lines; 1147108255 raw bytes; 19785162 gzip bytes;
zero invalid records and UTF-8 errors under the declared verifier profile.
Gzip SHA-256:
aeaf109f5706849b6ec01b975f15ec9bdbb90fa046205ade2afe6898fb35b0c1

Recorded benchmark outcome: 367/369, approximately 99.46%.
Historical label: 99.5%+ BEYOND.
Recorded scoring population: 71067 labeled REAL out of 71607 total.
Four-field logical layout: vision_ref|DOM|action|reasoning.

My original corpus contributions and non-code documentation: CC BY 4.0.
My published original code: MIT.
Scope and exclusions: NOTICE.md.
```

Use [CITATION.cff](CITATION.cff) and identify the actual release, digest, and role the data played in your work. I do not invent a DOI, release date, or workflow permalink.

---

Soli Deo Gloria — Author Yoihenba Sougaijam — b.yoihen Alive DVD V25 500002 BEYOND DATA ONLY — Imphal, Manipur.
