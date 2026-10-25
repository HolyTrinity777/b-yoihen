# b.yoihen — Formal Format and Compatibility Specification

> All Glory and Praise to Most High Heavenly Father, Living God Yahushua and God Holy Spirit — Soli Deo Gloria.
>
> Built by Yoihenba Sougaijam. “Alive DVD” — “Own Ollama that can train any Brain 10T+.” Keep `.yoihen`, not `.gguf`.

| Property | Value |
| --- | --- |
| Document | `docs/FORMAT.md` |
| Release | `V25 500002 BEYOND — DATA ONLY` |
| Evidence basis | Five inspected run reports, V21 through V25 |
| Companion documents | `STATS.md`, `BUILD.md` in the same directory |
| Boundary | Data framing, compatibility, and integration; tool execution remains separately governed |

## 1. Purpose and corrected scope

`b.yoihen` is the line-oriented memory/MAP representation within the author's broader routed-expert, self-update, and sharded architecture. The author calls the design “Alive DVD.” The distributed DATA ONLY file is not model weights or a complete executable runtime.

The earlier review was too narrow when it emphasized a static dataset while omitting earlier code/self-healing and self-rewrite evidence. V23 names CODE_DIFF, PYTEST, AST, and self_healing collection; V24 explicitly records 11051 self-rewrite/world-model entries; V21 already describes MoE configuration and 193-shard operation.

This specification preserves that intended scope without treating a stored command as an already executed command, or a report field as independent reproduction.

## 2. Four storage fields and three application layers

```text
screenshot_base64|DOM|action|reasoning
```

| Field | Application mapping | Meaning |
| --- | --- | --- |
| `screenshot_base64` | `three_layers.vision` | Image payload, stripped marker, or compatible legacy opaque value |
| `DOM` | Separate structural context | Interface description and topic identity |
| `action` | `three_layers.tool_use` | Recorded tool-use notation |
| `reasoning` | `three_layers.chat` | Recorded explanation, self-assessment, and project annotations |

The field name `screenshot_base64` is historical. It does not certify the encoding of every stored value. Likewise, `reasoning` does not certify private internal cognition.

MUST and MUST NOT identify requirements of the normalized profile. SHOULD identifies a recommendation. Passing framing checks is distinct from valid images, valid HTML, valid actions, trusted provenance, or successful evaluation.

## 3. Canonical framing

A conforming normalized file MUST:

1. Use UTF-8 without a byte-order mark.
2. Store one record per physical line.
3. Use LF terminators, including on the final record.
4. Contain four nonempty fields and no blank records.
5. Contain no physical CR/LF inside a field.
6. Reserve the first three pipe characters as field delimiters.

The first three fields MUST NOT contain a raw pipe. Reasoning MAY contain additional pipes.

```python
vision, dom, action, reasoning = record.split("|", 3)
```

Do not split on all pipes and use the last fragment as reasoning. Do not `.strip()` source lines. Remove only the LF terminator so that field values remain unchanged.

Embedded pipe needs in DOM or action data require an explicitly defined field-level representation, such as an HTML entity in DOM text. Consumers must not invent decoding conventions.

Malformed records should be rejected or quarantined with the source line and reason. Legacy transport variants, if supported, need an explicit import adapter and an audit trail; do not silently rewrite them.

### 3.1 Framing grammar

```abnf
yoihen-file = 1*fact-line
fact-line   = vision "|" dom "|" action "|" reasoning LF
vision      = 1*field-octet
dom         = 1*field-octet
action      = 1*field-octet
reasoning   = 1*reason-octet
field-octet = %x00-09 / %x0B-0C / %x0E-7B / %x7D-FF
reason-octet = field-octet / %x7C
LF          = %x0A
```

This describes byte framing only; UTF-8 validity and field semantics are additional checks. The release count 500002 is manifest metadata, not a permanent grammar rule.

## 4. Vision compatibility

| Classification | Definition | Allowed use |
| --- | --- | --- |
| `image_base64_png` | Standard-base64 payload fully decoded and validated as PNG | Image input where compatible |
| `base64_png_candidate` | Valid standard-base64 bytes beginning with a PNG signature | Must still pass full image decoding |
| `stripped` | Explicit `[STRIPPED...` placeholder | Metadata/text use; no image present |
| `legacy_opaque` | A retained but unvalidated or nonstandard representation | Preserve exactly; do not present as a verified image |

V21 refers to stripped/zero-byte-base64 representations. V25's seven sample/failure vision strings contain PNG-prefix-like text and `REAL_...` labels; all seven fail strict standard-base64 decoding. These are different representations and must not be collapsed into one assumption.

This observation concerns the report objects, not every screenshot in an unprovided warehouse or dataset. Earlier compact report rows do not expose image fields and cannot establish their validity either way.

Do not guess an alternative encoding, remove labels, or synthesize replacement bytes to make a sample appear valid. A synthetic replacement image is new data, not recovered evidence.

