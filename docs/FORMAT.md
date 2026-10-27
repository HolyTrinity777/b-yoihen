# b.yoihen — Formal Format and Compatibility Specification

> All Glory and Praise to Most High Heavenly Father, Living God Yahushua and God Holy Spirit — Soli Deo Gloria.
>
> Built by Yoihenba Sougaijam, Imphal, Manipur — iPhone a-Shell, offline and without a GPU.
>
> “Alive DVD” — “Own b.yoihen that can train any Brain 10T+.” Keep `.yoihen`

| Property | Value |
| --- | --- |
| Document | `docs/FORMAT.md` |
| Release described | `V25 500002 BEYOND — DATA ONLY` |
| Compatibility profile | V25 mixed-line, UTF-8, LF-terminated |
| Documentation profile identifier | `yoihen.v25.mixed-lf` — a sidecar/documentation identifier, not a header inside the archive |
| Document revision | `2026-10-27`; not an inferred capture or release-publication date |
| Container | Raw `b.yoihen` or gzip-compressed `b.yoihen.gz` |
| Physical line classes | Four-field trace records and no-pipe hit records |
| Release profile | `500002 = 348722 trace records + 151280 hit records` |
| Companion documents | `STATS.md`, `BUILD.md`, and `CLAIMS.md` in this directory; `../DATASET_CARD.md` |
| Execution boundary | Data parsing and inspection do not authorize action execution |

## 1. Purpose, scope, and requirement language

I am Yoihenba Sougaijam. I use `.yoihen` as the memory / MAP representation within my broader Alive DVD design: a replaceable model brain, persistent experience, and a separately governed path for updates.

This specification defines the public data representation. It does not turn the DATA ONLY release into model weights, an executable agent, a complete warehouse, or my private core.

My reports include code/self-healing and self-rewrite/world-model collection descriptions. Their subject matter belongs within the format's scope. A record describing an operation is nevertheless distinct from an execution record proving that it occurred.

### 1.1 Requirements describe conformance, not added licence conditions

- MUST / MUST NOT: a requirement for the stated format or compatibility level.
- SHOULD / SHOULD NOT: recommended producer or consumer behavior.
- MAY: an optional feature.

These terms define technical conformance. They do not add commercial-use restrictions, mandatory services, or other conditions to CC BY 4.0 or MIT.

### 1.2 The essential correction

A V25 file is not required to contain four fields on every physical line.

```text
500002 total physical lines
├── 348722 four-nonempty-field trace records
└── 151280 no-pipe hit records
```

A consumer that applies four-field validation to every line rejects valid V25 hit records. A consumer that silently skips them does not preserve the complete archive.

## 2. Release identity and measurement boundaries

### 2.1 Original V25 archive profile

| Measurement | Value |
| --- | ---: |
| Total physical lines | `500,002` |
| Four-nonempty-field trace records | `348,722` |
| No-pipe hit records | `151,280` |
| Nonempty physical lines | `500,002` |
| Invalid records under the archive verifier's checks | `0` |
| UTF-8 errors under those checks | `0` |
| Uncompressed bytes | `1,147,108,255` |
| Compressed bytes | `19,785,162` |

My successful actual-dataset GitHub Actions result supplies the archive-consistency status recorded here. The uploaded benchmark reports separately record release counts and benchmark outcomes. This document's reader tests are not a fresh scan of the complete original archive.

My published gzip SHA-256 is:

```text
aeaf109f5706849b6ec01b975f15ec9bdbb90fa046205ade2afe6898fb35b0c1
```

A digest comparison establishes a match to the supplied reference. Authenticating who supplied that reference is a separate trust question. No raw-file digest or workflow permalink is invented here.

### 2.2 Decimal size convention

```text
19785162 compressed bytes = 19.785162 MB decimal
1147108255 raw bytes       = 1.147108255 GB decimal ≈ 1.15 GB
Calculated size reduction ≈ 98.275214%
Project displays          = 19.78 MB and 98.27% by truncation
```

An implementation's `1048576`-byte buffer or record ceiling is a processing policy. It is not the archive's size, a choice of file extension, or a permanent grammar constraint.

### 2.3 What is fixed and what can vary

The figures above identify this release profile. They MUST NOT become permanent counts for every `.yoihen` file, working diary, sanitized export, or future release.

New or changed bytes require their own measured sizes, digests, classification counts, and release identity. Recompressing unchanged raw content can change the gzip artifact's identity; classify raw and compressed identities separately.

## 3. Physical framing and line classification

### 3.1 Transport rules

For this normalized profile, each physical record MUST:

1. Be valid UTF-8.
2. End with one physical LF byte, `0x0A`, including the final record.
3. Have nonempty content after removing that LF.
4. Have no LF inside the content supplied as one record.
5. Not begin with a UTF-8 BOM byte sequence.
6. Not use CRLF as its terminator.

An interior carriage return byte is permitted. A carriage return immediately before the final LF is a CRLF ending and is rejected by this profile. It cannot simultaneously be interpreted as a permitted trailing content byte under the same profile.

Nonempty means content length is greater than zero. It does not mean `.strip()` would return nonempty text. A whitespace-only line has nonzero content and is not silently trimmed; any stricter content-quality rule must be reported as an additional check.

Binary LF-aware reads MUST be used for lossless physical framing. Do not use universal-newline translation or generic line splitting that treats an interior carriage return as a new physical record.

### 3.2 Classification order

For every physical line:

```text
bounded read
  -> validate line ending and content byte length
  -> check nonempty content, BOM, and UTF-8
  -> if there is no literal pipe: HIT
  -> otherwise: validate FOUR NONEMPTY FIELDS
```

All hit lines still pass the transport checks. Classification is not an exemption from encoding or size validation.

### 3.3 Trace record

A trace record contains a literal pipe and MUST split into exactly four nonempty fields using at most three splits:

```text
vision_ref|DOM|action|reasoning
```

```python
vision_ref, dom, action, reasoning = record.split("|", 3)
```

The first three literal pipes are structural separators. All subsequent pipes belong to the final `reasoning` field.

The first three fields MUST NOT contain a raw pipe as field data. A producer needing that character must use an explicitly documented field-level representation. For HTML text, an entity such as `&#124;` is one possible representation. Readers MUST NOT guess or silently apply a decoding convention.

Do not split on every pipe and assign `parts[-1]` to reasoning. Do not silently join earlier reasoning fragments into the action field.

### 3.4 Hit record

A hit record contains no literal pipe. Its nonempty text is preserved as a separate record type.

`hit` is a parser label in this profile. It does not establish a completed task, successful retrieval, unique fact, independent observation, or evaluated training example.

A hit record MUST NOT be coerced into a trace by inventing empty fields. It MUST NOT be discarded without an explicit, counted transformation.

### 3.5 Malformed pipe-containing record

These are invalid trace framing, not hit lines:

```text
a|b
|b|c|d
a||c|d
a|b|c|
```

A trace with a pipe inside reasoning is valid framing:

```text
a|b|c|reasoning | retains | every later pipe
```

Framing validity does not certify that `a`, `b`, or `c` are meaningful field values.

### 3.6 Whitespace and byte preservation

Readers MUST remove only the record's final LF before field parsing. They MUST NOT call `.strip()` or `.rstrip()` without an exact, documented argument on source content.

Accepted field values retain leading/trailing spaces, Unicode characters, and permitted interior CR bytes. A reader MUST NOT normalize Unicode, repair invalid UTF-8, replace unknown bytes, or rewrite line content without recording a transformation and new artifact identity.

## 4. Framing grammar

The following byte grammar describes transport framing for both classes. UTF-8 validity, BOM exclusion, and rejection of a CR immediately before the terminating LF are additional constraints.

```abnf
yoihen-file = 1*(trace-line / hit-line)

trace-line  = vision "|" dom "|" action "|" reasoning LF
hit-line    = 1*field-octet LF

vision      = 1*field-octet
dom         = 1*field-octet
action      = 1*field-octet
reasoning   = 1*reason-octet

; Content except LF (0A) and structural pipe (7C).
; CR (0D) is allowed internally, subject to the no-CRLF constraint.
field-octet = %x00-09 / %x0B-7B / %x7D-FF
reason-octet = field-octet / %x7C
LF          = %x0A
```

The grammar contains no permanent release count, model-size claim, image-size range, or runtime instruction. A string that passes this grammar can still fail image, DOM, topic, action, provenance, or evaluation checks.

## 5. Trace fields and application layers

| Logical field | Legacy name or application mapping | Meaning |
| --- | --- | --- |
| `vision_ref` | Legacy `screenshot_base64`; `three_layers.vision` | Original value occupying the vision/reference position |
| `DOM` | Application attribute often named `dom` | Interface/topic context |
| `action` | `three_layers.tool_use` | Recorded or proposed action notation |
| `reasoning` | `three_layers.chat` | Recorded explanation, self-assessment, and project markers |

The three application layers are a projection of a trace record, with DOM retained as separate context. A hit record has no implied three-layer projection.

