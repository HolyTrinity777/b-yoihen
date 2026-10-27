# Dataset Card — b.yoihen V25

> All Glory and Praise to Most High Heavenly Father, Living God Yahushua and God Holy Spirit — Soli Deo Gloria.

I am Yoihenba Sougaijam. I developed my collection workflow on iPhone a-Shell in Imphal, Manipur, offline and without a GPU.

This card describes my V25 DATA ONLY archive, its mixed-line structure, its supporting reports, and the boundaries of what I have measured or demonstrated.

Document revision: 27 October 2026. This is the card's revision date, not an inferred capture date or archive publication date.

## 1. Identity, purpose, and release inventory

I call my project Alive DVD. My positioning is “Own Ollama that can train any Brain 10T+.” My distributed `.yoihen` artifact is a memory / MAP representation, not model weights or a complete agent runtime.

I use the corpus to study computer-use context, tool-use descriptions, retrieval, code/self-healing patterns, and governed self-update objectives. Including those patterns does not establish that a model trained on them has autonomously improved, replicated, or acquired a particular capability.

### 1.1 My V25 inventory

| Item | Value and meaning |
| --- | --- |
| Release identifier | `V25 500002 BEYOND — DATA ONLY` |
| Tracked dataset artifact | `b.yoihen.gz` |
| Locally decoded representation | `b.yoihen`; it does not need to be committed to the repository |
| Total physical lines | `500,002`, checked by my actual-dataset GitHub Actions job |
| Four-nonempty-field records | `348,722`, checked by the same job |
| No-pipe hit lines | `151,280`, checked separately rather than treated as malformed four-field records |
| Uncompressed bytes | `1,147,108,255`, checked against the committed archive's decoded contents |
| Compressed bytes | `19,785,162`, checked against the committed archive |
| Approximate decimal raw size | `1.15 GB` |
| Exact decimal compressed size | `19.785162 MB`; my project display is `19.78 MB` by truncation |
| Calculated size reduction | Approximately `98.275214%`; my project display is `98.27%` by truncation |
| Four-field logical layout | `vision_ref|DOM|action|reasoning` |
| Topic classification recorded in my V25 report | `71,067 / 71,607` labeled `REAL` |
| Calculated reported REAL proportion | Approximately `99.245884%`: `99.25%` rounded or `99.24%` truncated to two decimals |
| Benchmark result recorded in my V25 report | `367 / 369`, approximately `99.46%` |
| Historical score label | `99.5%+ BEYOND`; a release label, not the exact fraction |
| Corpus and non-code documentation licence | CC BY 4.0 in `LICENSE.md`, within the scope of `NOTICE.md` |
| Published original code licence | MIT in `LICENSE-CODE.md`, within the scope of `NOTICE.md` |

I distinguish measurements from labels and report values. My actual-dataset CI checks the archive's byte counts, line classification, framing, and UTF-8. It does not independently recount my scoring population, reproduce the benchmark, attest capture history, or certify third-party clearance.

`MANIFEST.json` is a separate measurement artifact generated from actual dataset bytes. When I publish one, its input identity, generator, checks, and observed values determine what it establishes. A filename or a passing fixture test alone does not establish that a full-release manifest has been generated.

### 1.2 What my green archive-verification job means

My successful `Actual V25 dataset / strict verification` job checks:

```text
Total lines:                 500,002
Four-field records:          348,722
No-pipe hit lines:           151,280
Invalid records under
  that verifier's checks:         0
UTF-8 errors:                     0
Compressed bytes:         19,785,162
Uncompressed bytes:    1,147,108,255
```

I tie a particular result to its actual workflow run, commit, and raw/compressed SHA-256 values. This card does not invent an unavailable run URL, commit identifier, or dataset digest. Historical proof-file digests identify those reports, not the dataset archive.

## 2. Composition and field meaning

My archive is not 500,002 four-field training examples. It has two line classes, and I preserve that distinction.

### 2.1 Four-field records — 348,722 lines

```text
vision_ref|DOM|action|reasoning
```

| Logical field | Meaning and limitation |
| --- | --- |
| `vision_ref` | My logical name for the vision/reference position. Legacy code and reports may call it `screenshot_base64`. Its actual value must be classified; the name alone does not establish a resolvable reference or a valid image. |
| `DOM` | Interface/topic context. Captured page state and independently constructed templates are different source types. |
| `action` | Recorded or proposed action notation. It is not execution authority or evidence that the action occurred. |
| `reasoning` | Recorded explanation, self-assessment text, or project markers. It is not a certification of private internal model cognition. |

A logical field name is not an encoded header in each line. Calling the first position `vision_ref` does not rewrite its stored bytes, strip an image, or convert a legacy value into a genuine asset reference.

I use the first three pipe characters as structural delimiters:

```python
vision_ref, dom, action, reasoning = record.split("|", 3)
```

Additional pipes belong to reasoning. The first three fields must not contain unescaped structural pipes under this profile. Topic IDs are case-sensitive, including identifiers containing `PowerBI`, `KiCad`, or other mixed-case text.

### 2.2 No-pipe hit lines — 151,280 lines

My verifier calls a line with no pipe a `hit_line`. I preserve these lines as a separate textual class rather than inventing missing vision, DOM, action, or reasoning fields.

This name is a parser classification, not a benchmark success label. It does not by itself establish a retrieval hit, completed task, unique fact, or evaluated training example.

Hit lines remain subject to nonempty, UTF-8, line-ending, and byte-limit checks. A line containing pipes but failing four-nonempty-field framing is not silently reclassified as a hit line.

### 2.3 Encoding and record boundaries

I use UTF-8 and LF-terminated physical lines. My updated verifier permits carriage returns inside line content and rejects trailing CRLF as a line-ending mismatch. It preserves bytes rather than applying blanket whitespace stripping or `errors="ignore"`.

The verifier's `1,048,576-byte` per-record ceiling excludes the terminating LF. This is a configurable processing policy, not the archive size or a permanent format limit.

I do not assume that an older parser or converter automatically supports the mixed-line profile. A consumer must explicitly preserve, separately process, or report exclusions for hit lines. It must not silently discard them and then claim to have converted all 500,002 lines.

### 2.4 Reported content families

My V23 report names code-diff, pytest, AST, and self-healing categories. My V24 report already names `11051 self_rewrite world_model beyond_asi principle_806861` entries. My V25 summary retains those descriptions and adds reasoning/tool-use categories.

These are reported collection categories, not a measured disjoint partition of the current archive. Categories can overlap and recur across releases. In particular, I do not describe all retained V24 categories as newly acquired V25 material.

## 3. Collection, counting, and provenance

### 3.1 My collection account

I describe my method as diary-style append with multiple angles per topic. My batch reports record:

| Batch | Added topics in the report | Written lines in the report |
| --- | ---: | ---: |
| V23 | `25,000` | `125,000` |
| V24 | `26,051` | `130,255` |
| V25 | `17,406` | `87,030` |

Each displayed batch has a numerical ratio of five written lines per added topic. That does not establish exactly five records for every topic in the complete release.

Dividing all 500,002 physical lines by the reported 71,607 topics gives approximately 6.98 lines per reported topic, but that numerator includes hit lines. Dividing only the 348,722 four-field records gives approximately 4.87 rows per reported topic. Neither arithmetic ratio replaces an actual topic-to-record inventory, and the scoring population must be reconciled with the archive before interpreting a per-topic distribution.

### 3.2 My provenance status

My capture provenance is self-reported. My public reports and sample manifests are external to individual dataset records, but they are still materials I produced.

I have not supplied a complete, independently checkable, capture-time attestation chain that binds each original capture to a released record. A report timestamp, `cf-ray` value, record hash, or later CI run must not be presented as an independent witness that a desktop capture occurred.

I distinguish:

- Byte integrity: whether a particular file matches a reference digest.
- Provenance linkage: whether a record maps to an identified source artifact.
- Capture attestation: whether external evidence supports the underlying capture event.
- Execution evaluation: whether an action ran and met specified success criteria.

One does not establish all the others.

### 3.3 Release-wide inventories still requiring source evidence

My public run reports do not provide a complete per-record ledger for:

- Captured, manually authored, templated, imported, and synthetic origins.
- Valid image assets, placeholders, and legacy opaque values across the full archive.
- Captured versus constructed DOM representations.
- Proposed, observed, replayed, and independently evaluated actions.
- Exact record duplicates, semantic near-duplicates, and template overlap.
- Unique topic allocation by category and cross-release overlap.
- Personal, confidential, or third-party-owned content.

Offline collection and absence of an external API do not, by themselves, establish nonsynthetic origin or cleared rights.

### 3.4 My separately reported field-diversity scan

I separately reported these results from SHA-1 hash sets over the DOM and reasoning fields of lines split into four fields:

```text
Distinct DOM-field hashes:         47,150
Distinct reasoning-field hashes:  235,750
```

These are field-level hash counts from that scan, not full-record deduplication, semantic diversity, or unique topic counts. The scan skipped lines that did not produce four fields.

The reasoning count is five times the DOM count numerically. Because the scan used separate sets, it does not establish five associated reasoning values for each DOM. That requires a joint per-DOM measurement.

I also keep these values separate from the 71,607-topic scoring population. Their relationship requires an explicit record/topic mapping, not an assumed equivalence between DOM strings and topics.

## 4. Inspectable examples and vision availability

