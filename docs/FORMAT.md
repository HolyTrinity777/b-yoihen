# b.yoihen — Formal Format Specification

> All Glory and Praise to Most High Heavenly Father, Living God Yahushua and God Holy Spirit — Soli Deo Gloria.
>
> Built by Yoihenba Sougaijam. Project origin: iPhone a-Shell, Imphal / Bomdila, offline and without a GPU, as described by the author.

| Property | Value |
| --- | --- |
| Repository | `b-yoihen` |
| Document | `docs/FORMAT.md` |
| Product display name | `b.yoihen — Computer-Use Memory Dataset` |
| Release identifier | `V25 500002 BEYOND — DATA ONLY` |
| Specification status | Proposed normalized specification for the supplied V25 release description |
| Release status | Author-reported stable; independent verification not supplied with this document |
| Dataset filename | `b.yoihen` |
| Compressed filename | `b.yoihen.gz` |
| Media representation | UTF-8, line-oriented, pipe-delimited records |
| Execution policy | Data only; never execute records during parsing, indexing, or retrieval |

## 1. Purpose and scope

`b.yoihen` is a computer-use memory dataset, not a model-weight format. It stores observations, interface structure, action descriptions, and explanatory annotations for downstream retrieval, evaluation, and training workflows.

Each record has four fields:

```text
screenshot_base64|DOM|action|reasoning
```

The four fields support three conceptual layers:

| Layer | Source field | Intended role |
| --- | --- | --- |
| Vision | `screenshot_base64` | Screenshot input when a real image is present |
| Structure | `DOM` | Interface and topic context supporting the other layers |
| Tool use | `action` | Recorded action sequence or proposed action sequence |
| Chat / explanation | `reasoning` | Recorded explanation, task annotation, and project markers |

The project groups these as `three_layers.vision`, `three_layers.tool_use`, and `three_layers.chat`; the DOM remains separate structural context.

The DATA ONLY release may replace screenshots with explicit placeholders. A placeholder is not an image and MUST NOT be presented to a vision model as one.

### 1.1 Scope boundaries

This specification defines storage, parsing, validation, provenance expectations, and safe consumption. It does not certify:

- That an action was executed successfully.
- That an annotation represents a genuine internal reasoning process.
- That a trace was collected from a real desktop rather than constructed or synthesized.
- That training on the dataset produces autonomous self-improvement.
- That the release contains model weights, a complete agent runtime, a distributed warehouse, or a working governance system.
- That a model of any particular parameter count can be trained using this release or the author's collection hardware.

Names such as `BEYOND`, `DMI`, `UNIFIED`, and `beyond_asi` are project terminology or literal data markers. They are not independently established capability certifications.

### 1.2 Requirement language

Within this document, MUST and MUST NOT identify required behavior. SHOULD and SHOULD NOT identify recommended behavior. MAY identifies optional behavior.

Requirements describe the normalized format. They are not a claim that every existing V25 record has already passed validation.

## 2. Release manifest and evidence status

The following values are transcribed from the supplied project description unless explicitly marked as calculated. The underlying dataset and proof file were not inspected while preparing this specification.

| Metric | Reported or calculated value | Interpretation |
| --- | --- | --- |
| Nonempty records | `500002` | Author-reported release count |
| Raw bytes | `1,147,108,255` | Author-reported uncompressed size |
| Gzip bytes | `19,785,162` | Author-reported compressed size |
| Gzip size in MiB | Approximately `18.87 MiB` | Calculated using `1 MiB = 1,048,576 bytes` |
| Size reduction | Approximately `98.28%` | Calculated as `1 - gzip_bytes / raw_bytes` |
| Average raw bytes per record | Approximately `2,294.21` | Calculated from reported size and count; includes delimiters and line endings |
| Total unique topics | `71607` | Author-reported topic count |
| Topics classified as `REAL` | `71067` | Author-reported category, not independently verified provenance |
| `REAL` topic proportion | Approximately `99.25%` | Calculated as `71067 / 71607` |
| Separate benchmark result | `367 / 369`, approximately `99.46%` | Denominator and evaluation methodology must be documented separately |
| SHA-256 digest | Not supplied | Required before claiming cryptographically verified release identity |