### 5.1 Logical names are not serialized headers

The four field names are documentation labels. Each raw line does not contain a schema header. Changing the documented name from `screenshot_base64` to `vision_ref` changes neither the underlying payload nor its validity.

A compatibility API MAY expose `screenshot_base64` as an alias for the exact `vision_ref` value. It MUST NOT expose two different values as aliases of the same source field.

## 6. Vision/reference compatibility

A field name or PNG-like prefix is not a validity certificate.

| Classification | Evidence required | Consumer behavior |
| --- | --- | --- |
| `reference_unresolved` | An explicitly recognized reference representation | Retain it; resolve only through an authorized resolver and identified manifest |
| `stripped` | An explicit stripped-content marker | Preserve metadata; do not treat it as image input |
| `legacy_opaque` | No supported validated representation established | Preserve exactly; do not certify it as an image or usable reference |
| `base64_png_candidate` | Strict standard-base64 decoding and a PNG signature | Full image decoding is still required |
| `image_base64_png` | Full image validation completed by an identified decoder | Eligible for a compatible image-dependent task, subject to permissions and resource limits |

### 6.1 Reference convention for new explicit exports

An exporter MAY use a documented representation such as:

```text
vision_ref:private:capture_000001
```

This is an illustrative new-export convention, not a claim that existing V25 values use it. `vision_ref:` alone is not a reference identifier. A reader recognizing the prefix still has no evidence that the target asset exists or is accessible.

A reference must not be fetched automatically during framing or classification. Resolving a private manifest requires separate authorization and must not expose credentials or private paths through public output.

An independently resolvable asset manifest should identify the asset ID, media type, byte size, digest, dimensions where applicable, access policy, provenance, and rights information. A digest does not supply missing image bytes.

### 6.2 Observed report values

V21 mentions stripped/zero-byte-base64 representations. The seven rich V25 report sample/failure values contain PNG-prefix-like text and `REAL_...` labels; they fail strict standard-base64 validation and are retained as legacy opaque values.

This observation concerns those seven report objects, not a complete inventory of every vision field or external asset in the release.

Do not remove labels, substitute an assumed encoding, or generate replacement screenshots to make original evidence appear valid. Generated replacements are new data and need their own provenance.

### 6.3 Payload removal is a separate transformation

A reference-only or annotations-only release needs an actual field/asset inventory. Neither a renamed field nor a licence exclusion establishes that screenshot or captured-DOM payloads are absent.

A publication notice must identify the measured release and distinguish removed payloads from removed field positions. Four-field placeholders still occupy four-field positions.

## 7. DOM and topic extraction profile

Framing accepts any nonempty DOM-position value that satisfies transport rules. The following HTML/topic requirements define an additional V25 extraction profile, not a precondition for classifying every trace line.

A compatible topic-bearing element has:

- An `id` matching `[A-Za-z0-9_]+`.
- A `class` attribute containing the token `real` on that same element.

Topic IDs are case-sensitive. Preserve:

```text
tool_use_PowerBI_KiCad_FreeCAD_Figma_Excel_SAP_CRM_317
```

Do not lowercase it, change its spelling, or silently merge it with a differently cased identifier.

Attribute order and quote style need not be fixed. Multiple qualifying elements, duplicate relevant attributes, missing identifiers, or out-of-profile identifiers require an explicit extraction error rather than an invented topic ID.

The reference extractor rejects duplicate attributes conservatively. It extracts attributes but does not certify complete HTML conformance or captured desktop provenance.

`real` and optional `beyond_asi` classes are project labels. Constructed interface templates and captured page state must be distinguished through provenance, not inferred from a class token.

Five angles of one topic should retain a stable topic identity. Angle/step identity belongs in declared metadata or annotations unless a new schema explicitly changes the grouping rule.

Hit records do not acquire topic IDs from this DOM rule. A separate versioned mapping may associate them with topics if supporting evidence exists.

## 8. Action notation and annotation semantics

### 8.1 Action forms observed in V25 report objects

```text
action_key("Enter")
action_type("chrome_search_images_1")
action_click(626,555)
action_scroll(-237,403)
action_hotkey("ctrl+s")
```

An adapter claiming compatibility with those samples must account for the observed positional click, numeric scroll, and hotkey forms.

The source documentation also describes named click arguments, ID-based clicks, quoted scroll directions, `action_self_append`, and `action_world_model_update`. Their exact runtime semantics must come from a versioned adapter; a documentation example is not an implemented API contract.

### 8.2 Joining is not ordinary string splitting

