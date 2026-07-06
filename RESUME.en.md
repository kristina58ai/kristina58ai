<!-- Language: [🇷🇺 Русский](RESUME.md) · 🇬🇧 English -->
<!-- Resume DRAFT. Edit everything in [brackets]. PDF is built by the robot (scripts/gen_resume.py). -->

# Tikhon [Last name]

**AI Agent Developer · Applied LLM Engineer**

---

## 1. About me

AI agent and RAG developer. I design and build multi-agent pipelines in Python and use them myself — the "I build tools I use" principle: I only publish tools I actually use every day. Applied track (AI agents, RAG, production, LLM engineering), not Research. I document every architectural decision as an ADR and can defend it from memory in a technical interview.

- 🎓 [University, field], 1st year — I learn by building real products
- 🌍 I work bilingually (RU + EN), all documentation in both languages
- 📍 [City · open to remote / relocation]

## 2. Desired positions

- AI Agent Developer
- Applied LLM Engineer
- Prompt Engineer
- Junior+ AI Engineer

## 3. Skills

- **AI / LLM:** multi-agent systems (multi-agent orchestration), RAG (embeddings, vector store, retrieval, re-ranking), LangGraph, prompt engineering, local LLM inference
- **Languages / tools:** Python, Git / GitHub, GitHub Actions (CI/CD), pytest, Alembic, Playwright
- **Data:** SQLite, Kuzu (graph DB), Chroma (vector DB), Anki / FSRS, vector indexes
- **Practices:** ADR / Decision Log, bilingual documentation, reproducibility, testing, production engineering

## 4. Experience / Projects

### DEV-HUB V.6 — multi-agent orchestration
The origin of the whole system and its "brain". A multi-agent pipeline of specialized AI agents that drives a product through the full cycle: requirements → architecture → validation → planning → build. It implements agent/network linking via a role-switching pattern, with contract checks at every phase hand-off and crash-safe state management. The project shows skills in designing multi-agent systems, orchestrating LLM agents, prompt engineering, and building reproducible, documented production pipelines.
**Stack / keywords:** multi-agent orchestration, LLM agents, prompt engineering, Markdown specs, phase contracts, state management, reproducibility · 🔗 [github.com/kristina58ai/dev-hub](https://github.com/kristina58ai/dev-hub)

### Content-hub — AI tool for social media, RAG + LangGraph (2 versions)
An AI tool for auto-running content across 5 social networks (Telegram, X, LinkedIn, Medium, Threads) with a production-oriented architecture. **Personal** (Cowork): 4 multi-agent networks (persona onboarding, content planner, post generator, analyzer) + a RAG persona over vector search so posts sound like me; automatic post-activity checkers (Playwright + social APIs), SQLite (STRICT) storage, Alembic migrations, 40 automated tests. **Showcase** (in progress): a full web app on **LangGraph**. The project demonstrates RAG (embeddings, vector store, retrieval), external API integrations, web automation, database work, and CI/CD.
**Stack:** Python, RAG, Chroma (vector DB), multilingual-e5, LangGraph, Playwright, SQLite, Alembic, pytest, CI/CD · 🔗 [github.com/kristina58ai/content-hub-personal](https://github.com/kristina58ai/content-hub-personal)

### Learning-hub — graph-RAG learning system
A beta-deployed multi-agent learning system built on a **graph-RAG** approach. Agents guide the user through "plan → theory → notes → cards → practice → check"; knowledge is stored in a knowledge graph (Kuzu) with a vector index, semantics are computed locally with Qwen3 embeddings via llama.cpp, spaced repetition runs in Anki/FSRS, and progress is shown on an interactive knowledge map (Cytoscape.js). The core is a Python package of ~9 modules with 36 automated tests, including a full-recovery test after destroying the DB. A deliberate move away from classic RAG toward a curated knowledge graph — because learning needs prerequisite links and forgetting-memory. Demonstrates graph-RAG, vector databases, local LLM inference, and the design of reliable, testable systems.
**Stack:** Python, Kuzu (graph DB), vector search, Qwen3 embeddings, llama.cpp, Anki/FSRS, Cytoscape.js, pytest · **Role:** architecture + implementation · 🔗 [github.com/kristina58ai/learning-hub](https://github.com/kristina58ai/learning-hub)

### Part-time / other

**Fine-tuning generative models for image generation** — fine-tuned diffusion image-generation models for a custom style/domain: dataset preparation and labeling, training and hyperparameter tuning, generation-quality evaluation.
*Keywords:* fine-tuning, diffusion models, image generation, generative AI, dataset preparation, computer vision.

**Large index table (100M+ rows) with per-row validation** — designed and populated an index table of 100M+ rows with validation of every record: an ETL pipeline for collection and cleaning, per-row integrity checks, and optimization for scale.
*Keywords:* data engineering, ETL, data validation, 100M+ rows, indexing, SQL, data quality, large-scale processing.

## 5. Courses / Education

- [University, field], 1st year, [year]–present
- [Courses / certificates — or remove]

## 6. Contacts

- GitHub: [github.com/kristina58ai](https://github.com/kristina58ai)
- Email: Tikhonmineev@gmail.com
- Telegram: [t.me/Tikhonmineev](https://t.me/Tikhonmineev)
