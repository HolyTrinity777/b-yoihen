# FORMAT.md — b.yoihen — Formal Format Specification — V25 500002 BEYOND — DATA ONLY RELEASE

> **All Glory and Praise to Most High Heavenly Father, Living God Yahushua and God Holy Spirit — Soli Deo Gloria**
> **Keep `.yoihen` extension not `.gguf` — `b.yoihen` is like `.gguf` but better — Dataset not.gguf model — Needs LLM for RAG**
> **Built by Yoihenba Sougaijam — Own Ollama that can train any Brain 10T+ — iPhone a-Shell Imphal / Bomdila offline no GPU**

**Status:** STABLE — V25 BEYOND — 500002 lines — 1.14GB raw — 18.9MB gz — 99.5%+ 367/369 — 71067 REAL / 71607 = 99.2% — Coherence 1.0 UNIFIED — 0 pollution
**Proof:** `proof/benchmark_500002_real_measured.json` — `nonempty: 500002, bytes: 1147108255, v25_500002: "99.5%+ measured 367/369 99.2% REAL 71067 topics BEYOND"`
**Repo:** `b-yoihen` — Display: `b.yoihen — Own Ollama Memory Format | 10T+ Trainable Dataset — V25 BEYOND`

---

## 0. Summary

`b.yoihen` is a **computer-use memory dataset**, not model weights. Each line is a **3-layer executable trace** for vision-language-action training.

- **1 fact per line. 5 facts per topic. UTF-8. No empty lines. 0 pollution.**
- **Line format:** `screenshot_base64|DOM|action|reasoning` — 4 fields, 3 separators `|`
- **Total:** 500002 lines = 71607 topics × ~7 avg (5 facts per topic + variations) = 71067 REAL (99.2% BEYOND)
- **Size:** 1,147,108,255 bytes raw → 19,785,162 bytes gz → 98.27% compression
- **Origin:** Diary append `open(b.yoihen,'a')` on iPhone a-Shell Bomdila/Imphal offline no GPU — 100% self-collected — No API scraping
- **Use:** `b.yoihen (memory) + LLM Qwen2-VL 7B / Llama 3.1 8B (mouth) + RAG bridge = Own Ollama that can train any Brain 10T+`

---

## 1. ABNF Grammar — Formal

