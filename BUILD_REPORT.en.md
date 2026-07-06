<!-- Language: [🇷🇺 Русский](BUILD_REPORT.md) · 🇬🇧 English -->

# 🛠️ How the portfolio was built

In brief: what each project is, how it was built and on what stack. Full technical reports live in each repo's `docs/BUILD_REPORT.md`.

## How projects are built

Every project goes through the single multi-agent **DEV-HUB** pipeline (idea → product): requirements → architecture → validation → plan → build. Contracts guard each hand-off, and every significant decision is recorded in the project's `DECISIONS.md` — so any choice can be defended in an interview.

---

## DEV-HUB V.6

- **What it is:** an AI-agent orchestration system that takes a project from idea to a finished product. It's the "brain" that built the other portfolio projects.
- **How it was built:** evolved from version V.5. The product layer runs in Cowork via a role-switching pattern (one agent plays different roles in turn); the coding layer is a separate pipeline. Contracts between phases block progress until artifacts are complete.
- **Stack in detail:**
  - *Orchestration* — multi-agent networks with explicit transitions and checkpoints
  - *Specs* — everything in Markdown with strict templates (requirements, architecture, plan)
  - *Contracts* — automatic completeness checks at network hand-offs
  - *Crash safety* — state is saved after each agent step

## Content-hub

- **What it is:** an AI tool that auto-runs content across 5 social networks (Telegram, X, LinkedIn, Medium, Threads). It generates posts in my voice, plans content and collects stats. It exists in two versions.
- **How it was built:** the **Personal** version went through DEV-HUB (Networks 1→2) and was assembled in Cowork; the **Showcase** version (a website) is currently in progress on LangGraph.
- **Stack in detail (Personal):**
  - *4 multi-agent networks* — Identity Manager (persona onboarding), Planner (content plan), Post Generator (post generation), Analyzer (a learning loop over the best posts); Backup as a cross-cutting service
  - *RAG persona* — Chroma (vector store) + a local `multilingual-e5-large` embedding model, so posts sound like me
  - *Database* — SQLite in STRICT mode (plans → posts → versions → stats)
  - *Activity checkers* — Playwright for X/LinkedIn/Medium (parsing post stats) + API for Telegram/Threads; with rate limiting
  - *Backup* — data snapshots to Google Drive
  - *Quality* — Alembic migrations, 40 tests
- **Stack in detail (Showcase):** a web app on **LangGraph** (a hot-stack demo for recruiters) — under development.

## Learning-hub

- **What it is:** a personal multi-agent learning system. Agents guide me through "plan → theory → notes → cards → practice → check"; knowledge settles into a graph and reviews run in Anki. The AI doesn't learn for me — I do; the system automates everything around it.
- **How it was built:** went through DEV-HUB (Networks 1+2), assembled by the Builder and deployed in beta; a v1.1 revision is ongoing.
- **Stack in detail:**
  - *Core* — a Python package `lh` (~9 modules): CLI, session planner, graph rebuild
  - *Knowledge graph* — Kuzu (embedded, Cypher, vector index): topics, prerequisite links, cards, errors — as a rebuildable cache
  - *Semantics* — Qwen3 embeddings locally via llama.cpp (offline, free)
  - *Reviews* — Anki + FSRS: cards ship as `.apkg`, forgetting stats return to the graph
  - *Knowledge map* — an interactive graph on Cytoscape.js
  - *Reliability* — 36 tests, including a full-recovery test after destroying the DB

---

<!-- Fill in as projects mature. Details — in each repo's docs/BUILD_REPORT.md. -->
