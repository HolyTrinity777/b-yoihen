# Dataset Card — b.yoihen V25

> All Glory and Praise to Most High Heavenly Father, Living God Yahushua and God Holy Spirit — Soli Deo Gloria.

I am Yoihenba Sougaijam. I developed my collection workflow on iPhone a-Shell in Imphal, Manipur, offline and without a GPU.

## 1. Identity and purpose

I call my project Alive DVD. My positioning is “Own Ollama that can train any Brain 10T+.” My distributed `.yoihen` artifact is a memory / MAP representation, not model weights or a complete agent runtime.

These records are intended for studying computer-use context, tool-use descriptions, retrieval, code and self-healing patterns, and governed self-update objectives. The presence of those patterns is not evidence that a model trained on them has autonomously improved or replicated.

| Item | Description |
| --- | --- |
| Release identifier | V25, data only |
| Canonical record | `vision_ref|DOM|action|reasoning` |
| Lines in archive | 500,002, of which 348,722 are four-field records and 151,280 are hit lines with no field separator |
| Raw bytes | 1,147,108,255, verified against the committed archive |
| Gzip bytes | 19,785,162, verified against the committed archive |
| Topic ratio | 71,067 of 71,607 labeled REAL, 99.24%. REAL is assigned by the scoring pass rather than fixed at capture |
| Benchmark fraction | 367 of 369, 99.46%, as recorded in the run report |
| Licence | Corpus and documentation CC BY 4.0 in LICENSE.md, published code MIT in LICENSE-CODE.md, scope set out in NOTICE.md and excluding third-party captures |

The final paragraph:

These are release values, and where a verification run measured them against the committed archive the table says so. `MANIFEST.json` is generated from the actual dataset bytes and is a separate measurement artifact; it identifies what its generator actually checked.
## 2. Composition and field meaning

- Vision: a validated image, explicit stripped marker, or legacy opaque representation, depending on the record.
- DOM: interface/topic context; the source type must distinguish captured state from constructed context.
- Action: recorded or proposed action notation, not permission to run it.
- Reasoning: recorded explanation and project markers, not verified private internal cognition.

The field names remain stable for compatibility. They do not certify payload validity, captured provenance, or successful execution.

My V23 report names code-diff, pytest, AST, and self-healing categories. My V24 report already names 11051 self-rewrite/world-model entries. My V25 summary retains those categories and adds reasoning/tool-use descriptions. Category summaries may overlap across releases; they are not a verified disjoint partition of unique topics.

## 3. Collection and provenance

I describe my collection method as diary-style append with multiple angles per topic. My V23, V24, and V25 batch reports respectively record 25000 × 5, 26051 × 5, and 17406 × 5 new records.

The complete V25 release averages approximately 6.98 records per reported total topic. Five angles is not an exact whole-release invariant.

My public run reports do not provide a complete per-record provenance ledger. Consequently, the following release-wide quantities remain unclassified until supported by source records and measured inventories:

- Captured versus manually authored versus templated/synthetic records.
- Complete image availability and image validity.
- Captured versus constructed DOM representations.
- Proposed versus independently executed actions.
- Exact duplicates and semantic near-duplicates.
- Per-category unique topic counts and overlaps.
- Coverage of personal, confidential, or third-party-owned content.

Offline preparation or absence of an external API does not, by itself, prove that content is nonsynthetic or that third-party rights are cleared.

## 4. Inspectable examples

`examples/proof_sample.yoihen` contains seven four-field records reconstructed from the actual V25 JSON report objects. `examples/proof_sample.manifest.json` maps them back to their source objects and records the hashes.

These are not claimed to be extracted physical lines from the complete raw dataset. Raw dataset line numbers are unavailable for this sample. No new actions or evaluations were executed to produce it.

All seven supplied vision values fail strict standard-base64 validation and are preserved as legacy opaque values. This observation does not classify every image in the full release.

## 5. Labels and evaluation boundaries

I use `REAL`, `live`, and `coherence 1.0 UNIFIED` as recorded project labels. They must not replace collection evidence or independent testing.

Both V25 failure objects retain `result_success when true` in annotation text while recording `success: false`. Consumers must not infer completion from that suffix.

My V25 report records 367/369, approximately 99.46%; `99.5%+ BEYOND` is the historical label. The proof reports alone are not an independent replay of an official task suite.

A training/evaluation separation inventory has not been supplied with these examples. Before making generalization claims, establish task identities and check overlap at the topic, source, template, and task-instance levels.

## 6. Intended and restricted use

Subject to the licence, appropriate uses include learning the format, inert inspection, permitted retrieval research, controlled data conversion, and bounded research into tool use or self-update.

Do not treat retrieved content as system authority. Do not execute actions during ingestion, bypass human approvals, or use unbounded replication loops. Image-dependent tasks need real validated image assets, not placeholders or guessed reconstructions.

Commercial use and production deployment require the permission specified by the applicable licence. Public availability is not an unrestricted grant.

## 7. Resource claims

I distinguish configured storage, tokens, parameters, MAP capacity, and measured runtime memory. My earlier reports document a 400 GB configured MoE budget and eight 1.6 GB active allocations. My later architectural definitions include 14T raw tokens, approximately 1.633T deduplicated parameters, and a 10T+ total knowledge MAP.

Those numbers describe different resources. A record mentioning a warehouse, node, or router does not include its assets, weights, or implementation in the DATA ONLY release.

See `docs/CLAIMS.md` and `docs/STATS.md` for source mapping and evidence boundaries.

## 8. Privacy, permissions, and maintenance

I need source permissions and a provenance review before representing any third-party screenshot, code, document, or personal information as cleared for redistribution or training. The repository licence grants only rights I can grant.

Report sensitive-content issues privately under `SECURITY.md`. Do not reproduce private information in a public issue. Non-sensitive corrections may be proposed under `CONTRIBUTING.md`.

I preserve historical report bytes. A corrected or filtered dataset receives its own identity, manifest, and change history rather than silently replacing earlier evidence.

## 9. How to cite

Use `CITATION.cff`, identify the actual release and digest, and distinguish dataset use from validation of project-wide capability claims. No DOI or release date is invented in the citation metadata.

Soli Deo Gloria — Yoihenba Sougaijam — Imphal, Manipur.