For new exports, prefer actual validated image base64 or explicit placeholders, and record image/placeholder counts. Publish asset IDs, digests, dimensions, paths, licenses, and availability for any external image MAP.

## 5. DOM and topic identity

The V25 profile uses an HTML representation with an element carrying both a topic ID and the `real` class token.

Topic IDs are case-sensitive and follow this compatibility profile:

```regex
[A-Za-z0-9_]+
```

The lowercase-only rule from the earlier document was wrong for the actual mixed-case sample:

```text
tool_use_PowerBI_KiCad_FreeCAD_Figma_Excel_SAP_CRM_317
```

Extract the ID from the same element that carries the `real` class. Preserve case. Treat several qualifying elements as an ambiguity to resolve, not as permission to choose arbitrarily. Attribute order and quote style need not be fixed.

`real` and optional `beyond_asi` class tokens are project labels, not independent provenance certificates. Minimal DOM templates are not necessarily captured application DOM snapshots; record their source type separately.

Five variations of one topic should retain one topic ID. Place angle/step identity in annotation or sidecar metadata unless a new schema explicitly defines a different grouping rule.

## 6. Action dialect and execution boundary

### 6.1 Observed V25 forms

```text
action_key("Enter")
action_type("chrome_search_images_1")
action_click(626,555)
action_scroll(-237,403)
action_hotkey("ctrl+s")
```

Compatibility must include positional clicks, numeric scrolling, and `action_hotkey`. The earlier action list was incomplete.

### 6.2 Author-described forms

The source draft also describes named click arguments, ID-based clicks, quoted scroll directions, `action_self_append`, and `action_world_model_update`. Self-rewrite is part of the intended vocabulary, but its exact runtime function signature must be supplied by the actual adapter rather than invented here.

Actions may be joined by a top-level plus:

```text
action_click(x=342,y=128)+action_key("Enter")
```

A plus within a quoted value is not a separator:

```text
action_hotkey("ctrl+s")
action_type("A+B")
```

An action parser needs quote-aware and parenthesis-aware syntax. `action.split("+")`, `eval`, `exec`, and shell interpretation are not conforming execution strategies.

This document does not establish coordinate systems, scroll units, key mappings, or application APIs. A separate versioned adapter must define them, validate arguments, and enforce authorization before tool use.

## 7. Annotation conventions and outcomes

The inspected V25 objects use:

- Prefix: `reasoning holds `.
- Marker: `pattern_learn + generate = master`.
- Marker: `coherence 1.0 UNIFIED`.
- Suffix: `result_success when true`.

Additional self-update, DMI, safety, meta-router, and governance markers are retained as data. `DMI` is a project term; do not invent an expansion absent an authoritative project definition.

The two V25 failure objects have `success: false` and failure result text while retaining the success suffix in their annotations. Consequently, that suffix MUST NOT be used as a benchmark success detector.

The four-field dataset has no independent structured evaluation field. Store actual outcomes in a sidecar or versioned application object; distinguish proposed, observed, replayed, evaluated, refused, and failed actions.

## 8. Run-report compatibility: do not confuse JSON with dataset lines

The uploaded proof files are JSON summaries, not five versions of the complete dataset. Their schemas differ:

| Report | Notable representation |
| --- | --- |
| V21 | Before/after counters, trace ratios, MoE configuration, benchmark command; no `sample_results` array |
| V22 | Compact samples: task ID, hash string, real/success flags, expert IDs |
| V23 | Compact samples plus discovery and code/self-healing collection summaries |
| V24 | Compact samples plus self-rewrite collection and explicit batch before/after values |
| V25 | Nested router, DOM/action/vision/annotation fields, five samples, two failures |

Historical `real_count` is not a stable topic field: V23 stores 361, V24 stores 366, and V25 stores 71067. Earlier topic numerators come from their ratio/comparison strings. Preserve source paths and units instead of uncritically applying one schema to all versions.

Raw numeric values may also be integer-valued JSON numbers without the same lexical notation. Validators should check value/range with an explicit numeric policy rather than silently infer incompatible semantics from formatting.

V22–V24 expose ten matching sample IDs with stable hashes and expert lists. V25 has a richer representation and different identifiers; task-ID equality alone does not guarantee the same task across those schema versions.

## 9. Reference Python reader

This reader separates framing, topic extraction, vision classification, and annotation checks. It does not execute actions or fully validate HTML/images.