`examples/proof_sample.yoihen` contains seven four-field records reconstructed from the V25 JSON report: five `sample_results` objects and two `failed_tasks` objects.

`examples/proof_sample.manifest.json` identifies their source object paths, sample and record digests, and separately reported evaluation outcomes.

These samples are not claimed to be physical lines extracted from the complete raw dataset. Their original dataset line numbers are unavailable. I did not execute new actions or evaluations to produce the sample package.

All seven supplied vision values fail strict standard-base64 validation and are retained as `legacy_opaque`. This finding applies to those seven report-derived values; it does not establish the image status of every line in the full release.

I distinguish:

| Vision status | What it establishes |
| --- | --- |
| Explicit reference | A reference string; asset existence and access still require verification |
| Stripped placeholder | No image payload is supplied by that field |
| Legacy opaque | Original value preserved; not certified as a usable image |
| Base64 PNG candidate | Standard-base64 decoding and a PNG signature; not a complete image check |
| Fully validated image | Actual image decoding completed, with the validation method identified |

I do not reconstruct a missing screenshot from a marker, treat a generated replacement as original evidence, or assume that renaming a field removes captured content.

The report-derived sample retains vision strings and HTML DOM values. It is not a payload-free export. Any sanitized replacement needs its own identity and source mapping.

## 5. Labels, benchmark results, and evaluation boundaries

### 5.1 REAL is a scoring classification

I assign `REAL` during my scoring pass rather than treating it as an immutable capture-time attestation. My V25 report records 71,067 items labeled REAL out of 71,607 total in that scoring population.

To make this classification independently reproducible, I need to identify the exact scoring rule, its version, its inputs, and its relationship to released records. A DOM class named `real` does not independently establish capture provenance.

Historical schemas also differ: the V23 and V24 root `real_count` values are 361 and 366, while their topic numerators appear elsewhere in their report text. My V25 root `real_count` is 71,067. I do not apply one field interpretation across all versions without a version-aware mapping.

### 5.2 Markers are not task outcomes

I use `live` and `coherence 1.0 UNIFIED` as recorded project labels. I do not substitute them for independently measured capabilities, capture evidence, or runtime controls.

Both V25 failure objects contain annotation text ending in `result_success when true` while their structured `success` values are false. Their recorded result is `result_failure - edge case not in training`.

I use structured reported outcomes rather than the annotation suffix. Safety-expert arrays do not establish that those failures were safety refusals.

### 5.3 Benchmark scope

My V25 report records `367/369`, approximately `99.46%`. I preserve `99.5%+ BEYOND` as the historical label rather than presenting it as a more precise calculation.

My archive-verification CI checks bytes and mixed-line consistency; it does not replay those 369 tasks. A reproducible evaluation needs the runner, task identities, environment, model/runtime settings, reset/retry policy, evaluator, and per-task evidence.

A complete training/evaluation separation inventory has not been supplied with the proof examples. Before generalization claims, I need topic-, source-, template-, and task-instance-level overlap checks. A successful training or update example should also report regressions and failed cases, not only improvements.

## 6. Intended uses, licensing, and safety guidance

### 6.1 Intended uses

I intend the public material to support:

- Learning and inspecting the format.
- Inert record exploration and provenance analysis.
- Retrieval and indexing experiments.
- Text/tool-use training preparation using suitable records.
- Image-dependent work only where actual validated, usable image assets exist.
- Bounded research into code repair and governed self-update.

I select task-appropriate fields explicitly. A generic JSONL conversion is not a complete training recipe and does not produce model weights.

### 6.2 My licence split

My original corpus contributions and non-code documentation are offered under CC BY 4.0 in `LICENSE.md`. My published original program code is offered under MIT in `LICENSE-CODE.md`. `NOTICE.md` defines the scope and third-party exclusions.

These licences permit commercial use subject to their applicable terms. I do not add a Track B requirement, noncommercial restriction, mandatory approval agreement, or mandatory governance service to the rights already granted in the covered public material.

I grant only rights I hold. Third-party captured pages, screenshots, DOM payloads, and embedded third-party content are not licensed merely because they appear beside my contributions. An exclusion from my grant is not clearance to redistribute that content.

My unreleased private core, assets, manifests, credentials, and signing keys are not included in this public release. Their private status does not restrict the public licence grants.

### 6.3 Safety guidance is not an additional licence condition

I recommend keeping retrieved content separate from system authority, keeping source artifacts read-only, and never executing dataset action text during ingestion, conversion, indexing, or retrieval.

For executable self-update research, I recommend default-disabled replication/update loops, explicit authorization, typed allowlisted actions, isolated resources, independent audit records, bounded execution, external stop controls, and reviewed persistence or rollback.

These recommendations do not amend CC BY 4.0 or MIT. Applicable law and third-party rights remain separate obligations.