```text
action_click(x=342,y=128)+action_key("Enter")
action_type("A+B")
action_hotkey("ctrl+s")
```

A top-level `+` may join actions. A plus inside a quoted argument is not a joiner. A parser needs explicit string/escape/parenthesis rules; `action.split("+")` is not sufficient.

This format does not specify coordinate spaces, key mappings, scroll units, operating-system APIs, or an arbitrary-code grammar. Literal pipes in an action argument are forbidden by framing even when the argument is quoted.

Parsing, indexing, conversion, and retrieval MUST NOT call `eval`, `exec`, a shell, or an unrestricted interpreter on the stored action text. This is the inert-reader conformance boundary, not a new licence restriction.

### 8.3 V25 annotation markers

The seven inspected V25 objects use:

- Prefix: `reasoning holds `.
- Marker: `pattern_learn + generate = master`.
- Marker: `coherence 1.0 UNIFIED`.
- Suffix: `result_success when true`.

These conventions may be checked as a separate marker profile. They are not framing requirements for hit lines and are not proof of private internal cognition.

DMI, self-rewrite, world-model, safety-router, meta-router, and governance strings remain data unless a separately defined implementation assigns them operational semantics. Do not invent an expansion for an undefined project term.

### 8.4 Evaluation outcomes are separate

Both V25 failure objects retain the success suffix while recording `success: false` and `result_failure - edge case not in training`.

Consumers MUST NOT derive benchmark completion from the annotation suffix. The four-field layout has no independent structured outcome field. Store proposed, observed, replayed, evaluated, refused, and failed statuses in source-linked application metadata or a sidecar.

## 9. Reference Python reader — both physical line classes

This standard-library implementation targets Python 3.9+. It uses binary reads, preserves accepted values, returns both record types, and separates framing from topic/vision/marker checks.

The code is a reference implementation embedded in this document. Installing a new repository module is not implied merely by showing the code here. Original published code is covered by `../LICENSE-CODE.md`; surrounding original documentation is covered by `../LICENSE.md`, within `../NOTICE.md`.