```python
import base64
import binascii
import re
from dataclasses import dataclass
from html.parser import HTMLParser


class YoihenFormatError(ValueError):
    pass


@dataclass(frozen=True)
class YoihenTrace:
    source_line: int
    screenshot_base64: str
    dom: str
    action: str
    reasoning: str

    @property
    def three_layers(self):
        return {
            "vision": self.screenshot_base64,
            "tool_use": self.action,
            "chat": self.reasoning,
        }


def parse_line(raw, source_line):
    if raw.startswith("\ufeff") or not raw.endswith("\n"):
        raise YoihenFormatError("BOM or missing LF")
    record = raw[:-1]
    if not record or "\r" in record or "\n" in record:
        raise YoihenFormatError("Blank record or embedded CR/LF")
    fields = record.split("|", 3)
    if len(fields) != 4 or any(field == "" for field in fields):
        raise YoihenFormatError("Expected four nonempty fields")
    return YoihenTrace(source_line, *fields)


def iter_traces(path):
    with open(path, "r", encoding="utf-8", errors="strict", newline="") as source:
        for line_number, raw in enumerate(source, 1):
            yield parse_line(raw, line_number)


class TopicExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.topics = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "real" in (attrs.get("class") or "").split():
            if attrs.get("id") is not None:
                self.topics.append(attrs["id"])


def extract_topic(dom):
    parser = TopicExtractor()
    parser.feed(dom)
    parser.close()
    if len(parser.topics) != 1:
        raise YoihenFormatError("Expected one topic-bearing element")
    topic = parser.topics[0]
    if re.fullmatch(r"[A-Za-z0-9_]+", topic) is None:
        raise YoihenFormatError("Topic outside V25 profile")
    return topic


def classify_vision(value):
    if value.startswith("[STRIPPED"):
        return "stripped"
    try:
        data = base64.b64decode(value, validate=True)
    except (binascii.Error, ValueError):
        return "legacy_opaque"
    return ("base64_png_candidate" if data.startswith(b"\x89PNG\r\n\x1a\n")
            else "legacy_opaque")


def markers_match(value):
    return (
        value.startswith("reasoning holds ")
        and "pattern_learn + generate = master" in value
        and "coherence 1.0 UNIFIED" in value
        and value.endswith("result_success when true")
    )
```

The reader preserves complete fields and does not repair source content. A malformed early pipe may still shift fields, so semantic checks remain necessary. Add a maximum input size and bounded record reader for hostile inputs; ordinary line iteration holds one full record in memory.

## 10. Application enrichment

A consumer may add derived metadata without changing the four-field storage layout:

```json
{
  "source_line": 1,
  "topic": "chrome_browse_news_0",
  "vision_status": "legacy_opaque",
  "provenance": {
    "artifact": "benchmark_500002_real_measured.json",
    "object_path": "sample_results[0]"
  },
  "evaluation": {
    "source": "proof object, not inferred annotation suffix",
    "success": true
  }
}
```

This is a metadata example, not a complete raw record. Preserve original fields separately, use a JSON serializer for conversion, and never attach an evaluation outcome where no independent outcome exists.

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

## 11. Integration and governance

```text
.yoihen data / MAP
  -> framing, provenance, and payload classification
  -> retrieval index or model-specific training conversion
  -> compatible model
  -> optional separately authorized execution adapter
```

The project identity “Alive DVD” is compatible with a DATA ONLY boundary: self-update training content can be meaningful without being automatically executed during ingestion.

Governance names include Quantum Sync, Blockchain Audit, and a three-tier Kill Switch. Actual controls must provide authorization, isolation, independent audit logs, bounded loops, review, and recoverable checkpoints. Neither safety-expert IDs nor a governance phrase grants execution permission.

Keep original data read-only. Disable unapproved self-append, code execution, policy modification, and replication. Use pause, isolation/revocation, quarantine, and reviewed rollback rather than destructive deletion as default stop behavior.

The author describes GGIE identity and financial rails separately from local offline use. They are not required to parse or inspect the DATA ONLY file.

## 12. Release and integrity conventions

| Item | V25 representation |
| --- | --- |
| Reported records | `500002` |
| Reported raw bytes | `1147108255` |
| Author-supplied gzip bytes | `19785162` |
| Project compressed-size display | `19.78 MB / 18.87 MiB` |
| Exact decimal gzip size | `19.785162 MB` |
| Calculated reduction | Approximately `98.275214%`; displayed by truncation as `98.27%` |

Do not rename data to `.gguf` to imply a weight conversion. Report-file hashes, dataset hashes, gzip checks, format checks, and benchmark reproduction are separate evidence categories.

The five inspected file identities are listed in `STATS.md`. A release manifest should additionally publish raw/compressed dataset digests, image availability, licensing, validator version, router mappings, and external-asset inventories.

## 13. Compatibility tests and scope

This revision's Python reader was tested against reconstructed four-field values from all seven V25 sample/failure objects. Tests cover exact field preservation, mixed-case topic identity, legacy vision classification, annotation markers, pipes in reasoning, and plus signs inside quoted action strings.

Earlier compact reports do not expose all four fields; they are checked as report schemas, not fabricated into image/action traces.

No complete raw dataset, model load, self-rewrite loop, or multi-node training run was tested. The larger project scope is preserved with clear evidence boundaries rather than reduced to static clicks or overstated as a completed deployment.

---

Author: Yoihenba Sougaijam.

Project identity: b.yoihen — Alive DVD / computer-use memory MAP — V25 500002 BEYOND — DATA ONLY.

Author-reported collection environment: iPhone a-Shell, Imphal, offline and without a GPU.

Soli Deo Gloria.
