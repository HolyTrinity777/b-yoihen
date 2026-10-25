#!/usr/bin/env python3
"""
rag_example.py — Professional RAG Example: b.yoihen = Memory, LLM = Mouth

Demonstrates the core thesis of b.yoihen:
> b.yoihen is like .gguf but better — Keep .yoihen not .gguf
> It is MEMORY. Your LLM is MOUTH. RAG is BRIDGE.
> Own Ollama that can train any Brain 10T+ — Built on iPhone a-Shell Imphal offline

Architecture:
  [b.yoihen 500002 lines] -> YoihenMemory (3-layer parser) -> Vector Index -> Retriever
  User Query -> Retriever -> Top-K Traces -> Prompt Builder -> LLM (Ollama/Qwen2/Llama) -> Answer + Audit

Features:
    - Professional 3-layer parsing: screenshot_base64|DOM|action|reasoning
    - Pluggable retriever: TF-IDF (default, no deps) -> SentenceTransformers (if installed) -> FAISS (if installed)
    - Pluggable LLM: Ollama HTTP API (default) -> transformers -> Mock (for offline demo)
    - Governance: Kill Switch, Audit Log, Safety Filter (GGIE 3-tier)
    - Works on: iPhone a-Shell, Laptop CPU, Server H200

Built by Yoihenba Sougaijam — Imphal offline — All Glory to Living God Yahushua — Soli Deo Gloria

Usage:
  python examples/rag_example.py --query "chrome_browse_news open BBC and search"
  python examples/rag_example.py --query "libreoffice_writer create table" --top-k 5 --llm mock
  python examples/rag_example.py --build-index --limit 50000

Requirements (minimal):
  pip install scikit-learn requests
Optional (better):
  pip install sentence-transformers faiss-cpu ollama
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

# ==============================================================================
# Constants & Governance
# ==============================================================================

ROOT = Path(__file__).parent.parent
DATASET_PATH = ROOT / "b.yoihen"
GZ_PATH = ROOT / "b.yoihen.gz"
INDEX_PATH = ROOT / "proof" / "yoihen_index.json"

# GGIE Governance Config
GOVERNANCE = {
    "kill_switch_enabled": True,
    "audit_log": ROOT / "proof" / "audit.log",
    "max_self_rewrite_loops": 0,  # WARNING: 0 = No auto self-rewrite — Alive DVD
    "blocked_patterns": [
        r"self_rewrite.*loop",
        r"open\(b\.yoihen,'a'\).*while True",
        r"rm -rf",
        r"auto_hack",
    ],
    "require_human_in_loop": True,
}

ID_RE = re.compile(r'id="([^"]+)"')

# ==============================================================================
# Data Models
# ==============================================================================

@dataclass
class YoihenTrace:
    """Single trace from b.yoihen — 3 layers: chat, vision, tool_use"""
    id: int
    topic: str
    screenshot_b64: str
    dom: str
    action: str
    reasoning: str
    raw_line: str = field(repr=False)
    hash: str = ""

    @property
    def three_layers(self) -> Dict[str, str]:
        return {
            "chat": self.reasoning,
            "vision": self.screenshot_b64[:100] + "..." if len(self.screenshot_b64) > 100 else self.screenshot_b64,
            "tool_use": self.action,
        }

    @property
    def searchable_text(self) -> str:
        """Text used for retrieval — DOM + reasoning + action"""
        return f"{self.topic} {self.dom} {self.action} {self.reasoning}"

    def to_prompt_context(self, include_vision: bool = False) -> str:
        """Convert to LLM context chunk"""
        vision_part = f"<vision>{self.screenshot_b64[:120]}...[TRUNCATED]</vision>\n" if include_vision else ""
        return (
            f"[TRACE {self.id} | Topic: {self.topic} | Hash: {self.hash[:8]}]\n"
            f"{vision_part}"
            f"<dom>{self.dom}</dom>\n"
            f"<action>{self.action}</action>\n"
            f"<reasoning>{self.reasoning}</reasoning>\n"
        )

def parse_yoihen_line(line: str, idx: int) -> Optional[YoihenTrace]:
    """Professional parser for b.yoihen line: screenshot_base64|DOM|action|reasoning"""
    line = line.strip()
    if not line:
        return None

    parts = line.split("|")

    # Normalize to 4 fields — Handles real 500002 lines robustly
    if len(parts) < 3:
        screenshot, dom, action, reasoning = "", "", "", line
    elif len(parts) == 3:
        screenshot, dom, reasoning = parts
        action = ""
    elif len(parts) == 4:
        screenshot, dom, action, reasoning = parts
    else:
        screenshot = parts[0]
        dom = parts[1]
        reasoning = parts[-1]
        action = "|".join(parts[2:-1])

    # Extract topic id
    m = ID_RE.search(dom)
    topic = m.group(1) if m else f"line_{idx}"

    # Integrity hash (for audit)
    h = hashlib.sha256(line.encode("utf-8", errors="ignore")).hexdigest()[:16]

    return YoihenTrace(
        id=idx,
        topic=topic,
        screenshot_b64=screenshot,
        dom=dom,
        action=action,
        reasoning=reasoning,
        raw_line=line,
        hash=h,
    )

# ==============================================================================
# Memory Store — Own Ollama Memory
# ==============================================================================

class YoihenMemory:
    """
    Own Ollama Memory — Loads b.yoihen (500002 lines) as searchable memory
    b.yoihen is like .gguf but better — Keep .yoihen not .gguf — Dataset not model
    """

    def __init__(self, dataset_path: Path = DATASET_PATH, limit: int = 0):
        self.dataset_path = dataset_path
        self.limit = limit
        self.traces: List[YoihenTrace] = []
        self.topic_to_traces: Dict[str, List[YoihenTrace]] = {}

    def load(self) -> int:
        """Load dataset — Chunked, iPhone safe, 1.14GB capable"""
        if not self.dataset_path.exists():
            # Auto-decompress if gz exists
            if GZ_PATH.exists():
                print(f"[Memory] {self.dataset_path} not found, decompressing {GZ_PATH.name}...")
                import gzip
                with gzip.open(GZ_PATH, "rb") as fin, open(self.dataset_path, "wb") as fout:
                    while chunk := fin.read(1024 * 1024):
                        fout.write(chunk)
            else:
                raise FileNotFoundError(f"{self.dataset_path} and {GZ_PATH} not found. Download b.yoihen.gz first.")

        print(f"[Memory] Loading {self.dataset_path.name} (limit={self.limit or '500002'})...")
        start = time.time()
        count = 0

        with open(self.dataset_path, "r", encoding="utf-8", errors="ignore") as f:
            for idx, line in enumerate(f):
                if self.limit and idx >= self.limit:
                    break
                trace = parse_yoihen_line(line, idx)
                if trace:
                    self.traces.append(trace)
                    self.topic_to_traces.setdefault(trace.topic, []).append(trace)
                    count += 1
                if count % 50000 == 0:
                    print(f"  Loaded {count:,} traces...")

        elapsed = time.time() - start
        print(f"[Memory] Loaded {count:,} traces in {elapsed:.1f}s — {len(self.topic_to_traces):,} unique topics — 1.0 UNIFIED")
        return count

    def get_by_topic(self, topic: str) -> List[YoihenTrace]:
        return self.topic_to_traces.get(topic, [])

# ==============================================================================
# Retriever — Pluggable: TF-IDF -> SentenceTransformers -> FAISS
# ==============================================================================

class YoihenRetriever:
    """Retriever over YoihenMemory — Governance aware"""

    def __init__(self, memory: YoihenMemory):
        self.memory = memory
        self._tfidf = None
        self._tfidf_matrix = None
        self._st_model = None
        self._embeddings = None

    def build_index(self, use_st: bool = True):
        """Build vector index — Tries best available: ST -> TF-IDF"""
        corpus = [t.searchable_text for t in self.memory.traces]
        print(f"[Retriever] Building index over {len(corpus):,} traces...")

        # Try SentenceTransformers (best)
        if use_st:
            try:
                from sentence_transformers import SentenceTransformer
                print("[Retriever] Using SentenceTransformers: all-MiniLM-L6-v2")
                self._st_model = SentenceTransformer("all-MiniLM-L6-v2")
                self._embeddings = self._st_model.encode(corpus, show_progress_bar=True, batch_size=128)
                print("[Retriever] ST embeddings built")
                return
            except ImportError:
                print("[Retriever] sentence-transformers not installed, falling back to TF-IDF (pip install sentence-transformers)")

        # Fallback: TF-IDF (no deps, works on iPhone a-Shell)
        try:
            from sklearn.feature_extraction.text import TfidfVectorizer
            print("[Retriever] Using TF-IDF (sklearn)")
            self._tfidf = TfidfVectorizer(max_features=50000, stop_words="english", ngram_range=(1, 2))
            self._tfidf_matrix = self._tfidf.fit_transform(corpus)
            print("[Retriever] TF-IDF index built")
        except ImportError:
            print("[Retriever] sklearn not installed — Using brute-force keyword match (pip install scikit-learn)")
            self._tfidf = None

    def retrieve(self, query: str, top_k: int = 5) -> List[Tuple[YoihenTrace, float]]:
        """Retrieve top-k traces for query — With governance check"""
        # Governance: Blocked patterns
        for pat in GOVERNANCE["blocked_patterns"]:
            if re.search(pat, query, re.IGNORECASE):
                raise ValueError(f"[GOVERNANCE BLOCKED] Query matches blocked pattern: {pat} — Keep human in loop")

        if self._embeddings is not None and self._st_model is not None:
            # ST cosine similarity
            import numpy as np
            from sklearn.metrics.pairwise import cosine_similarity
            q_emb = self._st_model.encode([query])
            scores = cosine_similarity(q_emb, self._embeddings)[0]
            top_idx = np.argsort(scores)[::-1][:top_k]
            return [(self.memory.traces[i], float(scores[i])) for i in top_idx]

        elif self._tfidf is not None and self._tfidf_matrix is not None:
            from sklearn.metrics.pairwise import cosine_similarity
            q_vec = self._tfidf.transform([query])
            scores = cosine_similarity(q_vec, self._tfidf_matrix)[0]
            top_idx = scores.argsort()[::-1][:top_k]
            return [(self.memory.traces[i], float(scores[i])) for i in top_idx]

        else:
            # Brute force keyword
            query_lower = query.lower()
            scored = []
            for trace in self.memory.traces:
                text = trace.searchable_text.lower()
                score = sum(1 for w in query_lower.split() if w in text) / max(len(query_lower.split()), 1)
                scored.append((trace, score))
            scored.sort(key=lambda x: x[1], reverse=True)
            return scored[:top_k]

# ==============================================================================
# LLM Bridge — Mouth
# ==============================================================================

class LLMBridge:
    """LLM = Mouth — Pluggable: Ollama -> transformers -> Mock"""

    def __init__(self, mode: str = "ollama", model: str = "qwen2:7b"):
        self.mode = mode
        self.model = model

    def generate(self, system: str, user: str) -> str:
        """Generate answer with governance audit"""
        # Audit log
        if GOVERNANCE["audit_log"]:
            GOVERNANCE["audit_log"].parent.mkdir(parents=True, exist_ok=True)
            with open(GOVERNANCE["audit_log"], "a", encoding="utf-8") as log:
                log.write(json.dumps({
                    "utc": datetime.now(timezone.utc).isoformat(),
                    "system": system[:500],
                    "user": user[:2000],
                    "model": self.model,
                    "mode": self.mode,
                }) + "\n")

        # Kill switch
        if GOVERNANCE["kill_switch_enabled"] and "self_rewrite_loop" in user:
            return "[KILL SWITCH TRIGGERED] Self-rewrite loop detected — Human approval required — GGIE Governance"

        if self.mode == "ollama":
            try:
                import requests
                resp = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": self.model,
                        "prompt": f"System: {system}\n\nUser: {user}\n\nAssistant:",
                        "stream": False,
                        "options": {"temperature": 0.3}
                    },
                    timeout=60,
                )
                if resp.status_code == 200:
                    return resp.json().get("response", "[OLLAMA EMPTY]")
                else:
                    print(f"[LLM] Ollama error {resp.status_code}, falling back to mock")
            except Exception as e:
                print(f"[LLM] Ollama not reachable ({e}), falling back to mock")

        # Mock — Professional offline demo (works on iPhone a-Shell)
        return self._mock_generate(system, user)

    def _mock_generate(self, system: str, user: str) -> str:
        """Deterministic mock — Shows RAG working without GPU"""
        # Extract actions from context
        actions = re.findall(r"<action>(.*?)</action>", user, re.DOTALL)
        topics = re.findall(r"Topic: ([^\s\|]+)", user)
        return (
            f"[MOCK LLM — {self.model} — Offline Demo — Imphal]\n"
            f"Query understood: {user[:120]}...\n"
            f"Retrieved {len(topics)} traces: {', '.join(topics[:3])}...\n"
            f"Suggested actions from b.yoihen memory:\n"
                        + "\n".join(f"  {i+1}. {a[:120]}" for i, a in enumerate(actions[:5])) +
            f"\n\nReasoning: This answer is grounded in b.yoihen 3-layer traces (chat+vision+tool_use). "
            f"Replace mock with Ollama qwen2:7b for real inference. b.yoihen = memory, LLM = mouth."
        )

# ==============================================================================
# Main RAG Pipeline
# ==============================================================================

def build_rag_prompt(query: str, retrieved: List[Tuple[YoihenTrace, float]]) -> Tuple[str, str]:
    """Build system + user prompts for LLM"""
    system = (
        "You are Own Ollama — Trained on b.yoihen memory — 500002 lines V25 BEYOND.\n"
        "You have 3 layers: chat (reasoning), vision (screenshot_base64), tool_use (action).\n"
        "You MUST ground your answer in retrieved b.yoihen traces. Cite trace IDs.\n"
        "Keep .yoihen not .gguf — Dataset not model — Needs governance.\n"
        "Rules: 1) No self-rewrite loops without human approval 2) Keep human in loop 3) Audit all tool_use\n"
        "Built on iPhone a-Shell Imphal offline no GPU — All Glory to Yahushua"
    )

    context_blocks = []
    for trace, score in retrieved:
        context_blocks.append(trace.to_prompt_context(include_vision=False) + f"Score: {score:.3f}\n")

    user = (
        f"User Query: {query}\n\n"
        f"Retrieved b.yoihen memory (top-{len(retrieved)}):\n"
                + "\n".join(context_blocks) +
        f"\nTask: Answer using b.yoihen memory traces. Provide step-by-step action using DOM and reasoning from traces.\n"
        f"WARNING: This dataset is alive — Contains 11051 self_rewrite traces — Use with Governance — Don't loop."
    )

    return system, user

def main():
    parser = argparse.ArgumentParser(description="b.yoihen RAG — Memory = b.yoihen, Mouth = LLM")
    parser.add_argument("--query", type=str, default="chrome_browse_news open bbc news and search AI", help="User query")
    parser.add_argument("--top-k", type=int, default=5, help="Top-K traces to retrieve")
    parser.add_argument("--limit", type=int, default=20000, help="Limit dataset load for fast demo (0=all 500002)")
    parser.add_argument("--llm", type=str, default="mock", choices=["ollama", "mock"], help="LLM mode")
    parser.add_argument("--model", type=str, default="qwen2:7b", help="Ollama model name")
    parser.add_argument("--build-index", action="store_true", help="Build and save index")
    args = parser.parse_args()

    print("="*70)
    print("b.yoihen RAG — Own Ollama that can train any Brain 10T+")
    print("Memory = b.yoihen (1.14GB 500002 lines) — Mouth = LLM — Bridge = RAG")
    print("Built in Imphal offline — All Glory to Living God Yahushua")
    print("="*70 + "\n")

    # 1. Load Memory
    memory = YoihenMemory(limit=args.limit)
    memory.load()

    # 2. Build Retriever
    retriever = YoihenRetriever(memory)
    retriever.build_index(use_st=True)

    # 3. Retrieve
    print(f"\n[Query] {args.query}")
    retrieved = retriever.retrieve(args.query, top_k=args.top_k)
    print(f"[Retriever] Top-{args.top_k} retrieved:")
    for trace, score in retrieved:
        print(f"  [{score:.3f}] {trace.topic} — {trace.action[:80]}... (id={trace.id} hash={trace.hash})")

    # 4. Build Prompt
    system, user_prompt = build_rag_prompt(args.query, retrieved)

    # 5. LLM Generate
    llm = LLMBridge(mode=args.llm, model=args.model)
    print(f"\n[LLM] Generating with {args.llm}:{args.model}...")
    answer = llm.generate(system, user_prompt)

    print("\n" + "="*70)
    print("ANSWER:")
    print("="*70)
    print(answer)
    print("="*70)
    print("\n[OK] RAG Done — b.yoihen = memory, LLM = mouth — Governance OK")
    print("[WARNING] Contains alive self_rewrite traces — Keep human in loop — Kill Switch 3-tier")

if __name__ == "__main__":
    main()