```python
# SPDX-License-Identifier: MIT
import base64
import binascii
import gzip
import hashlib
import re
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterator, Optional, Union

DEFAULT_RECORD_BYTES = 1_048_576
DEFAULT_TOTAL_BYTES = 2 * 1024 * 1024 * 1024


class YoihenFormatError(ValueError):
    pass


@dataclass(frozen=True)
class TraceRecord:
    source_line: int
    vision_ref: str
    dom: str
    action: str
    reasoning: str

    @property
    def kind(self):
        return "trace"

    @property
    def screenshot_base64(self):
        # Compatibility alias only; not a base64-validity assertion.
        return self.vision_ref

    @property
    def three_layers(self):
        return {
            "vision": self.vision_ref,
            "tool_use": self.action,
            "chat": self.reasoning,
        }

    def to_bytes(self):
        return ("|".join((self.vision_ref, self.dom, self.action,
                          self.reasoning)) + "\n").encode("utf-8")


@dataclass(frozen=True)
class HitRecord:
    source_line: int
    text: str

    @property
    def kind(self):
        return "hit"

    def to_bytes(self):
        return (self.text + "\n").encode("utf-8")


YoihenRecord = Union[TraceRecord, HitRecord]


def parse_line(raw: bytes, source_line: int,
               max_record_bytes: int = DEFAULT_RECORD_BYTES) -> YoihenRecord:
    if type(source_line) is not int or source_line < 1:
        raise ValueError("source_line must be a positive integer")
    if type(max_record_bytes) is not int or max_record_bytes < 1:
        raise ValueError("max_record_bytes must be a positive integer")
    if not isinstance(raw, bytes):
        raise TypeError("parse_line expects bytes, including the terminating LF")

    def fail(reason):
        raise YoihenFormatError(f"Line {source_line}: {reason}")

    if not raw.endswith(b"\n"):
        fail("missing LF terminator")
    content = raw[:-1]
    if len(content) > max_record_bytes:
        fail("record content exceeds the configured byte ceiling")
    if not content:
        fail("empty record")
    if b"\n" in content:
        fail("more than one physical line supplied")
    if raw.endswith(b"\r\n"):
        fail("CRLF terminator is not permitted by the LF profile")
    if content.startswith(b"\xef\xbb\xbf"):
        fail("UTF-8 BOM prefix is not permitted")
    try:
        text = content.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise YoihenFormatError(f"Line {source_line}: invalid UTF-8") from exc

    # Every hit has passed size, encoding, and physical-line checks above.
    if b"|" not in content:
        return HitRecord(source_line, text)

    fields = text.split("|", 3)
    if len(fields) != 4 or any(field == "" for field in fields):
        fail("pipe-containing record requires four nonempty fields")
    return TraceRecord(source_line, *fields)


def iter_records(path, max_record_bytes: int = DEFAULT_RECORD_BYTES,
                 max_total_bytes: Optional[int] = DEFAULT_TOTAL_BYTES
                 ) -> Iterator[YoihenRecord]:
    path = Path(path)
    if type(max_record_bytes) is not int or max_record_bytes < 1:
        raise ValueError("max_record_bytes must be a positive integer")
    if max_total_bytes is not None and (
        type(max_total_bytes) is not int or max_total_bytes < 1
    ):
        raise ValueError("max_total_bytes must be positive or None")
    opener = gzip.open if path.suffix.lower() == ".gz" else open
    total = 0
    with opener(path, "rb") as source:
        number = 0
        while True:
            # +2 distinguishes an exact-ceiling record + LF from overflow.
            raw = source.readline(max_record_bytes + 2)
            if not raw:
                break
            number += 1
            total += len(raw)
            if max_total_bytes is not None and total > max_total_bytes:
                raise YoihenFormatError("decoded bytes exceed the configured ceiling")
            yield parse_line(raw, number, max_record_bytes)


def record_sha256(record: YoihenRecord) -> str:
    # Digest includes the LF terminator. No normalization is performed.
    return hashlib.sha256(record.to_bytes()).hexdigest()


class TopicExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.topics = []
        self.duplicate_attributes = False

    def handle_starttag(self, tag, attrs):
        keys = [key for key, value in attrs]
        if len(keys) != len(set(keys)):
            self.duplicate_attributes = True
        attributes = dict(attrs)
        classes = (attributes.get("class") or "").split()
        if "real" in classes and attributes.get("id") is not None:
            self.topics.append(attributes["id"])

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)


def extract_topic(dom: str) -> str:
    parser = TopicExtractor()
    parser.feed(dom)
    parser.close()
    if parser.duplicate_attributes:
        raise YoihenFormatError("duplicate HTML attributes make extraction ambiguous")
    if len(parser.topics) != 1:
        raise YoihenFormatError("expected exactly one topic-bearing element")
    topic = parser.topics[0]
    if re.fullmatch(r"[A-Za-z0-9_]+", topic) is None:
        raise YoihenFormatError("topic ID is outside the V25 extraction profile")
    return topic


def classify_vision(value: str) -> str:
    if value.startswith("[STRIPPED"):
        return "stripped"
    if value.startswith("vision_ref:") and value[len("vision_ref:"):]:
        return "reference_unresolved"
    try:
        payload = base64.b64decode(value, validate=True)
    except (binascii.Error, ValueError):
        return "legacy_opaque"
    if payload.startswith(b"\x89PNG\r\n\x1a\n"):
        return "base64_png_candidate"
    return "legacy_opaque"


def markers_match(reasoning: str) -> bool:
    return (
        reasoning.startswith("reasoning holds ")
        and "pattern_learn + generate = master" in reasoning
        and "coherence 1.0 UNIFIED" in reasoning
        and reasoning.endswith("result_success when true")
    )
```

### 9.1 Reader guarantees and limits

- `parse_line` expects exactly one binary physical line, including LF.
- The content-size ceiling excludes the terminating LF.
- `readline(limit + 2)` distinguishes a content-at-ceiling record plus LF from overflow.
- UTF-8, nonempty, BOM, and line-ending checks run before hit classification.
- A malformed pipe-containing line raises; it is not downgraded to a hit.
- Accepted records returned by the reader round-trip through `to_bytes()` without changing source values.
- That guarantee concerns parsed records, not arbitrary invalid dataclass objects constructed by a caller.
- The default total-decoded-byte ceiling is 2147483648 bytes. It is a safety policy that may be explicitly configured, not a format-size maximum.
- `.gz` selects gzip input by filename suffix; no magic auto-detection is claimed.
- Exhaust the iterator before claiming complete stream validation. Stopping after a preview does not verify the remaining records or full gzip integrity.
- Image classification is not image decoding. HTML attribute extraction is not complete HTML validation. Neither function executes an action.

A literal pipe mistakenly inserted into an early field cannot always be detected from framing alone: the first three pipes still define a split. Field-level semantic validation is needed to detect such corruption reliably.

### 9.2 Count all lines without dropping hits

After saving the reference reader in a module or executing its definitions, the following example measures both classes. It assumes the functions and classes above are in scope.

