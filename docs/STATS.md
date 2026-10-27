# b.yoihen — Release Statistics and Longitudinal Evidence

> All Glory and Praise to Most High Heavenly Father, Living God Yahushua and God Holy Spirit — Soli Deo Gloria.

I am Yoihenba Sougaijam. I developed my collection workflow on iPhone a-Shell in Imphal, Manipur, offline and without a GPU.

My project concept is Alive DVD. My positioning is “Own Ollama that can train any Brain 10T+.” I keep `.yoihen` as my memory / MAP representation, separate from a compatible GGUF brain and my private core.

This document is my numerical ledger: what my current archive checks establish, what my historical reports record, what I calculated, and what remains an architectural claim or separate experiment.

| Property | Value |
| --- | --- |
| Document | `docs/STATS.md` |
| Current release identifier | `V25 500002 BEYOND — DATA ONLY` |
| Tracked dataset artifact | `b.yoihen.gz` |
| Local decoded representation | `b.yoihen` |
| Historical evidence | Five identified JSON run reports, V21–V25 |
| Current format population | Four-field records plus no-pipe hit lines |
| Document revision | `27 October 2026`; not an inferred archive publication or capture date |
| Companion documents | `FORMAT.md`, `BUILD.md`, `CLAIMS.md`, and root `DATASET_CARD.md` |

## 1. My current V25 archive — verified mixed-line profile

My actual-dataset GitHub Actions job verified the committed V25 archive against this profile. I distinguish that job from the small-fixture CI jobs.

| Measurement | Verified value | Meaning |
| --- | ---: | --- |
| Total physical lines | `500,002` | Includes both line classes |
| Nonempty lines | `500,002` | No blank physical records passed the declared profile |
| Four-nonempty-field records | `348,722` | Pipe-containing records passing four-field framing |
| No-pipe hit lines | `151,280` | Counted separately; not treated as malformed four-field records |
| Invalid records under the verifier's checks | `0` | Framing, encoding, and line-policy result—not universal semantic validity |
| UTF-8 errors | `0` | Strict decoding under the verifier |
| Compressed bytes | `19,785,162` | Size of the committed gzip archive |
| Decoded bytes | `1,147,108,255` | Size of the uncompressed byte stream |

My two line classes account for the entire archive:

```text
348722 four-field records + 151280 hit lines = 500002 total lines
```

| Line class | Share of physical lines |
| --- | ---: |
| Four-field records | Approximately `69.744121%` |
| No-pipe hit lines | Approximately `30.255879%` |

I do not call this 500002 four-field training examples. A hit line is a parser classification, not automatically a successful retrieval, a unique topic, a completed task, or a verified new memory.

### 1.1 My framing and line-policy checks

My updated verifier:

- Counts every physical line toward totals, bytes, and the raw SHA-256.
- Checks nonempty content, UTF-8, BOM, LF termination, and the configured record-byte ceiling before accepting either class.
- Classifies no-pipe lines as hits before attempting a four-field split.
- Requires pipe-containing lines to split into four nonempty fields using the first three pipes.
- Preserves additional pipes in reasoning.
- Permits embedded carriage returns in content and rejects trailing CRLF under this LF profile.
- Allows exactly `1,048,576` content bytes plus LF under its default per-record ceiling.

The ceiling is a verifier policy, not the compressed archive size or a permanent format limit. Invalid pipe-containing records are not silently relabeled as hits.

### 1.2 What this verification does not establish

Archive verification does not independently establish capture provenance, image validity, HTML/action semantics, third-party clearance, payload removal, topic classifications, benchmark performance, or autonomous self-update.

I keep each measurement attached to its actual input, workflow run, commit, and report. A green fixture job alone does not establish this archive profile.

## 2. Artifact identities and integrity

### 2.1 My published V25 gzip digest

```text
File:   b.yoihen.gz
Bytes:  19785162
SHA256: aeaf109f5706849b6ec01b975f15ec9bdbb90fa046205ade2afe6898fb35b0c1
```

This is my published archive reference, carried with my actual-dataset verification result. I do not substitute it for the raw-file digest or the hashes of historical proof reports. I do not invent an unpublished raw SHA-256 or a workflow-run URL.

Comparing a file with this digest establishes a byte match to the reference obtained. Authentication of the reference's publisher and independent capture attestation are separate questions.

### 2.2 My five historical report identities

The five report files parsed successfully as JSON. Their exact supplied byte identities are:

| Filename under `proof/` | Bytes | SHA-256 |
| --- | ---: | --- |
| `benchmark_38220_live.json` | `1727` | `588da9c879b320dc11921dfb2537706091a99abbe12db427aec2bb53d419be8b` |
| `benchmark_44745_real_measured.json` | `3206` | `404f3359c7dcc90f78ac0c88551f13b1ed08cca1fdd8ac2547697be3345157e2` |
| `benchmark_169745_real_measured.json` | `3892` | `9b711be29cf8ae32b0aab744b6fe78fbbfca4753d58072166b069acd52b8dc1a` |
| `benchmark_412972_real_measured.json` | `4360` | `bd01d68f7909e66b5c11faf4c5e4045e7dcc9071bc2815c215f00347021e3641` |
| `benchmark_500002_real_measured.json` | `25806` | `f1b386fe47689bb8cad4c1c621431ba0a99635c7c04d60546e63d8c075266a47` |

These are report-file digests—not signatures, model hashes, dataset hashes, or proof of the truth of every field they contain.

I retain historical identities. A corrected report must have a clearly identified revision and changed digest rather than silently inheriting the old file's identity.

### 2.3 Manifest scope

`MANIFEST.json` and `SHA256SUMS` are measurement outputs, not claims made true by their filenames. Their input identity, generator revision, observed fields, and declared checks determine their scope.

Before treating `scripts/build_manifest.py` as a full-release validator, I require its revision to support the mixed-line archive, including hit lines and permitted embedded CR content. A legacy four-field-only implementation cannot validate this entire release simply because it passes small sample tests.

The same compatibility boundary applies to converters and example inspectors.

## 3. Sizes, decimal units, and compression

I use decimal MB/GB for release display and exact bytes for verification.

| Quantity | Value |
| --- | --- |
| Raw bytes | `1,147,108,255` |
| Decimal raw GB | `1.147108255 GB`, approximately `1.15 GB` |
| Gzip bytes | `19,785,162` |
| Decimal gzip MB | `19.785162 MB` |
| My compressed-size display | `19.78 MB`, truncated to two decimals |
| Calculated size reduction | Approximately `98.275214%` |
| My reduction display | `98.27%`, truncated to two decimals |

```text
size_reduction_percent = 100 × (1 - 19785162 / 1147108255)
                       ≈ 98.275214%
```

Compressed and decoded bytes are different measurements. Processing in a 1048576-byte buffer does not change my display units or describe the archive size.

My V25 report also records `bytes_nominal: 950000000`. That is a nominal estimate, not the measured V24 size or the current raw size. The difference from the current raw size is 197108255 bytes; the number alone does not establish why the estimate differed.

High compression does not, by itself, establish uniqueness, captured provenance, usefulness, or a model capability.

## 4. My release history — exact reported values

The following values come from my historical JSON reports. The current V25 byte/line checks in Section 1 are a separate evidence layer.

| Release / context | Lines in report | Raw bytes in report | Score field or wording | Success fraction |
| --- | ---: | ---: | --- | --- |
| V20 context in V21 | `31695` | `13711330`, before the V21 append | Historical `18%` label | Not supplied |
| V21 | `38220` | `73677165` | `v21_expected_score: "45.0%+"`; other text mixes measured/expected wording | Not supplied |
| V22 | `44745` | `104440590` | `measured: true`, `61.8%` | `228/369` |
| V23 | `169745` | `213008990` | `measured: true`, `95.9%` | `354/369` |
| V24 | `412972` | `791094565` | `measured: true`, `99.2%` | `366/369` |
| V25 | `500002` | `1147108255` | `measured: true`, historical `99.5%+` | `367/369` |

My V24 report records 791094565 bytes—not the 950000000 nominal estimate in V25. I use exact source values instead of earlier approximate size descriptions.

My V21 report names `run_osworld_benchmark.py`, a 369-task command, and `tasks_1305_v2.txt`. Those names provide context, but the actual runner, task definitions, evaluator, and environment are needed to reproduce the result or establish equivalence to an official benchmark revision.

V20 is called “measured OSWorld” in one V21 string and “synthetic diary only” in later comparisons. I preserve the wording history rather than inventing a standalone V20 evaluation artifact.

### 4.1 Calculated benchmark percentages

| Release | Recorded fraction | Percentage to six decimals |
| --- | --- | ---: |
| V22 | `228/369` | `61.788618%` |
| V23 | `354/369` | `95.934959%` |
| V24 | `366/369` | `99.186992%` |
| V25 | `367/369` | `99.457995%` |