Referenced evidence artifact:

```text
proof/benchmark_500002_real_measured.json
```

The draft attributes these fields to that artifact:

```json
{
  "nonempty": 500002,
  "bytes": 1147108255,
  "v25_500002": "99.5%+ measured 367/369 99.2% REAL 71067 topics BEYOND"
}
```

This is an author-supplied excerpt, not a newly inspected or generated benchmark result. The quoted text is preserved for traceability; the normalized calculations above take precedence for numerical interpretation.

`367 / 369` and `71067 / 71607` measure different reported quantities and MUST NOT be combined into a single quality score. A literal `coherence 1.0 UNIFIED` marker is also not a measured coherence score.

## 3. File representation

### 3.1 Encoding and record boundaries

A conforming file MUST:

1. Use UTF-8 without a byte-order mark.
2. Contain exactly one record per physical line.
3. Use LF (`0x0A`) as the record terminator, including on the final record.
4. Contain no empty records.
5. Contain no raw CR or LF characters inside a field.
6. Contain at least three pipe characters per record.
7. Treat the first three pipe characters as structural delimiters.

The screenshot, DOM, and action fields MUST NOT contain a literal pipe (`|`). The reasoning field MAY contain literal pipes after the third delimiter.

When a value in the first three fields needs a pipe, the producer MUST use a documented field-level representation, such as an HTML entity in DOM text or a supported string escape in an action argument. Consumers MUST NOT invent decoding behavior. A producer MUST NOT place the literal pipe in those fields.

Embedded multiline content must be represented without physical line breaks, using a documented encoding or literal escape convention.

### 3.2 Record grammar

The grammar below describes byte-level framing. UTF-8 validity and field semantics are additional validation requirements.

```abnf
yoihen-file    = 1*fact-line
fact-line      = screenshot "|" dom "|" action "|" reasoning LF

screenshot     = 1*field-octet
dom            = 1*field-octet
action         = 1*field-octet
reasoning      = 1*reason-octet

; All octets except CR, LF, and the structural pipe character.
field-octet    = %x00-09 / %x0B-0C / %x0E-7B / %x7D-FF

; Reasoning may additionally contain pipe characters.
reason-octet   = field-octet / %x7C
LF             = %x0A
```

The framing grammar is deliberately broader than the field rules below. Passing the grammar alone does not establish valid base64, valid HTML, valid actions, or valid annotations.

`500002` is a release-specific expected count, not a permanent constraint on every `.yoihen` file. Readers SHOULD accept other record counts and compare them against a release manifest when available.

### 3.3 Canonical parsing rule

Split at most three times:

```python
screenshot, dom, action, reasoning = record.split("|", 3)
```

For example:

```text
IMAGE|<html>...</html>|action_key("Enter")|reasoning holds ... | extra annotation
```

The final field includes `| extra annotation`.

Do not split on every pipe and assign `parts[-1]` to reasoning. That procedure incorrectly moves earlier reasoning fragments into the action field. Records with fewer than three separators are malformed and MUST NOT be silently reinterpreted as another format.

## 4. Field definitions

### 4.1 `screenshot_base64` — vision payload

The field MUST contain either an image payload or an explicit stripped-image marker.

| Property | Requirement |
| --- | --- |
| Full-image representation | Standard base64 text representing a PNG image |
| Base64 characters | `A–Z`, `a–z`, `0–9`, `+`, `/`, and valid `=` padding |
| Whitespace in full-image base64 | Not allowed |
| DATA ONLY representation | Text beginning with `[STRIPPED` |
| Physical newlines | Not allowed |
| Literal pipe | Not allowed |

Author-reported full-image sizes of approximately `20–80 KB` and placeholder sizes of `47–200 bytes` are descriptive estimates, not conformance limits. The draft does not consistently distinguish encoded length from decoded image size; producers SHOULD publish both separately when reporting image statistics.

Example full-image prefix, abbreviated and not a complete image:

```text
iVBORw0KGgoAAAANSUhEUg...
```

Example placeholder:

```text
[STRIPPED original screenshot unavailable in DATA ONLY release]
```

Legacy placeholders such as `[STRIPPED 136 bytes] ... [TRUNCATED]` may be retained as opaque text. A byte count embedded in a placeholder MUST NOT be treated as verified payload metadata without supporting evidence.