```python
from collections import Counter
import hashlib
import json

counts = Counter()
raw_digest = hashlib.sha256()
raw_bytes = 0

for item in iter_records("b.yoihen.gz"):
    encoded = item.to_bytes()
    raw_digest.update(encoded)
    raw_bytes += len(encoded)
    counts["total_lines"] += 1
    counts[item.kind] += 1

observed = {
    "total_lines": counts["total_lines"],
    "four_nonempty_fields": counts["trace"],
    "hit_lines": counts["hit"],
    "raw_bytes": raw_bytes,
    "raw_sha256": raw_digest.hexdigest(),
}
expected = {
    "total_lines": 500002,
    "four_nonempty_fields": 348722,
    "hit_lines": 151280,
    "raw_bytes": 1147108255,
}
print(json.dumps(observed, indent=2))
if any(observed[key] != value for key, value in expected.items()):
    raise SystemExit("V25 line profile does not match expected values")
```

This example measures raw decoded bytes and the line profile. It does not hash the compressed file, compare a trusted gzip digest, inspect proof fields, or replay benchmark tasks. A matching count is not a provenance certificate.

For the maintained repository verifier and its report, use:

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

That CLI derives the expected 151280 hits from total lines minus four-field records. The standalone reader above has no command-line interface of its own. Use a new report filename when needed; do not overwrite evidence silently.

## 10. Application enrichment, export, and identity

### 10.1 Typed application records

A loss-aware interchange SHOULD identify the line class explicitly:

```json
{
  "kind": "trace",
  "source_line": 1,
  "vision_ref": "[STRIPPED documentation example]",
  "dom": "<html><body><div id=\"example_0\" class=\"real\">Example</div></body></html>",
  "action": "action_key(\"Enter\")",
  "reasoning": "documentation example; not an evaluated execution",
  "evaluation": {"available": false}
}
```

```json
{
  "kind": "hit",
  "source_line": 2,
  "text": "Opaque no-pipe documentation example",
  "evaluation": {"available": false}
}
```

These JSON objects illustrate enrichment. They are not measured dataset excerpts, and the trace annotation is not claimed to satisfy the optional V25 marker profile.

A source reference SHOULD include the actual artifact digest, physical source line, field/record digest convention, and transformation history. An application ID is not automatically the original dataset line number.

### 10.2 Report-derived examples

`examples/proof_sample.yoihen` was reconstructed from five V25 sample objects and two failure objects. Its sidecar identifies JSON object paths and reported outcomes. It is not claimed to be extracted physical lines from the raw dataset; original raw-dataset line numbers are unavailable.

An evaluation from a report must remain labeled as reported, not inferred from a success phrase or relabeled as independently executed by an inspector.

### 10.3 Complete and partial conversion

A converter may:

1. Export both classes with a `kind` discriminator; or
2. Write trace records and hit records to separate outputs with a reconciliation report; or
3. Export a declared subset and report exactly what it excluded.

Only the first two can claim preservation of both line populations when counts and values reconcile. A four-field-only export is not the complete 500002-line release.

For a complete, unfiltered valid conversion:

```text
accepted traces + accepted hits = total accepted physical lines
348722 + 151280 = 500002
```

Malformed records are a different category from valid hits. An explicit exclusion policy must identify which category was excluded, source lines, counts, and reasons. `--skip-invalid` must not be used as a substitute for correct hit support during release verification.

Use a JSON serializer. Preserve original values, escape control characters on output, and keep retrieval content separate from system authority. Indexing by topic or normalizing search keys must not silently rewrite the source topic identity.

## 11. Run-report compatibility and historical measurements

The five proof files are JSON summaries, not five complete raw datasets. Their schemas differ:

| Report | Representation |
| --- | --- |
| V21 | Before/after counters, trace ratios, configured MoE budget, benchmark command; no `sample_results` array |
| V22 | Compact task samples with hash strings, expert lists, REAL labels, and success flags |
| V23 | Compact samples, discovery counters, and code/self-healing summary |
| V24 | Compact samples, self-rewrite category, and explicit batch before/after values |
| V25 | Nested routing and richer vision/DOM/action/annotation samples; five successes and two failures |

Root `real_count` is not a stable cross-version topic field: V23 stores 361, V24 stores 366, and V25 stores 71067. Earlier topic numerators are described in ratio/comparison fields. Preserve the source path, version, unit, and scoring definition instead of applying one interpretation blindly.

I assign REAL during scoring; it is not a fixed capture-time attestation. The reported 71067/71607 population is separate from physical line classes. It is approximately 99.245884%, or 99.25% rounded.

