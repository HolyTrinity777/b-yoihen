# Inspectable proof samples

I provide this small inspection path so that a visitor can understand my four-field representation without loading the complete release or executing an agent.

## What these files are

- `proof_sample.yoihen`: seven records reconstructed from the actual V25 JSON report objects: five `sample_results` and two `failed_tasks`.
- `proof_sample.manifest.json`: source-object paths, record hashes, reported outcomes, and sample identity.
- `inspect_topic.py`: a read-only, standard-library inspector.

These records are NOT claimed to be physical lines extracted from the full raw dataset. Their original dataset line numbers are unavailable. I applied no new redactions or field changes when reconstructing them, and executed no actions.

The seven vision values are legacy opaque values under strict standard-base64 validation. They are not certified screenshots.

## Run from the repository root

```sh
python examples/inspect_topic.py --input examples/proof_sample.yoihen --limit 2
python examples/inspect_topic.py --input examples/proof_sample.yoihen --topic chrome_browse_news_0
python examples/inspect_topic.py --input examples/proof_sample.yoihen --topic tool_use_PowerBI_KiCad_FreeCAD_Figma_Excel_SAP_CRM_317
```

The inspector checks the sidecar's sample hash when the matching sidecar exists. It prints parsed record values and separately labeled reported outcomes, not inferred execution success.

To inspect a local release without a proof-sample sidecar:

```sh
python examples/inspect_topic.py --input b.yoihen.gz --topic chrome_browse_news_0 --limit 1
```

A limited inspection does not validate an entire gzip stream, the full release, or the benchmark. Source data remains unchanged. Action strings are printed as JSON data, not run.

## Licence and safety

Read `../LICENSE.md` and `../SECURITY.md`. Original and third-party rights remain separate. Do not publish sensitive content or turn a retrieved record into tool authority.