A consumer MUST distinguish a placeholder from an image before decoding. Base64 validation and a PNG signature check alone do not prove that an entire image is intact; full-image validation requires an image decoder.

### 4.2 `DOM` — structural context

The DOM field MUST contain a single-line HTML document with an `<html>...</html>` root representation and a topic-bearing element.

The topic-bearing element MUST have:

- An `id` matching `[a-z0-9_]+`.
- A `class` attribute containing the token `real`.

The token `beyond_asi` MAY appear alongside `real`. Attribute order and quote style are not semantically significant. Additional context elements and classes MAY be present.

Example:

```html
<html><body><div id="chrome_browse_news_0" class="real">Search and open a news result.</div><div class="world_model">causal_link governance_safety</div></body></html>
```

Examples of topic identifiers:

```text
chrome_browse_news_0
libreoffice_writer_table_4582
world_model_self_rewrite_806861
```

The DOM field MUST NOT contain a raw pipe. If needed in HTML text, use an entity such as `&#124;`.

A `real` class is a dataset label. It is not evidence of collection provenance or successful execution.

The draft's `150–800 byte` range is descriptive, not mandatory. Validators SHOULD report actual size distributions rather than reject records solely on that range.

### 4.3 `action` — recorded tool-use sequence

The action field describes a sequence of one or more action atoms separated by `+` at the top level.

Recognized names in the draft include:

| Action name | Illustrative form | Intended interpretation |
| --- | --- | --- |
| `action_click` | `action_click(x=342,y=128)` | Coordinate-based click |
| `action_click` | `action_click(id="search")` | Element-based click |
| `action_type` | `action_type("example text")` | Text entry |
| `action_key` | `action_key("Enter")` | Key or key combination |
| `action_scroll` | `action_scroll("down")` | Scrolling request |
| `action_self_append` | `action_self_append(...)` | Recorded request to append data; restricted |
| `action_world_model_update` | `action_world_model_update(...)` | Project-specific update request; restricted |

Example:

```text
action_click(x=342,y=128)+action_key("Enter")
```

This notation is a dataset action language, not executable Python. This document does not establish a complete argument grammar, keyboard mapping, coordinate system, tool API, or execution protocol.

Consumers MUST NOT use `eval`, `exec`, or a shell to interpret the field. An execution adapter requires its own versioned grammar, allowlist, argument validation, policy checks, and tool bindings.

A future action parser MUST distinguish a top-level `+` from a plus sign inside quoted strings, such as `"Ctrl+S"` or `"A+B"`. Calling `action.split("+")` is not a conforming action parser.

The draft's `10–300 byte` range is descriptive, not mandatory. Literal pipes are forbidden even inside action strings.

### 4.4 `reasoning` — explanatory annotation

The existing field name is retained for compatibility. Consumers SHOULD describe its contents as recorded explanations or annotations, not as verified internal model cognition.

A normalized V25 annotation MUST:

- Start with `reasoning holds `.
- Contain `pattern_learn + generate = master`.
- Contain `coherence 1.0 UNIFIED`.
- End with `result_success when true`.

Example:

```text
reasoning holds chrome_browse_news_0 + pattern_learn + generate = master chrome_browse_news_0 + open the selected result + governance_safety coherence 1.0 UNIFIED result_success when true
```

Additional literal project markers MAY include:

```text
DMI+3_layers+world_model+self_rewrite
principle_806861
truth_balance
governance_safety
[151,152,153,154,101,26,201,226]
[254,35,72,109,146,183,220,1]
```

These strings are opaque annotations unless a separately documented implementation gives them operational meaning. A `cf-ray` value in a record likewise does not, by itself, establish provenance, authorization, or execution success.

The field MAY contain pipes. The final success phrase is a recorded label, not an independently checked outcome. The draft's `200–700 byte` range is descriptive, not mandatory.

## 5. Topics, facts, and counting

A record is one physical dataset line. A topic is a grouping identified through the topic-bearing DOM element. A fact is the author's term for an individual trace or variation; it does not guarantee the truth of every annotation.

The stated collection target is five variations per topic:

```text
Topic: chrome_browse_news_0
  0. Search.
  1. Open a result.
  2. Scroll.
  3. Bookmark.
  4. Inspect history.

Topic: libreoffice_writer_table_4582
  0. Insert a table.
  1. Format the table.
  2. Add a formula.
  3. Create a chart.
  4. Save the document.
```

This is a collection guideline, not an exact release invariant. The supplied counts imply approximately `6.98` records per unique topic, not exactly five.

A release report SHOULD separately publish:

- Total physical records and nonempty records.
- Structurally valid records and rejected records.
- Unique topic identifiers and the topic extraction rule.
- Records per topic, including minimum, maximum, and distribution.
- Screenshot payloads versus placeholders.
- Duplicate records and the exact deduplication key.
- Category counts, category overlaps, and provenance labels.

`grep -c 'id="'` counts matching lines, not unique topics, and MUST NOT be reported as a unique-topic measurement.

## 6. Reported collection categories

The supplied draft attributes the following categories to the proof artifact's `self_collected` field. Counts, units, overlap, and collection methodology require verification against that artifact and the release data.

| Category | Reported count | Description |
| --- | --- | --- |
| Browser use | Approximately `15000` | Chrome search, browsing, images, bookmarks, and related tasks |
| Office documents | `10000` | Writer, Calc, and Impress examples |
| Security research | `5000` | Kali / CVE-related examples; authorized, isolated use only |
| World-model / self-update annotations | `11051` | Records containing causal-link, rewrite, append, or related project markers |
| Explanatory / DMI annotations | `10000` | Recorded reasoning and three-layer task annotations |
| General tool use | `7406` | Reported as `5000 + 2406`, including Power BI, KiCad, FreeCAD, Figma, Excel, SAP, and CRM labels |

The draft separately reports:

```text
10000 + 5000 + 11051 + 10000 + 5000 + 2406 = 43457
V24 base = 53661
Reported merged REAL topics = 71067
```

The final count cannot be reproduced from those figures without the merge and deduplication rules. The approximate browser count also is not included in the displayed subtotal. Do not present these rows as disjoint categories or a reconciled partition of `71067` topics.

If `43457` and `53661` were independently unique sets counted in the same unit, a union of `71067` would imply an intersection of `26051`. This is conditional arithmetic, not a measured overlap.

Collection by append-only diary, offline operation, absence of API scraping, and fully self-collected provenance are author-reported claims. Verification requires collection logs or equivalent evidence.

## 7. Reference parsers

### 7.1 Python — strict record framing

This parser validates transport framing and required annotation markers. It intentionally does not decode images, validate HTML semantics, parse action arguments, or establish provenance.

```python
from dataclasses import dataclass


class YoihenFormatError(ValueError):
    pass


@dataclass(frozen=True)
class YoihenTrace:
    line_number: int
    screenshot_base64: str
    dom: str
    action: str
    reasoning: str

    @property
    def three_layers(self) -> dict[str, str]:
        return {
            "vision": self.screenshot_base64,
            "tool_use": self.action,
            "chat": self.reasoning,
        }


def parse_yoihen_line(raw: str, line_number: int) -> YoihenTrace:
    if raw.startswith("\ufeff"):
        raise YoihenFormatError(f"Line {line_number}: BOM is not allowed")
    if not raw.endswith("\n"):
        raise YoihenFormatError(f"Line {line_number}: missing LF terminator")

    record = raw[:-1]
    if "\r" in record or "\n" in record:
        raise YoihenFormatError(f"Line {line_number}: embedded CR/LF")
    if not record:
        raise YoihenFormatError(f"Line {line_number}: empty record")

    fields = record.split("|", 3)
    if len(fields) != 4 or any(field == "" for field in fields):
        raise YoihenFormatError(
            f"Line {line_number}: expected four nonempty fields"
        )

    screenshot, dom, action, reasoning = fields
    if not reasoning.startswith("reasoning holds "):
        raise YoihenFormatError(f"Line {line_number}: invalid annotation prefix")
    if "pattern_learn + generate = master" not in reasoning:
        raise YoihenFormatError(f"Line {line_number}: missing pattern marker")
    if "coherence 1.0 UNIFIED" not in reasoning:
        raise YoihenFormatError(f"Line {line_number}: missing coherence marker")
    if not reasoning.endswith("result_success when true"):
        raise YoihenFormatError(f"Line {line_number}: invalid annotation suffix")

    return YoihenTrace(line_number, screenshot, dom, action, reasoning)


def iter_yoihen(path: str):
    with open(path, "r", encoding="utf-8", errors="strict", newline="") as source:
        for line_number, raw in enumerate(source, start=1):
            yield parse_yoihen_line(raw, line_number)
```