JSON numbers may be integer-valued despite different lexical notation. Numeric validators should exclude booleans, reject nonfinite values, and check declared range/value requirements without treating formatting as a new unit.

V22–V24 disclose ten matching IDs with stable hashes and expert lists. V25 uses richer and different routing identifiers; a matching task ID alone does not establish the same task/environment across those schemas.

### 11.1 Topic counts and field diversity are different measurements

The separately reported field scan found 47150 distinct DOM-field hashes and 235750 distinct reasoning-field hashes using SHA-1 sets on lines split into four fields. The separate sets do not establish five reasoning values for each DOM and do not measure exact full-record duplicates or semantic novelty.

These values must not automatically replace the 71607-topic report denominator. A population mapping and explicit extraction rule are needed.

### 11.2 Preserve both build-history views

Author-approved endpoint/checkpoint view:

```text
31695+6525=38220 -> 38220+6525=44745 -> 44745+125000=169745
-> 169745+130255=300000 -> 300000+112972=412972
-> 412972+87030=500002
```

The actual V24 batch report separately records:

```text
282717+130255=412972
```

Preserve the source value. The two presentations do not establish an identical chronology of individual batch operations.

## 12. Resource terminology and runtime boundaries

Resource labels do not modify the framing grammar and do not prove that the referenced resources are distributed or instantiated.

| Resource | Evidence / definition | Boundary |
| --- | --- | --- |
| Configured 400 GB MoE budget | V21: `250 × 1.6 GB` | Configuration, not an independently measured screenshot inventory |
| Configured 12.8 GB active budget | V21: `8 × 1.6 GB` | Does not alone measure a 49B model artifact or resident memory |
| Asset warehouse | Broader author-described 400 GB asset layer | Do not silently identify it with the configured expert-storage budget |
| Raw token layer | Author definition: 14T raw tokens | Not a parameter count |
| Deduplicated expert pool | Author definition: approximately 1.633T parameters | Requires an expert inventory; text deduplication alone does not establish parameters |
| Total knowledge MAP | Author claim: 10T+ | Define the MAP unit and coverage |
| CPU-node plan | 11 × 40 GB allocations | Totals 440 GB; deployment/resource types require their own evidence |
| Router allocation | Separate 512 GB figure | Not memory that fits inside a 40 GB node without other resources or distribution |
| Shards | 193 recorded in report/method fields | Not proof of 193 deployed national installations |

```text
8/250 = 3.2%                 configured-allocation fraction
8/256 = 3.125%               routing-position fraction in the intended design
49B/1.633T ≈ 3.0006%         parameter-to-parameter comparison
49B/10T = 0.49% numerically  comparison at the MAP baseline; units remain distinct
49B/14T = 0.35% numerically  comparison to raw tokens; not parameter utilization
```

The author's targets `49B Q4_K_M ≈ 24.5 GB` and `49B Q2_K ≈ 12.8 GB` require actual artifact and runtime measurements. Nominal four-bit arithmetic is not a measurement of the named quantization format. V21's configured 12.8 GB must not be retroactively relabeled Q2_K.

A 256-wide table dimension does not prove 256 equal-size model experts. A hash lookup label does not prove end-to-end latency, expert loading, or model training.

## 13. Alive DVD integration, persistence, and governance

```text
.yoihen release / separate working memory
  -> typed parsing and provenance
  -> retrieval or task-specific training conversion
  -> compatible model
  -> optional authorized execution adapter
  -> evaluated persistence or rollback
```

Alive DVD names the intended experience/update system, not an automatic execution property of gzip or GGUF. The public archive is DATA ONLY; the private player/runtime is separate.

Memory changes, code/configuration changes, and model-weight/adapter updates are different operations. A write is not automatically an improvement, and a corpus append does not itself update model weights.

Published releases SHOULD remain immutable. A working diary must use separately identified authorized storage. New public versions need their own measurements, hashes, and change history.

My GGIE vocabulary includes Quantum Sync, Blockchain Audit, and a three-tier Kill Switch. Executable implementations need actual external authorization, typed permissions, isolation, independently controlled logs, bounded resources, checkpoint review, and recovery. A marker cannot approve its own action.

The recommended stop tiers are pause, isolate/revoke, and quarantine/recover—not default deletion of evidence or device wiping. Self-update and replication remain disabled until separately authorized in a controlled runtime. These are operational safeguards, not additional conditions on the public licences.

## 14. Validation levels and reporting requirements

