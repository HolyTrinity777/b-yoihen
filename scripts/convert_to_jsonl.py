"""
convert_to_jsonl.py - Convert b.yoihen (500002 lines) to JSONL for training/RAG

Format per line: screenshot_base64|DOM|action|reasoning
Outputs:
    - b.yoihen.jsonl (full, for fine-tuning Qwen2-VL 7B -> .gguf)
    - b.yoihen.rag.jsonl (RAG: memory = b.yoihen, mouth = LLM)
    - b.yoihen.sample.jsonl (first 100 lines, for inspection)

Keep .yoihen extension not .gguf - Dataset not .gguf model
All Glory to Living God Yahushua - Built in Imphal offline

Usage:
    python scripts/convert_to_jsonl.py
    python scripts/convert_to_jsonl.py --limit 1000 --sample-only
"""

import argparse
import json
import re
from pathlib import Path
from typing import Dict, Optional

ROOT = Path(__file__).parent.parent
INPUT = ROOT / "b.yoihen"
OUTPUT_FULL = ROOT / "b.yoihen.jsonl"
OUTPUT_RAG = ROOT / "b.yoihen.rag.jsonl"
OUTPUT_SAMPLE = ROOT / "b.yoihen.sample.jsonl"

# Pattern to extract id="..." from DOM
ID_RE = re.compile(r'id="([^"]+)"')

def parse_yoihen_line(line: str, idx: int) -> Optional[Dict]:
    """Parse one .yoihen line into structured dict."""
    line = line.strip()
    if not line:
        return None

    parts = line.split("|")
    
    # Normalize to 4 fields: screenshot, dom, action, reasoning
    if len(parts) < 3:
        screenshot, dom, action, reasoning = "", "", "", line
    elif len(parts) == 3:
        screenshot, dom, reasoning = parts
        action = ""
    elif len(parts) == 4:
        screenshot, dom, action, reasoning = parts
    else:
        # >4 parts: first=screenshot, second=dom, last=reasoning, middle=action
        screenshot = parts[0]
        dom = parts[1]
        reasoning = parts[-1]
        action = "|".join(parts[2:-1])

    # Extract topic from DOM id if present
    topic_match = ID_RE.search(dom)
    topic = topic_match.group(1) if topic_match else f"line_{idx}"

    return {
        "id": idx,
        "topic": topic,
        "screenshot_base64": screenshot,
        "dom": dom,
        "action": action,
        "reasoning": reasoning,
        "three_layers": {
            "chat": reasoning,
            "vision": screenshot,
            "tool_use": action,
        },
        # Unified text for vision-language training
        "text": f"<dom>{dom}</dom>\n<action>{action}</action>\n<reasoning>{reasoning}</reasoning>",
    }

def main():
    parser = argparse.ArgumentParser(description="Convert b.yoihen to JSONL")
    parser.add_argument("--limit", type=int, default=0, help="Limit lines (0 = all 500002)")
    parser.add_argument("--sample-only", action="store_true", help="Only create 100-line sample")
    args = parser.parse_args()

    if not INPUT.exists():
        print(f"[FAIL] {INPUT} not found. Run scripts/verify.py first to get b.yoihen from b.yoihen.gz")
        return

    limit = args.limit if args.limit > 0 else (100 if args.sample_only else 0)
    print(f"[CONVERT] {INPUT.name} -> JSONL (limit={limit if limit else 'all 500002'})")

    total = 0
    # Open outputs
    fout_full = None if args.sample_only else open(OUTPUT_FULL, "w", encoding="utf-8")
    fout_rag = None if args.sample_only else open(OUTPUT_RAG, "w", encoding="utf-8")
    fout_sample = open(OUTPUT_SAMPLE, "w", encoding="utf-8")

    with open(INPUT, "r", encoding="utf-8", errors="ignore") as fin:
        for idx, line in enumerate(fin):
            if limit and idx >= limit:
                break
            
            rec = parse_yoihen_line(line, idx)
            if not rec:
                continue

            # Full training format
            if fout_full:
                # Keep full screenshot for training, but you can truncate if needed
                json.dump(rec, fout_full, ensure_ascii=False)
                fout_full.write("\n")

                # RAG format
                rag_rec = {
                    "id": rec["id"],
                    "topic": rec["topic"],
                    "context": f"{rec['dom']} {rec['reasoning']}",
                    "query": rec["topic"],
                    "answer": rec["action"],
                    "three_layers": rec["three_layers"],
                }
                json.dump(rag_rec, fout_rag, ensure_ascii=False)
                fout_rag.write("\n")

            # Sample (first 100)
            if idx < 100:
                sample_rec = {
                    "id": rec["id"],
                    "topic": rec["topic"],
                    "dom_preview": rec["dom"][:200],
                    "action": rec["action"],
                    "reasoning_preview": rec["reasoning"][:500],
                }
                json.dump(sample_rec, fout_sample, ensure_ascii=False)
                fout_sample.write("\n")

            total += 1
            if total % 50000 == 0:
                print(f"  {total:,} converted...")

    if fout_full: fout_full.close()
    if fout_rag: fout_rag.close()
    fout_sample.close()

    print(f"\n[OK] Converted {total:,} records")
    if not args.sample_only:
        print(f"  Full: {OUTPUT_FULL} ({OUTPUT_FULL.stat().st_size/1024/1024:.1f} MB)")
        print(f"  RAG:  {OUTPUT_RAG} ({OUTPUT_RAG.stat().st_size/1024/1024:.1f} MB)")
    print(f"  Sample: {OUTPUT_SAMPLE} (100 lines)")

    print("\n[NEXT]")
    print("  1. Fine-tune: axolotl / unsloth with b.yoihen.jsonl -> Qwen2-VL 7B -> Q4_K_M .gguf")
    print("  2. RAG: b.yoihen = memory, LLM = mouth, bridge = b.yoihen.rag.jsonl")
    print("  3. Keep .yoihen extension not .gguf - Dataset not model")
    print("\n[WARNING] Contains 11051 self_rewrite alive traces - Don't loop without Governance")

if __name__ == "__main__":
    main()