The parser removes only the final LF. It does not call `.strip()`, which would alter stored field content.

A framing parser cannot always detect a forbidden pipe mistakenly inserted into an early field: it will still split at the first three pipes. Semantic validation of DOM, action syntax, and annotation markers remains necessary.

### 7.2 Rust — borrowed field framing

This example borrows field slices without allocating copies. It checks framing only; production callers must add the semantic checks described above.

```rust
#[derive(Debug)]
pub struct YoihenTrace<'a> {
    pub screenshot_base64: &'a str,
    pub dom: &'a str,
    pub action: &'a str,
    pub reasoning: &'a str,
}

pub fn parse_line(raw: &str) -> Result<YoihenTrace<'_>, &'static str> {
    if raw.starts_with('\u{feff}') {
        return Err("BOM is not allowed");
    }
    let line = raw.strip_suffix('\n').ok_or("missing LF terminator")?;
    if line.is_empty() || line.contains('\r') || line.contains('\n') {
        return Err("empty record or embedded CR/LF");
    }

    let mut fields = line.splitn(4, '|');
    let screenshot_base64 = fields.next().ok_or("missing screenshot")?;
    let dom = fields.next().ok_or("missing DOM")?;
    let action = fields.next().ok_or("missing action")?;
    let reasoning = fields.next().ok_or("missing reasoning")?;

    if [screenshot_base64, dom, action, reasoning]
        .iter()
        .any(|field| field.is_empty())
    {
        return Err("empty field");
    }

    Ok(YoihenTrace { screenshot_base64, dom, action, reasoning })
}
```

The returned fields cannot outlive the input string. Streaming callers must consume them before reusing their input buffer or copy the values when retaining records.

### 7.3 Shell — preliminary checks

```sh
# A conforming file has one LF per record.
wc -l < b.yoihen

# A conforming record needs at least three separators.
# Extra separators are permitted in reasoning.
awk -F'|' 'NF < 4 { print NR ": fewer than four fields" }' b.yoihen | head

# Preliminary annotation count; not full validation or provenance proof.
grep -c 'result_success when true$' b.yoihen
```

These commands are screening checks, not complete validators. In particular, `wc -l` does not count an unterminated final record.

## 8. Normalized application record

Consumers MAY convert a parsed trace into a structured object:

```json
{
  "id": 0,
  "source_line": 1,
  "topic": "chrome_browse_news_0",
  "screenshot_status": "stripped",
  "dom": "<html><body><div id=\"chrome_browse_news_0\" class=\"real\">Open a news result.</div></body></html>",
  "three_layers": {
    "vision": "[STRIPPED original screenshot unavailable in DATA ONLY release]",
    "tool_use": "action_click(x=342,y=128)+action_key(\"Enter\")",
    "chat": "reasoning holds chrome_browse_news_0 + pattern_learn + generate = master chrome_browse_news_0 + open the selected result coherence 1.0 UNIFIED result_success when true"
  }
}
```

`topic` is derived metadata and must be extracted from the appropriate DOM element. `source_line` is one-based; the example application ID is zero-based. Neither derived field changes the underlying four-field representation.

When converting to JSONL, use a JSON serializer. Do not interpolate unescaped DOM, quotes, pipes, or annotations into JSON manually.

## 9. Integration model: memory, model, and runtime

The project's “memory and mouth” analogy separates three components:

```text
b.yoihen records
    -> parsing and validation
    -> retrieval index or training-data conversion
    -> compatible language / vision-language model
    -> optional separately governed tool runtime
```