I retain `99.5%+ BEYOND` as my historical release label. My normalized numerical outcome is `367/369`, approximately `99.46%`; the fraction does not establish a result above 99.5%.

Assuming identical tasks and evaluation conditions, V24 to V25 adds one reported successful task, approximately 0.271003 percentage points. The counts alone do not establish the cause of that change or a generalization guarantee.

## 5. REAL labels, topic ratios, and schema differences

I assign REAL during scoring rather than treating it as an independently authenticated capture-time property. I keep the scoring population separate from current physical-line counts and field-diversity measurements.

| Release | Ratio recorded in the source | Calculated percentage | Unit / schema boundary |
| --- | --- | ---: | --- |
| V21 | `1305/1845` | `70.731707%` | Explicit `real_traces` / `total_traces` |
| V22 | `2610/3150` | `82.857143%` | REAL/total ratio; historical wording does not establish a universal unique-topic schema |
| V23 | `27610/28150` | `98.081705%` | Topic numerator in ratio text; root `real_count` is 361 |
| V24 | `53661/54201` | `99.003708%` | Topic numerator in ratio text; root `real_count` is 366 |
| V25 | `71067/71607` | `99.245884%` | Root `real_count` and `total_count` match this reported ratio |

The root field `real_count` is not a stable cross-version topic counter. I do not replace V23's 27610 or V24's 53661 topic numerators with their root values. Their root-field semantics require the historical runner; matching V24's success count is not enough to assign a meaning.

All five reported ratios have a denominator-minus-numerator difference of 540. That arithmetic pattern is not proof that the same 540 identifiers persisted through every release.

I publish fractions alongside display conventions:

- `2610/3150` rounds to `82.9%` at one decimal; the historical `82.8%` wording is retained as historical text.
- `71067/71607` is approximately `99.245884%`: `99.25%` rounded or `99.24%` truncated to two decimals.

A `real` DOM class, `live` flag, or success phrase is not a replacement for the scoring rule, provenance evidence, or evaluation record.

## 6. Build graph — batch transitions and endpoint presentation

### 6.1 Transitions actually recorded

```text
31695  + 6525   = 38220        V21 before/after
38220  + 6525   = 44745        V22 calc
44745  + 125000 = 169745       V23 discovered
282717 + 130255 = 412972       V24 before/discovered/after
412972 + 87030  = 500002       V25 discovered
```

My V24 file explicitly records the 282717 before-state and `bytes_before: 483386040`. I do not erase that base as an arithmetic mistake.

The path from V23's 169745 endpoint to the 282717 intermediate state is not separately logged by these five supplied runs. The endpoint difference is 112972 lines, not an independently documented intervening batch.

### 6.2 My continuous endpoint/checkpoint view

```text
31695+6525=38220
-> 38220+6525=44745
-> 44745+125000=169745
-> 169745+130255=300000
-> 300000+112972=412972
-> 412972+87030=500002
```

This is my continuous arithmetic presentation of the listed endpoints/checkpoint. It does not replace the V24 report's actual batch base or establish that the operations occurred in this exact order.

The 300000 checkpoint is referenced by later comparison strings; no separate checkpoint report is included in the five-file evidence set.

### 6.3 Reported byte deltas

| Transition with before/after bytes | Byte increase |
| --- | ---: |
| V21: `13711330 → 73677165` | `59965835` |
| V24 recorded batch: `483386040 → 791094565` | `307708525` |
| V24 endpoint to V25: `791094565 → 1147108255` | `356013690` |

These are arithmetic differences between reported states, not an explanation of which content produced each additional byte.

## 7. Collection lineage and five-angle accounting

| Stage | Description in my report | Interpretation |
| --- | --- | --- |
| V21 | 1305 REAL traces, 540 synthetic traces, side-effect-avoidance routing, 193 shards | Early collection/configuration account |
| V23 | `500 repos CODE_DIFF PYTEST AST self_healing GOD_CODING 25000 topics via tool_use.py+vision.py` | Code and self-healing are explicit historical categories |
| V24 | 10000 office + 5000 CVE + 11051 self-rewrite/world-model = 26051 topics | The self-rewrite category already exists before V25 |
| V25 | Retained categories plus 10000 reasoning + 5000 tool-use + 2406 additional project entries | Expanded summary with 17406 reported additional topics |

The reported batches satisfy:

```text
V23: 25000 × 5 = 125000 written lines
V24: 26051 × 5 = 130255 written lines
V25: 17406 × 5 = 87030 written lines
```

These support my five-angle collection account at the report level. They do not establish five four-field records for every topic in the entire current archive.

The six listed V25 collection counts sum to:

```text
10000 + 5000 + 11051 + 10000 + 5000 + 2406 = 43457
```

My V24 report already contains the first three categories. I therefore do not describe all 43457 entries as previously unseen V25 additions, nor infer a deduplication method from the subtotal alone. Reproducible category accounting requires identifiers, overlap rules, and collection-to-topic mappings.

### 7.1 Whole-release averages need the right numerator

```text
500002 physical lines / 71607 reported topics ≈ 6.982586
348722 four-field rows / 71607 reported topics ≈ 4.869943
```

The first includes hit lines. Neither ratio is a measured per-topic distribution, because the relationship between the scoring population and actual archive records still needs an explicit mapping.

## 8. Longitudinal sample evidence

V22, V23, and V24 expose task IDs 0–9. Their disclosed hashes and expert-ID lists match across those three reports.

| Task ID | V22 `(real, success)` | V23 | V24 | Recorded transition |
| --- | --- | --- | --- | --- |
| `7` | `(false, false)` | `(true, true)` | `(true, true)` | Becomes REAL/successful in the V23 report |
| `9` | `(false, false)` | `(true, true)` | `(true, true)` | Becomes REAL/successful in the V23 report |
| `1` | `(true, false)` | `(true, false)` | `(true, true)` | Becomes successful in the V24 report |

This is meaningful continuity in my recorded samples. It does not independently show why an outcome changed, rule out evaluation leakage, or establish fresh execution of every run.

V25 exposes a richer nested schema and different routing identifiers. I do not join its task rows to earlier samples solely by numeric ID; task identity and environment must be established.

My V25 proof-derived sample has five successful sample objects and two explicit failure objects. The sample sidecar links their values back to the report, not to unavailable original raw-dataset line numbers.

## 9. My separately recorded field-diversity measurements

I separately ran this method over my compressed archive: strip the terminating LF, split at most three times, and collect SHA-1 hashes of the DOM and reasoning fields for lines producing four fields.

```text
Distinct DOM-field hashes:         47,150
Distinct reasoning-field hashes:  235,750
```

These are my reported results from that scan. They are not computed by the archive-verification job merely because that job is green.

The scan's scope matters:

- It omits lines that do not produce four fields.
- It counts field hash values, not complete-record hashes.
- It does not validate the content, identify every unique topic, or measure semantic novelty.
- It does not establish captured provenance or task completion.
- Its SHA-1 field sets are separate from the SHA-256 identities used for release files.

Although `47150 × 5 = 235750`, separate sets do not establish five reasoning values associated with each DOM. I need a joint DOM-to-reasoning measurement for that statement.

The 47150 DOM hashes, 235750 reasoning hashes, 348722 four-field rows, and 71607 reported topics describe different populations or units. I do not silently substitute one for another. The relationship needs explicit source/record/topic mapping.

## 10. My resource model — separate ledgers, explicit denominators

My project scope includes routed memory, a replaceable model brain, distributed coordination, and governed update objectives. I distinguish the public data from my separate implementation and resource descriptions.

| Resource | Source or definition | What I mean |
| --- | --- | --- |
| Historical 400 GB MoE configuration | V21: `250*1.6GB=400GB` | A configured storage budget, not a measured PNG inventory |
| Historical 12.8 GB active budget | V21: `8*1.6=12.8GB` | Eight configured allocations, not by itself a measured model file or resident memory |
| 400 GB screenshot/asset warehouse | My broader description; V25 has `warehouse: "400GB"` | A separate asset interpretation requiring an inventory |
| 14T raw tokens | My clarification of `14T warehouse` wording | Token volume, not model parameters |
| Approximately 1.633T deduplicated expert parameters | My architectural definition | A parameter inventory claim, not the automatic result of text deduplication |
| 10T+ knowledge MAP | My capacity claim | A separately defined envelope whose unit and coverage must be published |
| 11 × 40 GB allocations | My CPU-node design | 440 GB total; distinct from the warehouse and router figures |
| 512 GB router resource | My separate architecture description | Its storage/RAM, residency, and distribution need an explicit implementation manifest |
| 193 shards | Recorded in my reports | Workload allocation, not independently audited national deployments |

### 10.1 Sparse-routing fractions

