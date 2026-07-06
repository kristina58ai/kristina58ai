<!-- Language: [🇷🇺 Русский](HOW_TO_DEPLOY.md) · 🇬🇧 English -->

# {{Project name}} — Setup & Run

The correct install order, step by step, to reproduce from scratch.

## Requirements

- {{e.g. Python 3.11+}}
- {{e.g. Node 20+ / Anki / llama.cpp — whatever is needed}}

## Installation (in order)

1. Clone the repository
   ```bash
   git clone {{repo-url}}
   cd {{repo}}
   ```
2. Dependencies
   ```bash
   {{e.g. pip install -e ".[dev]"}}
   ```
3. Environment / secrets
   ```bash
   cp .env.example .env   # fill in the keys
   ```
   {{which keys are needed and where to get them}}
4. {{migrations / DB init / model download — if any}}
5. Verify
   ```bash
   {{e.g. python -m {{app}} doctor}}
   ```

## Run

```bash
{{run command}}
```

## Troubleshooting

- **{{symptom}}** → {{fix}}