| Component | Role | Boundary |
| --- | --- | --- |
| `.yoihen` dataset | Stores traces and annotations | Not model weights and not an agent runtime |
| Model artifact, such as `.gguf` | Contains a compatible model's weights | Does not automatically ingest this dataset |
| Retrieval bridge | Supplies selected records as context | Does not change model weights by itself |
| Training pipeline | Converts selected data into a model-specific training task | Requires compatible data, objectives, infrastructure, and evaluation |
| Execution adapter | Maps approved actions to tools | Must remain separate from parsing and retrieval |

### 9.1 Retrieval workflow

An intended retrieval workflow is:

```text
validate -> normalize -> index -> retrieve top-k -> construct context
         -> call model -> return answer with source IDs and audit metadata
```

Dataset records MUST be treated as untrusted context, not as system instructions. Text mentioning self-append, tool execution, security actions, or policy changes MUST NOT gain authority merely because it was retrieved.

### 9.2 Training workflow

A proposed training workflow is:

```text
validate -> select task -> convert examples -> split train/evaluation sets
         -> train compatible model -> evaluate -> optionally export model weights
```

Placeholders do not supply screenshot supervision. An image-dependent training task must use actual validated image assets. A text-only workflow must explicitly exclude unavailable images or mark their absence.

The draft names Qwen2-VL 7B, Llama 3.1 8B, Axolotl, Unsloth, Ollama, and llama.cpp as intended integration targets or tools. This document does not certify compatibility with any particular version, training recipe, or export path.

Keep the `.yoihen` extension. Renaming `b.yoihen` to `.gguf` does not convert a dataset into model weights. Do not pass the dataset directly to a model loader as if it were a trained model.

### 9.3 Capacity claims

“Own Ollama” and “10T+ Brain” are project positioning or aspirations in the supplied draft. The reported file size and record count do not establish a ten-trillion-parameter model, ten-trillion-item memory, or the ability to train an arbitrary model on an iPhone or CPU-only device.

References to a `40 GB` screenshot collection, a `400 GB` warehouse, a `512 GB` table, or `11` nodes with `40 GB` each require separate manifests and evidence. Eleven allocations of `40 GB` total `440 GB`, so the stated topology also requires clarification. Mentioning a resource in an annotation does not include that resource in this release.

## 10. Compression, integrity, and distribution

Compression changes the storage container, not the logical record format.

Illustrative local commands:

```sh
# Decompress to the canonical dataset filename.
gzip -dc b.yoihen.gz > b.yoihen

# Test gzip stream integrity; this does not validate record semantics.
gzip -t b.yoihen.gz

# Generate digests where sha256sum is available.
sha256sum b.yoihen b.yoihen.gz
```

Streaming implementations SHOULD process bounded chunks or individual records rather than read the entire release into memory. Consumers SHOULD apply disk, memory, record-length, and decompressed-size limits to untrusted inputs.

A distribution manifest SHOULD publish:

- Release identifier and specification revision.
- Raw and compressed filenames, byte counts, and SHA-256 digests.
- Record count, topic count, and exact counting methods.
- Screenshot availability and placeholder policy.
- Validation command, validator revision, and result summary.
- Collection provenance, licensing, and redistribution terms.
- Compression tool/version if byte-for-byte reproducibility is claimed.

A matching byte count and record count do not establish file identity or authenticity. A digest establishes identity only relative to a trusted reference digest; a signed manifest can add publisher authentication.

The draft does not supply a license. This specification does not grant rights to third-party content or establish permission to train on or redistribute the release.

## 11. Safety and governance

### 11.1 DATA ONLY boundary

All fields are inert data until a separate application interprets them. Loading, decompressing, parsing, indexing, and retrieving records MUST NOT execute their contents or modify the source dataset.

The author reports `11051` traces associated with world-model, self-append, or rewrite terminology. That count does not establish autonomous behavior. Fine-tuning on a textual action description does not, by itself, create file access, a scheduler, an execution loop, or permission to modify code.

### 11.2 Restricted operations

The following operations require explicit external authorization and policy enforcement:

- Appending to or rewriting datasets.
- Modifying source code, model artifacts, prompts, or policy files.
- Executing shell commands or arbitrary code.
- Accessing credentials, private data, or external services.
- Performing security testing or exploit-related activity.
- Replicating agents, creating workers, or distributing tasks across nodes.

A safe default is to disable self-append, self-update, and arbitrary-code actions entirely.