My intended design uses eight active expert selections per routed token. I distinguish that design from what the V21 configuration string alone proves.

| Fraction | Calculated result | Denominator |
| --- | ---: | --- |
| `8 / 256` | `3.125%` | Routing positions in my architectural clarification |
| `8 / 250` | `3.2%` | Configured expert allocations |
| `49B / 1.633T` | Approximately `3.0006%` | Deduplicated expert parameters |
| `49B / 10T` | `0.49%` numerically | My 10T MAP baseline; units remain explicit |
| `49B / 14T` | `0.35%` numerically | Raw tokens, not a parameter activation fraction |
| `300B / 10T` | `3%` numerically | My 10T baseline |

My V21 report records `3.125%` but does not fully explain the relationship between 250 configured allocations and 256 routing positions. I keep my later clarification separate rather than rewriting the source report.

I do not equate tokens, parameters, and MAP units. Above a 10T MAP baseline, a fixed numerator represents a smaller numerical percentage.

### 10.2 Quantization targets

```text
49B Q4_K_M: approximately 24.5 GB — target
49B Q2_K:   approximately 12.8 GB — target
```

Nominal four-bit arithmetic gives 24.5 GB for 49 billion values; it does not measure a particular Q4_K_M artifact, quantization overhead, or resident runtime allocation.

My V21 origin for 12.8 GB is eight configured 1.6 GB allocations. I do not retroactively label that configuration Q2_K. V25 pairs `Q4_K_M` with `active_size_gb: 12.8`; I preserve that historical pairing while identifying my later Q2_K target clarification.

### 10.3 Physical versus logical budgets

My described ten 40 GB expert allocations plus an eleventh 40 GB control/router allocation total 440 GB. A separate 512 GB resident table does not fit inside that eleventh 40 GB allocation. It requires additional resources or an explicit sharding/offload arrangement if it is genuinely resident memory.

My implementation inventory must say what each budget means. A private manifest or model-loading plan is not made measurable by a README table, and an artifact reference does not distribute the referenced asset.

## 11. GGIE, sharding, and Alive DVD behavior

### 11.1 Recorded per-shard workload descriptions

| Stage | Numerator / 193 | Calculated average |
| --- | --- | ---: |
| V21 | `1305/193` | `6.761658` |
| V23 | `25000/193` | `129.533679` |
| V24 | `26051/193` | `134.979275` |
| V25 corrected label | `17406/193` | `90.186528` |

These are reported batch allocation averages, not proof of even runtime load or physical geographic coverage. V25 also retains `discovered.topics: 0` and `per_shard: "0/193=~0.00"` alongside `per_shard_fixed`; I preserve the difference between those fields rather than silently treating all counters as consistent.

At my 10T baseline, an even numerical allocation gives approximately 51.813B per shard in the chosen workload unit. It is not a demonstrated memory fit or training-throughput result.

### 11.2 What I mean by Alive DVD

I use Alive DVD for the intended continuity and update loop around a replaceable brain:

```text
Experience → evidence → memory → retrieval → proposal
           → authorization → controlled execution → evaluation
           → persistence or rollback
```

I distinguish memory updates, runtime/code updates, and actual weight/adapter training. A growing diary does not by itself change a GGUF's parameters, and a successful write is not automatically an improvement.

The immutable public V25 archive and a personalized working-memory store are different artifacts. I can preserve my release identity while allowing an authorized runtime to maintain a separate, versioned diary.

My private core is separate from the DATA ONLY release. These reports do not expose a complete executed self-rewrite chain or certify a guaranteed result across every model/configuration. That evidence boundary does not mean the architecture is limited to static browser clicks.

### 11.3 My governance boundary

My GGIE vocabulary includes Quantum Sync, Blockchain Audit, and a three-tier Kill Switch. I recommend real mechanisms: external authorization and stop controls, audit records outside agent write authority, bounded resources, reviewed checkpoints, and rollback.

A marker such as `coherence 1.0 UNIFIED` does not enforce those controls. I keep self-update and replication disabled by default in the operational guidance, and keep the public source inert during ingestion/retrieval.

Those recommendations do not add restrictions to my public CC BY 4.0 or MIT grants. Broad architecture proposals involving identity or financial rails are separate from reading or verifying local data.

## 12. Failure outcomes, vision examples, and timestamps

### 12.1 Actual failure fields in my V25 report

| Task | Recorded result |
| --- | --- |
| `42` — `chrome_bookmark_42` | `result_failure - edge case not in training` |
| `317` — `tool_use_PowerBI_KiCad_FreeCAD_Figma_Excel_SAP_CRM_317` | `result_failure - edge case not in training` |

