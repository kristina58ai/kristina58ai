<!-- Language: [🇷🇺 Русский](SPEC.md) · 🇬🇧 English -->

# {{Project name}} — Specification

How the product works: stack, components, data, external services, modes. A reference for anyone who wants to understand the system deeper than the README.

## 1. Stack

| Layer | Technology | Why |
|---|---|---|
| {{language/runtime}} | {{...}} | {{...}} |
| {{data/DB}} | {{...}} | {{...}} |
| {{interface}} | {{...}} | {{...}} |

## 2. Components and how they connect

- **{{Component 1}}** — {{responsibility}}
- **{{Component 2}}** — {{responsibility}}

{{How components talk to each other}}

## 3. Data and memory

{{Where and how data is stored, top-level schema, what is persistent, what is cache}}

## 4. External services / APIs

- **{{Service}}** — {{why, direction, limits}}

## 5. How it works (main scenario)

{{Step by step: user does X → system Y → result Z}}

## 6. Modes / commands

- `{{command}}` — {{what it does}}

## 7. Constraints and assumptions

- {{constraint}}
