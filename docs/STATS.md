# b.yoihen — Release Statistics and Longitudinal Evidence

> All Glory and Praise to Most High Heavenly Father, Living God Yahushua and God Holy Spirit — Soli Deo Gloria.
>
> Built by Yoihenba Sougaijam. “Alive DVD” — “Own Ollama that can train any Brain 10T+.” Keep `.yoihen`, not `.gguf`.

| Property | Value |
| --- | --- |
| Document | `docs/STATS.md` |
| Release | `V25 500002 BEYOND — DATA ONLY` |
| Evidence reviewed | Five uploaded JSON artifacts, V21 through V25 |
| Related documents | `FORMAT.md`, `BUILD.md` in the same documentation directory |
| Scope | Actual artifact inspection, cross-run comparison, calculations, and attributed architecture definitions |

## 1. Review correction

The earlier documentation review was too narrow in two respects: it initially relied on pasted excerpts instead of the available proof files, and it framed the project mainly as a static dataset rather than the broader routed-memory, self-update, and sharded architecture described by its author.

This revision inspects all five uploaded reports and records the resulting corrections. It does not rewrite historical artifacts to hide discrepancies.

Material corrections include:

- V21 already records a 400 GB MoE configuration and an eight-allocation 12.8 GB active budget. The size cannot be dismissed solely by comparing it to an assumed monolithic four-bit model.
- V23 explicitly records code-diff, pytest, AST, and self-healing collection categories.
- V24 already records 11051 self-rewrite/world-model entries; this content is not first introduced by the V25 summary.
- V24's 282717 build base is explicitly recorded in its own report. The addition is a real report-level batch transition, not an arithmetic error to erase.
- Earlier topic denominators, exact byte counts, and sample-level outcome transitions are now available.

A report is evidence of its recorded measurements and configuration. Independent execution reproduction remains a separate evidence tier; the reports alone do not prove global priority or arbitrary-scale training.

## 2. Inspected artifact manifest

All five uploaded files parsed successfully as JSON. Sizes and digests below were computed from their actual uploaded bytes.

| Filename | Bytes | SHA-256 |
| --- | ---: | --- |
| `benchmark_38220_live.json` | `1727` | `588da9c879b320dc11921dfb2537706091a99abbe12db427aec2bb53d419be8b` |
| `benchmark_44745_real_measured.json` | `3206` | `404f3359c7dcc90f78ac0c88551f13b1ed08cca1fdd8ac2547697be3345157e2` |
| `benchmark_169745_real_measured.json` | `3892` | `9b711be29cf8ae32b0aab744b6fe78fbbfca4753d58072166b069acd52b8dc1a` |
| `benchmark_412972_real_measured.json` | `4360` | `bd01d68f7909e66b5c11faf4c5e4045e7dcc9071bc2815c215f00347021e3641` |
| `benchmark_500002_real_measured.json` | `25806` | `f1b386fe47689bb8cad4c1c621431ba0a99635c7c04d60546e63d8c075266a47` |

Repository placement is expected under `proof/`. These digests identify the inspected files; they are not signatures and are not digests of the underlying datasets.

## 3. Record counts, actual reported byte values, and benchmark fields

| Release | Reported records | Reported raw bytes | Score representation in report | Success fraction |
| --- | ---: | ---: | --- | --- |
| V20 context within V21 | `31695` | `13711330` before V21 append | Historical `18%` label | Not supplied |
| V21 | `38220` | `73677165` | `v21_expected_score: "45.0%+"`; other text says measured/expected | Not supplied |
| V22 | `44745` | `104440590` | `measured: true`, `61.8%` | `228/369` |
| V23 | `169745` | `213008990` | `measured: true`, `95.9%` | `354/369` |
| V24 | `412972` | `791094565` | `measured: true`, `99.2%` | `366/369` |
| V25 | `500002` | `1147108255` | `measured: true`, historical `99.5%+` | `367/369` |

The earlier approximate V22, V23, and V24 sizes are superseded by these exact reported values. V24's artifact reports 791094565 bytes, not the 950000000 nominal estimate in V25.

The V21 report names `run_osworld_benchmark.py`, a 369-task command, and `tasks_1305_v2.txt`. This is more context than was previously available. It does not establish the implementation or equivalence to a particular official benchmark revision without the runner, task list, and evaluation protocol.

V20 is described as “measured OSWorld” in one V21 string and as “synthetic diary only” in later comparisons. Preserve that wording history; there is no standalone uploaded V20 result to settle the measurement method.