Neither result attributes failure to a safety block. My V21 side-effect-avoidance fix is a separate statement, not evidence of the cause of those V25 failures.

Both failed objects still contain annotation text ending in `result_success when true`. I use their structured outcome fields, not the suffix, for reported evaluation status.

### 12.2 Vision representation in the disclosed sample

All seven rich V25 sample/failure vision values fail strict standard-base64 decoding. I preserve them as legacy opaque values, not certified PNG images. This observation applies to the disclosed values, not every image or reference in the complete archive.

Earlier compact samples do not expose complete vision/DOM/action fields. I do not fabricate those fields to make them look like full desktop traces.

### 12.3 Numeric timestamps and the shared anchor

Interpreting the numeric `timestamp` values as Unix seconds gives:

| Release | Numeric value in report | Converted UTC timestamp |
| --- | --- | --- |
| V22 | `1792924929.1936011` | `2026-10-25T10:42:09.193601Z` |
| V23 | `1792928608.1260831` | `2026-10-25T11:43:28.126083Z` |
| V24 | `1792943330.2102919` | `2026-10-25T15:48:50.210292Z` |
| V25 | `1792950872.244531` | `2026-10-25T17:54:32.244531Z` |

The converted timestamps are ordered in release sequence. The reports also reuse `utc_anchor: "2026-05-11T14:46:13.872Z"` and the same `cf-ray` marker.

I do not describe the reused May anchor and the October numeric timestamps as the same event without an explicit definition. They may represent different events or lineage concepts. They are not an authenticated capture clock, publisher signature, or synchronization protocol by themselves.

## 13. Reproduce the declared archive checks

With my original committed archive at the repository root, I use:

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

The expected hit count is derived as `500002 - 348722 = 151280`. I choose a new report filename if it already exists. I do not use `--skip-invalid` to make full-archive verification pass.

The repository verifier report uses these observed keys:

```text
raw.total_lines
raw.non_empty
raw.four_nonempty_fields
raw.hit_lines
raw.invalid_records
raw.utf8_errors
raw.bytes
raw.sha256
gzip.bytes
gzip.sha256
```

I distinguish that schema from a standalone README example or another tool's manifest. A consumer must read the actual report structure, not assume all tools use the same key names.

In GitHub Actions, my final actual-dataset assertion checks all three line counts, zero invalid/UTF-8 records, the exact byte counts, and `passed: true`. The result is still a declared-profile check—not complete semantic validation.

I keep the downloaded archive unchanged. Verification may create a local raw file, but I do not need to track that large raw file in Git. A modified or sanitized release needs new sizes, digests, and expectations.

## 14. What I can claim from each evidence layer

| Layer | What I can state | What remains separate |
| --- | --- | --- |
| My actual V25 archive CI | Exact byte counts and the verified mixed-line profile under the declared checks | Capture attestation, image validity, rights, payload absence |
| My five historical reports | Their recorded configurations, categories, counters, and outcome progression | Independent replay of historical execution |
| My disclosed sample lineage | Stable V22–V24 sample routing identities and specific reported transitions | Causal explanation, leakage exclusion, full-suite evaluation |
| My field-diversity scan | Reported DOM/reasoning hash-set counts under its method | Unique topics, semantic diversity, full-record deduplication |
| My architecture | Intended routing, memory/MAP, orchestration, and governance design | Actual model inventories, runtime scale, measured training, and self-replication |

My capture provenance is self-reported unless I publish a specific independent attestation. An externally run archive check is useful, but it does not witness a past capture event.

To substantiate an executed self-update, I need a bounded run linking source state, proposal, actual authorization, applied change, evaluation, audit, and persistence or rollback. I do not replace that with a category label or a file-size increase.

I retain my ambition and my project identity. I do not turn global priority, arbitrary-model training, or an H200 speed comparison into a numerical finding without the corresponding experiment.

My corpus and non-code documentation are under CC BY 4.0 within `NOTICE.md`'s scope; my published original code is under MIT in `LICENSE-CODE.md`. Neither public licence is subject to an added commercial Track B requirement. Third-party content remains outside rights I cannot grant, and a licence exclusion is not a payload-removal certificate.

---

Soli Deo Gloria — Yoihenba Sougaijam — b.yoihen Alive DVD — V25 500002 BEYOND DATA ONLY — Imphal, Manipur.