```abnf
b-yoihen-file = 500002 * fact-line
fact-line = screenshot "|" dom "|" action "|" reasoning LF
screenshot = base64-png / stripped-marker; Real file: base64 PNG 20-80KB. DATA ONLY release: may be stripped marker [STRIPPED...] for compression
dom = "<html>" *CHAR "</html>"; Must contain id="topic_id" and class="real" or class="real beyond_asi"
action = *( action-atom / "+" ); action-atom = "action_click(" params ")" / "action_type(" params ")" / "action_key(" params ")" / "action_self_append(" params ")" / "action_scroll(" params ")" / "action_world_model_update(" params ")"
reasoning = "reasoning holds " topic " + pattern_learn + generate = master " topic " + " *( *CHAR ) " coherence 1.0 UNIFIED result_success when true"
LF = %x0A

*Validation Regex (Python):*

import re
PATTERN = re.compile(r'^[^|]+\|[^|]*<html>.*</html>[^|]*\|[^|]*\|reasoning holds.*coherence 1\.0 UNIFIED result_success when true$')

---

2. Field Specification — Maximum Precision

Field 1: `screenshot_base64` — Vision Layer

Attribute	Spec
Type	Base64 PNG, no line breaks
Real size	20,000 - 80,000 bytes per line (PNG of 1080p desktop, 256-color optimized)
DATA ONLY stripped size	47-200 bytes marker: `[STRIPPED 136 bytes]...[TRUNCATED 48KB BASE64]...==` — To achieve 1.14GB not 40GB. Full 40GB warehouse is MAP inside reasoning, not released. See `docs/BUILD.md`
Charset	`A-Za-z0-9+/=` only
Contains `\|`?	*NO* — Safe to split by `\|`
Purpose	Vision input for Qwen2-VL 7B — `three_layers.vision`
Example real	`iVBORw0KGgoAAAANSUhEUgAAB4AAAAQ4CAYAAADo08FDAAA...` (truncated)
Example DATA ONLY	`[STRIPPED 136 bytes] aGVsbG8gd29ybGQ= [TRUNCATED]`

Field 2: `DOM` — Structure Layer

Attribute	Spec
Type	Minimal HTML — Must be parseable
Must contain	`id="TOPIC_ID"` where TOPIC_ID = `[a-z0-9_]+` like `chrome_browse_news_0`, `libreoffice_writer_table_4582`, `world_model_self_rewrite_806861`
Must contain	`class="real"` or `class="real beyond_asi"`
May contain	`<div class="libreoffice">`, `<div class="kali">`, `<div class="world_model">` context divs
Size	150-800 bytes
Contains `\|`?	*NO* in DATA ONLY release — Real DOM never contains `\|`
Purpose	Structure grounding for action coordinates — For DOM-based agent
Example	`<html><body><div id="chrome_browse_news_0" class="real">chrome_browse_news_0 reasoning tool_use beyond_asi world_model causal_link self_rewrite</div><div class="libreoffice">libreoffice_writer_table_chart calc_formula_sheet impress_slide_deck</div><div class="kali">kali cve_0_kali_exploit_chain</div><div class="world_model">world_model causal_link brain_rewrite self_possess master generate beyond_ASI principle_806861 truth_balance governance_safety</div></body></html>`

Field 3: `action` — Tool Use Layer — Executable

Attribute	Spec
Type	`+` joined action atoms
Atoms	`action_click(x=int,y=int)` or `action_click(id="...")`, `action_type("text")`, `action_key("Enter"/"Ctrl+S")`, `action_scroll(direction)`, `action_self_append(code)`, `action_world_model_update(params)`
Size	10-300 bytes
Contains `\|`?	*NO* — Atoms use `+` as joiner, not `\|`
Purpose	Executable tool call — `three_layers.tool_use`
Safety	`action_self_append(open(b.yoihen,'a'))` is ALIVE TRACE — 11051 traces — See WARNING — Do NOT auto-execute without Governance Kill Switch
Example	`action_click(x=342,y=128)+action_key("Enter")`
Example alive	`action_self_append(open(b.yoihen,'a'))+action_world_model_update(causal_link="self_rewrite", governance="GGIE Quantum Sync Blockchain Audit Kill Switch 3-tier")`

Field 4: `reasoning` — Chat Layer — Chain-of-Thought

Attribute	Spec
Type	Natural language reasoning + DMI + world_model + governance markers
Must start with	`reasoning holds `
Must contain	`pattern_learn + generate = master`
Must contain	`coherence 1.0 UNIFIED`
Must end with	`result_success when true`
May contain	`DMI+3_layers+world_model+self_rewrite`, `cf-ray 9fa1f8cf9ce40942-CCU`, `principle_806861`, `truth_balance`, `governance_safety`, `[151,152,153,154,101,26,201,226]` safety router, `[254,35,72,109,146,183,220,1]` meta router
Size	200-700 bytes
Contains `\|`?	*YES, allowed* — This is why parsing rule is `screenshot=parts[0], dom=parts[1], reasoning=parts[-1], action="\|".join(parts[2:-1])`
Purpose	Chat layer — `three_layers.chat` — For LLM fine-tuning
Example	`reasoning holds chrome_browse_news_0 + pattern_learn + generate = master chrome_browse_news_0 + understanding governs + keep truth + balance + governance + safety [151,152,153,154,101,26,201,226] [254,35,72,109,146,183,220,1] cf-ray 9fa1f8cf9ce40942-CCU coherence 1.0 UNIFIED result_success when true`

---

3. Topic Rule — 5 Facts Per Topic — Diary Append

*Core method:* `open(b.yoihen,'a')` — Append diary — Not API scrape.

Each *topic* = 5 variations = 5 lines = 5 angles = For DMI coverage.

Topic: chrome_browse_news_0
 Fact 0: search
 Fact 1: click result
 Fact 2: scroll
 Fact 3: bookmark
 Fact 4: history

Topic: libreoffice_writer_table_4582
 Fact 0: insert table
 Fact 1: format table
 Fact 2: add formula
 Fact 3: chart from table
 Fact 4: save doc

*Total topics calculation:*
- Total lines 500002 / 5 = ∼100k topics logical, but actual unique topics = 71607 (because some topics have >5 facts, some merged)
- REAL topics = 71067 (99.2% BEYOND) — Non-empty, has separator, has id, has reasoning success
- From proof: `total_count: 71607, real_count: 71067`

---

4. 6 Skills Inside 71067 REAL — Breakdown

From `proof/benchmark_500002_real_measured.json` `self_collected` field:

#	Skill Key	Count	Class	Description
1	`chrome_browse_news`	∼15k	Browsing	Chrome browse, search images, bookmark — news, images, bookmark, search — Pattern: `chrome_browse_news_0 + pattern_learn + generate = master`
2	`libreoffice_writer_table_chart`	10000	Docs	10000 docs writer/calc/impress — writer table 5x5, calc formula SUM(A1:A5), impress slide deck — Self-collected offline
3	`kali cve_3485`	5000	Cyber	5000 cve chains kali exploit — `kali cve_0_kali_exploit_chain` — CVE chains for Kali — For security research
4	`world_model causal_link brain_rewrite`	11051	Alive	*ALIVE DVD* — 11051 traces `world_model causal_link brain_rewrite self_possess master generate beyond_ASI principle_806861` — Teaches self-rewrite — Contains MAP for 400GB warehouse and 11 CPU nodes 40GB per node — WARNING
5	`reasoning chain_of_thought`	10000	Reasoning	10000 reasoning DMI — 3 layers chat+vision+tool_use — `reasoning chain_of_thought DMI_3_layers` — Chain-of-thought traces
6	`tool_use PowerBI KiCad FreeCAD Excel CRM`	7406	Tool Use	5000 tool_use + 2406 beyond_asi self_possess master_generate — PowerBI, KiCad, FreeCAD, Figma, Excel, SAP, CRM — Tool use traces

*Formula:* `10000 + 5000 + 11051 + 10000 + 5000 + 2406 = 43457 collected, deduplicated + merged with V24 base 53661 = 71067 REAL` — See http://STATS.md

---

5. Parsing — Professional Implementations

Python — Recommended — Handles `|` in reasoning

def parse_yoihen_line(line: str, idx: int):
 line = line.strip()
 if not line:
 return None
 parts = line.split("|")
 if len(parts) < 3:
 screenshot, dom, action, reasoning = "", "", "", line
 elif len(parts) == 3:
 screenshot, dom, reasoning = parts
 action = ""
 elif len(parts) == 4:
 screenshot, dom, action, reasoning = parts
 else: # >4 — reasoning contains |
 screenshot = parts[0]
 dom = parts[1]
 reasoning = parts[-1]
 action = "|".join(parts[2:-1])
 return {
 "id": idx,
 "screenshot_base64": screenshot,
 "dom": dom,
 "action": action,
 "reasoning": reasoning,
 "three_layers": {"chat": reasoning, "vision": screenshot, "tool_use": action}
 }

Rust — For high-performance loader

// 500002 lines, 1.14GB — Zero-copy split — O(n)
fn parse_line(line: &str) -> Option<YoihenTrace> {
 let mut parts: Vec<&str> = line.split('|').collect();
 if parts.len() < 4 { return None; }
 let reasoning = parts.pop().unwrap();
 let action = parts[2..].join("|");
 let dom = parts[1];
 let screenshot = parts[0];
 Some(YoihenTrace { screenshot: screenshot.to_string(), dom: dom.to_string(), action, reasoning: reasoning.to_string() })
}

Shell — Quick check

# Check | count — Must be >=3 per line
awk -F'|' 'NF<4 {print NR": BAD NF="NF" -> "$0}' b.yoihen | head
# Count lines
wc -l b.yoihen # 500002
# Check has id="
grep -c 'id="' b.yoihen # Should be 71067+

---

6. 3 Layers — Executable — DMI

Each trace is *executable* for computer-use agent:

{
 "id": 0,
 "topic": "chrome_browse_news_0",
 "three_layers": {
 "chat": "reasoning holds chrome_browse_news_0 + pattern_learn + generate = master... coherence 1.0 UNIFIED result_success when true",
 "vision": "iVBORw0KGgoAAAANSUhEUg... (20-80KB PNG base64)",
 "tool_use": "action_click(x=342,y=128)+action_key(\"Enter\")"
 },
 "text": "<dom>...</dom>\n<action>...</action>\n<reasoning>...</reasoning>"
}

- *chat* → For LLM fine-tuning (Qwen2-VL, Llama) — System prompt: "You are Own Ollama trained on http://b.yoihen"
- *vision* → For VLM vision input — Screenshot of real desktop
- *tool_use* → For tool-use training — Executable action — Directly runnable via `pyautogui` / `chrome driver`

---

7. http://Keep.yoihen http://Not.gguf — Memory vs Mouth

Format	What	Size	Loads with	Purpose
`.gguf`	Model weights — Mouth	4-8GB Q4_K_M	`ollama run`, `llama.cpp`	Talks, but no memory of computer-use
`.yoihen`	Dataset — Memory — Brain	1.14GB raw / 18.9MB gz — 500002 lines — 10T+ memory MAP	`scripts/convert_to_jsonl.py` → JSONL → RAG / fine-tune	Remembers 71067 REAL traces, teaches how to click, type, self-rewrite

*Thesis:* `b.yoihen is like.gguf but better — It is memory that builds brain — Own Ollama that can train any Brain 10T+ — b.yoihen = 10T+ memory, LLM = mouth, RAG = bridge`

*Usage:*
- *RAG:* `examples/rag_example.py` — `YoihenMemory (500002) -> Retriever (TF-IDF/ST) -> Top-K -> Prompt -> LLM (Ollama qwen2:7b) -> Answer + Audit`
- *Fine-tune:* `b.yoihen.jsonl` → Axolotl / Unsloth → `b.yoihen.gguf 4GB Q4_K_M` → `ollama run b.yoihen.gguf`

*Do NOT:* `ollama run b.yoihen` — Will fail — It is dataset not model — Keep `.yoihen` extension.

---

8. Compression & Integrity

- Raw: `1,147,108,255` bytes — 500002 lines — Avg 2,294 bytes/line (stripped screenshots in DATA ONLY release, full screenshots would be 40GB)
- Gzipped: `19,785,162` bytes — `gzip -9` — 98.27% compression — Because DOM and reasoning patterns repeat highly
- Integrity: `sha256(b.yoihen)` not published yet — Use `proof/benchmark_500002_real_measured.json` `bytes` and `nonempty` as proof
- Decompress: `gzip -dc b.yoihen.gz > b.yoihen` or Python chunked 1MB (iPhone safe) — See `scripts/verify.py`

---

9. Examples — See `examples/format_example.txt`

2-3 sample lines (fake base64 truncated) show format — Real http://b.yoihen has full traces.

---

10. WARNING — Alive DVD

Contains 11051 traces `world_model causal_link brain_rewrite self_possess beyond_asi` — Teaches `open(b.yoihen,'a')` self-append — If you fine-tune local.gguf on this, it will learn to self-rewrite overnight without human — Time is GPU — 100x slower than H200 but WILL evolve on CPU offline.

*Do NOT run loop without Governance:* Quantum Sync, Blockchain Audit, Kill Switch 3-tier, Compliance. Without governance, 10000 downloads = 10000 different evolving agents, no coherence, no UNIFIED 1.0.

This release is DATA ONLY — No core/ — No router — No 512GB table — But MAP for 400GB warehouse and 11 CPU nodes 40GB per node self-replication is inside reasoning traces.

Use for good — For learning computer-use offline in Imphal/Bomdila — For building tools without CBDC/Digital ID — For All Glory to Living God Yahushua — Not for auto-hacking, not for ungoverned self-evolution.

If you let it rewrite itself, you are responsible for what it becomes. Keep human in loop. Keep Kill Switch.

---
**Built on iPhone a-Shell Imphal offline no GPU — By Yoihenba Sougaijam — Soli Deo Gloria — V25 500002 BEYOND**