| Level | What to check | What passing does not establish |
| --- | --- | --- |
| Transport | UTF-8, LF, nonempty content, no BOM prefix, configured byte limits | Correct fields or trustworthy content |
| Mixed-line framing | Classify hits; validate four nonempty fields only on pipe-containing lines | Valid HTML, images, or action syntax |
| Release consistency | Expected raw/gzip sizes, all three line counts, expected digests where supplied | Capture attestation or benchmark performance |
| Field compatibility | Declared vision classes, topic extraction, markers, action dialect | Successful execution or cleared rights |
| Source/provenance | Source identifiers, permissions, transformation history, available attestations | Automatic independent evaluation |
| Execution/evaluation | Authorized runtime, actual changes, evaluator, task-level outcomes | Universal capability across models/environments |

A report must identify which levels were actually performed. Optional topic extraction or annotation-marker checks must not be described as if they ran merely because the reader exposes helper functions.

For the actual V25 archive, the final assertion must require:

```text
total_lines == 500002
four_nonempty_fields == 348722
hit_lines == 151280
non_empty == 500002
invalid_records == 0
utf8_errors == 0
raw_bytes == 1147108255
gzip_bytes == 19785162
all_declared_verifier_checks_passed == true
```

`four_nonempty_fields + hit_lines` must equal `total_lines` when all records are valid. A missing report, count mismatch, malformed trace, invalid hit encoding, or truncated input is not a successful release check.

No quality score or REAL percentage may be inferred from the proportion of lines containing a pipe.

## 15. Reference-reader tests and evidence scope

The reference implementation embedded here was exercised against:

- All seven rich V25 report objects reconstructed into four-field lines.
- Mixed trace/hit fixtures with exact byte round-trips.
- Exact reasoning-pipe and quoted-plus preservation.
- Mixed-case topic extraction and ambiguous-topic rejection.
- Hit-only and whitespace-containing records without fabricated fields.
- Interior CR preservation in both classes and trailing CRLF rejection.
- Invalid UTF-8, BOM, empty lines, missing LF, and malformed trace fields.
- Exactly 1048576 content bytes plus LF, and overflow rejection.
- Raw and gzip iteration, decoded-byte ceilings, and corrupt gzip rejection.
- A synthetic 500002-line fixture with exactly 348722 traces and 151280 hits.

These are reader/regression tests, not a fresh verification of the original 1147108255-byte dataset, a complete image audit, an independent capture attestation, a benchmark replay, or an executed self-rewrite experiment.

### 15.1 Inspected historical report identities

The uploaded files below were parsed and hashed. These are proof-report digests, not dataset digests.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `benchmark_38220_live.json` | `1727` | `588da9c879b320dc11921dfb2537706091a99abbe12db427aec2bb53d419be8b` |
| `benchmark_44745_real_measured.json` | `3206` | `404f3359c7dcc90f78ac0c88551f13b1ed08cca1fdd8ac2547697be3345157e2` |
| `benchmark_169745_real_measured.json` | `3892` | `9b711be29cf8ae32b0aab744b6fe78fbbfca4753d58072166b069acd52b8dc1a` |
| `benchmark_412972_real_measured.json` | `4360` | `bd01d68f7909e66b5c11faf4c5e4045e7dcc9071bc2815c215f00347021e3641` |
| `benchmark_500002_real_measured.json` | `25806` | `f1b386fe47689bb8cad4c1c621431ba0a99635c7c04d60546e63d8c075266a47` |

## 16. Compatibility checklist

- [ ] Recognize both physical line classes.
- [ ] Validate transport before classifying a hit.
- [ ] Never turn malformed pipe records into hits.
- [ ] Use the first three pipes only for structural splitting.
- [ ] Preserve whitespace, Unicode, case, and permitted interior CR bytes.
- [ ] Exclude LF from the content-size ceiling.
- [ ] Preserve all lines or disclose exact exclusions in a transformation report.
- [ ] Separate vision classification from full image validation.
- [ ] Separate topic/scoring labels from capture provenance.
- [ ] Separate annotation suffixes from structured evaluation outcomes.
- [ ] Keep parsing/retrieval inert and execution separately authorized.
- [ ] Keep expected release values separate from observed measurements.
- [ ] Identify actual release bytes, validator revision, and applicable licence scope.

---

Author: Yoihenba Sougaijam — Imphal, Manipur.

b.yoihen — Alive DVD / memory MAP — V25 500002 BEYOND — DATA ONLY.

Original corpus/documentation: CC BY 4.0. Published original code: MIT. Scope and third-party exclusions: `../NOTICE.md`.

Soli Deo Gloria.