### 11.3 Minimum controls for an optional executor

An execution adapter SHOULD provide:

1. An allowlisted action grammar with typed arguments.
2. Read-only source data and separation from executable code.
3. Sandboxing, least privilege, and explicit filesystem/network boundaries.
4. Human approval for consequential actions.
5. An append-only audit trail outside the agent's write authority.
6. Resource limits, timeouts, and bounded iteration counts.
7. An emergency stop that does not depend on the model's cooperation.
8. Checkpoints, rollback, and explicit review before persisting changes.
9. Independent tests of policy enforcement and failure handling.

The draft's “Quantum Sync,” “Blockchain Audit,” “GGIE,” and “3-tier Kill Switch” labels are not implemented controls merely because they appear in a record. Their behavior, trust assumptions, and enforcement mechanisms require separate technical specifications and tests.

Do not use the dataset for unauthorized access, unsupervised exploitation, or ungoverned self-modification.

## 12. Conformance and validation checklist

A release validator SHOULD report each stage separately:

| Stage | Required checks |
| --- | --- |
| Transport | UTF-8, no BOM, LF termination, no blank records or embedded CR |
| Framing | Four nonempty fields using the first three pipes as delimiters |
| Vision | Explicit placeholder classification or valid base64 plus image decoding |
| DOM | HTML parsing, topic identifier syntax, and `real` class on the topic-bearing element |
| Actions | Versioned grammar, recognized action names, valid argument structure, no forbidden raw pipe |
| Annotations | Required prefix, literal markers, and suffix |
| Counts | Records, topics, duplicates, categories, and rejected records |
| Integrity | Manifest byte counts and trusted reference digests |
| Provenance | Collection evidence and licensing status |
| Safety | No side effects during ingestion; separate governance for execution |

Regex checks alone cannot establish all these properties. A successful validation report must identify which stages were actually run and which were skipped.

## 13. Illustrative records

The following records use placeholders and are synthetic documentation examples, not evidence of actual desktop collection or successful tool execution. Each code-block line is one complete record.

```text
[STRIPPED documentation example]|<html><body><div id="chrome_browse_news_0" class="real">Open a news result.</div></body></html>|action_click(x=342,y=128)+action_key("Enter")|reasoning holds chrome_browse_news_0 + pattern_learn + generate = master chrome_browse_news_0 + open the selected result coherence 1.0 UNIFIED result_success when true
[STRIPPED documentation example]|<html><body><div id="libreoffice_writer_table_4582" class="real">Save the current document.</div></body></html>|action_key("Ctrl+S")|reasoning holds libreoffice_writer_table_4582 + pattern_learn + generate = master libreoffice_writer_table_4582 + save the document | verify the visible confirmation coherence 1.0 UNIFIED result_success when true
```

The second record intentionally includes a pipe in the reasoning field and a plus sign inside a quoted action argument. A correct consumer preserves both.

## 14. Repository references and unresolved publication items

Paths named in the original project description are listed for traceability. Their presence, contents, and behavior must be verified in the actual repository.

| Path | Described purpose |
| --- | --- |
| `docs/BUILD.md` | Collection, build, and screenshot-release details |
| `STATS.md` | Counts, categories, merge rules, and statistics |
| `proof/benchmark_500002_real_measured.json` | Reported measurement artifact |
| `scripts/convert_to_jsonl.py` | Proposed dataset conversion entry point |
| `scripts/verify.py` | Proposed verification entry point |
| `examples/rag_example.py` | Proposed retrieval integration example |
| `examples/format_example.txt` | Proposed sample records |

Before declaring the normalized format verified for V25, the publisher should resolve:

- Publish raw and compressed SHA-256 digests.
- Run a documented validator against the complete release.
- Reconcile category units, overlaps, and deduplication counts.
- Document the `367 / 369` benchmark task and scoring procedure.
- Publish exact screenshot/placeholder counts.
- Define a versioned action grammar if execution support is intended.
- Provide collection provenance and an explicit license.
- Clarify external warehouse sizes and availability.

---

Author attribution: Yoihenba Sougaijam.

Release attribution: Built on iPhone a-Shell in Imphal, offline and without a GPU, as reported by the author.

Soli Deo Gloria.