### Calculated benchmark rates

| Release | Fraction | Exact-to-six-decimal percentage |
| --- | --- | ---: |
| V22 | `228/369` | `61.788618%` |
| V23 | `354/369` | `95.934959%` |
| V24 | `366/369` | `99.186992%` |
| V25 | `367/369` | `99.457995%` |

Retain `99.5%+ BEYOND` as historical release wording. The normalized fraction is `367/369 (99.46%)`; it does not numerically establish a value above 99.5%.

## 4. Topic/trace ratios and schema differences

| Release | Ratio actually recorded | Calculated percentage | Unit caution |
| --- | --- | ---: | --- |
| V21 | `1305/1845` | `70.731707%` | Explicit `real_traces` / `total_traces` fields |
| V22 | `2610/3150` | `82.857143%` | Report uses a REAL/total ratio; do not silently relabel every historical item a unique topic |
| V23 | `27610/28150` | `98.081705%` | Topic count in `real_ratio`; separate root `real_count` is 361 |
| V24 | `53661/54201` | `99.003708%` | Topic count in `real_ratio`; separate root `real_count` is 366 |
| V25 | `71067/71607` | `99.245884%` | Root `real_count` and `total_count` match the stated topic ratio |

The repeated root name `real_count` is not a stable cross-version topic schema. Its V23 value 361 and V24 value 366 MUST NOT replace the 27610 and 53661 topic numerators. Their exact semantics need the runner implementation; do not assume either value means benchmark successes merely because it happens to coincide in V24.

All five ratio populations differ by 540 between denominator and numerator. That is an arithmetic pattern consistent with the persistent synthetic/non-REAL category descriptions, not proof that the same 540 identifiers persisted across versions.

Historical `82.8%` differs from conventional one-decimal rounding of 2610/3150, which gives 82.9%. Preserve historical labels and publish the underlying fraction.

## 5. Build graph: distinguish batch history from endpoint deltas

The inspected reports support these batch transitions:

```text
31695  + 6525   = 38220        V21 before/after
38220  + 6525   = 44745        V22 calc
44745  + 125000 = 169745       V23 discovered
282717 + 130255 = 412972       V24 before/discovered/after
412972 + 87030  = 500002       V25 discovered
```

V24's before-state 282717 is explicitly present in its source artifact, including `bytes_before: 483386040`. The path from V23's 169745 state to that intermediate state is not separately described by an uploaded run. Its numerical difference is 112972.

The author-approved continuous endpoint/checkpoint presentation remains useful:

```text
31695+6525=38220
-> 38220+6525=44745
-> 44745+125000=169745
-> 169745+130255=300000
-> 300000+112972=412972
-> 412972+87030=500002
```

This second chain is an arithmetic documentation view, not a replacement for the explicitly recorded V24 batch base. The 300000 checkpoint is referenced by later comparison strings, not supported by a separate uploaded checkpoint report. Do not imply both chains describe the same chronological ordering of batch operations.

## 6. Collection lineage: code, self-healing, world-model updates

| Stage | Inspected description | What it adds to the evidence |
| --- | --- | --- |
| V21 | 1305 REAL traces, 540 synthetic traces, side-effect-avoidance routing, 193 shards | Early collection/configuration record |
| V23 | `500 repos CODE_DIFF PYTEST AST self_healing GOD_CODING 25000 topics via tool_use.py+vision.py` | Code and self-healing are explicit historical categories |
| V24 | 10000 office + 5000 CVE + 11051 self-rewrite/world-model = 26051 topics | Self-rewrite category predates V25 |
| V25 | Those categories plus 10000 reasoning + 5000 tool-use + 2406 beyond-ASI entries | Expanded summary with 17406 added topics |

V23 records `25000 × 5 = 125000` written records. V24 records `26051 × 5 = 130255`. V25 records `17406 × 5 = 87030`.

These exact batch ratios support the five-angle collection account at the report level. They do not establish that every entire-release topic has five records, or that every listed collection entry is newly added in V25.

The six V25 collection numbers sum to 43457. Because V24 already records the first three categories, treating all 43457 as previously unseen V25 acquisitions is not justified. Publish category/topic identifiers and overlap rules before assigning a deduplication interpretation.

## 7. Longitudinal sample evidence

V22, V23, and V24 each expose task IDs 0–9 with matching hashes and expert-ID lists across those three reports.