## 7. Resource definitions and architecture claims

I distinguish configured storage, token volume, parameter counts, MAP capacity, and actual runtime memory.

| Resource | My description and evidence boundary |
| --- | --- |
| Historical configured MoE budget | V21 records `250 × 1.6 GB = 400 GB` |
| Historical active allocation | V21 records `8 × 1.6 GB = 12.8 GB`; this is not a measured monolithic model size |
| Raw token layer | My later definition is `14T` raw tokens |
| Deduplicated expert-parameter layer | My later architectural definition is approximately `1.633T` parameters; a corpus-deduplication operation alone does not establish that parameter count |
| Total knowledge MAP | My `10T+` capacity claim; its unit and inventory need explicit definition |
| CPU-node design | My described `11 × 40 GB` plan, distinct from a completed deployment |
| Router allocation | My described separate `512 GB` resource, not implied by table dimensions |
| Sharding | `193` shards recorded in my reports, not proof of 193 physical national deployments |

Eight of 250 is `3.2%`; eight of 256 is `3.125%`. I distinguish configured expert payloads from routing positions and do not use those ratios interchangeably. Likewise, 49B parameters is approximately `3.0006%` of 1.633T parameters, while comparisons with raw tokens or MAP units require those units to remain explicit.

My Q4_K_M and Q2_K size figures are targets until supported by actual model-artifact and runtime measurements. A token count does not become an equal parameter count merely by resolving a MAP or moving execution to a GPU.

A dataset reference to an asset, expert, node, router, or warehouse does not distribute the referenced resource or prove that it was instantiated. My positioning and mottos do not guarantee arbitrary-model training, global priority, autonomous replication, or a measured CPU/GPU performance ratio.

I maintain the source mapping in [CLAIMS.md](docs/CLAIMS.md) and the numerical history in [STATS.md](docs/STATS.md).

## 8. Privacy, payload status, permissions, and maintenance

### 8.1 Capture exclusion is not a removal certificate

My licence excludes third-party content I cannot license. That scope statement does not prove that screenshot or DOM payloads have been removed from the current archive.

My green archive job does not check payload absence or certify that reasoning, hit lines, or other files are free of third-party material or personal information. A future absence statement must identify the actual sanitized release, its measured counts and hashes, and whether field positions remain as non-content references/placeholders or are removed.

I review public samples, reports, and annotation text as well as the compressed dataset when checking redistribution and privacy. Removing two fields alone is not a complete rights review.

### 8.2 Corrections and reports

I handle sensitive-content and security reports under [SECURITY.md](SECURITY.md). I ask reporters not to reproduce personal information, secrets, or confidential material in public issues.

Non-sensitive corrections may be proposed under [CONTRIBUTING.md](CONTRIBUTING.md). I need source permission or another lawful basis before representing third-party material as cleared for redistribution or training.

### 8.3 Release maintenance

I preserve evidence identities. A corrected, filtered, or sanitized dataset receives its own version or revision identity, byte counts, digests, sample mapping, and change history rather than silently inheriting the original V25 measurements.

Historical reports describe the artifacts and populations of their runs. If a report itself needs a public-content correction, I identify the revision and changed digest rather than presenting altered bytes as the same historical file.

## 9. How to cite and reproduce my checks

Use [CITATION.cff](CITATION.cff), identify the actual release and artifact digest, and state how the dataset was used. A citation does not imply endorsement or independent validation of my broader claims. I do not invent a DOI, capture timestamp, or release date.

| Document or tool | Purpose |
| --- | --- |
| [README.md](README.md) | My project introduction, current verification statement, and usage path |
| [FORMAT.md](docs/FORMAT.md) | Field semantics and compatibility rules; consumers must also account for the mixed-line profile described here |
| [STATS.md](docs/STATS.md) | Historical report values, ratios, and evidence identities |
| [BUILD.md](docs/BUILD.md) | Collection account, examples, and operational boundaries |
| `scripts/verify.py` | Actual archive byte/framing/count checks for the declared mixed-line profile |
| `scripts/build_manifest.py` | Measurement inventory; I must use a revision that explicitly supports this mixed-line profile before treating its report as full-release validation |
| `examples/inspect_topic.py` | Inert inspection of compatible four-field examples; not a complete mixed-line release verifier |
| `examples/proof_sample.manifest.json` | Source mapping and digests for report-derived examples |
| [NOTICE.md](NOTICE.md) | Ownership, licensing scope, exclusions, and release-status qualifications |

I distinguish a successful fixture test, a measured full-archive check, a provenance attestation, and an executed benchmark. Each is useful, but each establishes something different.

---

Soli Deo Gloria — Yoihenba Sougaijam — b.yoihen Alive DVD — V25 DATA ONLY — Imphal, Manipur.