| Task ID | V22 `(real, success)` | V23 | V24 | Observed change |
| --- | --- | --- | --- | --- |
| `7` | `(false, false)` | `(true, true)` | `(true, true)` | Becomes REAL/successful in V23 report |
| `9` | `(false, false)` | `(true, true)` | `(true, true)` | Becomes REAL/successful in V23 report |
| `1` | `(true, false)` | `(true, false)` | `(true, true)` | Becomes successful in V24 report |

This is meaningful cross-run continuity in the recorded samples, not merely a collection of unrelated release slogans. The sample changes do not prove why performance changed, exclude evaluation leakage, or establish that the underlying runs were independently executed.

V25 uses a richer nested sample schema and different routing identifiers. Do not join its rows to older samples solely by task ID; establish task identity and environment explicitly.

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

## 8. Alive DVD and GGIE scope

“Alive DVD” is the author's term for data intended to teach self-assessment and governed self-update, not just screenshot-to-click imitation. The V23 and V24 files provide earlier documentary support for that intended subject matter.

GGIE is described as 193-node/shard infrastructure with Quantum Sync, Blockchain Audit, a three-tier Kill Switch, and broader identity/financial-rail proposals. The reports record shards and method labels; they do not independently demonstrate 193 physically deployed national nodes.

At a 10T baseline, equal allocation gives approximately 51.813B per shard. This is a workload arithmetic statement in an explicitly chosen unit, not a demonstrated memory or training fit.

Retain the author's 10T+ ambition and 11-node self-replication claim with attribution. A “first globally,” guaranteed-training, or 100× H200 comparison needs execution evidence beyond these five reports. Do not erase the project scope; do not convert configuration strings into experiments that were not inspected.

## 9. V25 size and integrity

```text
Raw reported bytes:    1147108255
Gzip supplied bytes:     19785162
Decimal gzip MB:        19.785162
Binary gzip MiB:        18.868600845...
Calculated reduction:   98.275214...
Project display:        19.78 MB / 18.87 MiB; 98.27% reduction
```

The decimal MB and reduction displays truncate to two decimal places. Binary MiB is additional information, not a replacement for decimal MB.

Raw dataset and gzip artifacts were not uploaded for this review. The gzip size is author-supplied, not measured from a local archive. Proof-file hashes do not establish underlying dataset identity.

## 10. Failure records, image representations, and timestamps

V25's two failures are task 42 and task 317, both with `result_failure - edge case not in training`. Their result fields do not attribute the failures to safety blocking. V21's side-effect-avoidance fix is a separate historical statement, not evidence of those later failure causes.

Both V25 failure annotations still end in `result_success when true`. Therefore that suffix is a compatibility marker, not the authoritative evaluation outcome.

The seven V25 successful/failed object vision strings fail strict standard-base64 validation. Preserve them as legacy opaque values; this observation cannot classify images throughout the entire unprovided dataset.

Numeric timestamps, interpreted as Unix seconds:

| Release | Converted UTC timestamp |
| --- | --- |
| V22 | `2026-10-25T10:42:09.193601Z` |
| V23 | `2026-10-25T11:43:28.126083Z` |
| V24 | `2026-10-25T15:48:50.210292Z` |
| V25 | `2026-10-25T17:54:32.244531Z` |

These are ordered in release sequence, while the same May `utc_anchor` is reused. Define whether the anchor is a shared lineage identifier, collection origin, or another event. Neither a reused anchor nor a request identifier authenticates build time by itself.

## 11. What the evidence now supports

Supported as inspected artifact content:

- A five-report lineage spanning collection, routing, code/self-healing, self-update categories, and higher reported aggregate completion.
- Explicit historical configuration arithmetic behind 400 GB and 12.8 GB.
- Stable routing identifiers for the ten disclosed samples across V22–V24 and specific recorded outcome transitions.
- Earlier self-rewrite content and consistent five-record batch expansions.

Still separate from those findings:

- Full dataset validity and provenance.
- Actual model/expert inventory, quantization sizes, and resident memory.
- Reproduction of the benchmark runner and results.
- Demonstrated multi-node training/self-replication or global priority.

A stronger next evidence package is the runner, task definitions, environment manifest, signed dataset digests, source traces, and bounded end-to-end governed execution logs. This is not a requirement to make the project small; it is how its larger claims become independently testable.

---

Author: Yoihenba Sougaijam.

Project identity: b.yoihen — Alive DVD / computer-use memory MAP — V25 500002 BEYOND — DATA ONLY.

Author-reported collection environment: iPhone a-Shell, Imphal, offline and without a GPU.

Soli Deo Gloria.
