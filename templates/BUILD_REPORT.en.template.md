<!-- Language: [🇷🇺 Русский](BUILD_REPORT.md) · 🇬🇧 English -->

# Build Report — {{Project name}}

A build report: what was built, how it was verified, what remains. The final development artifact.

## 1. Build Identity
- **Project:** {{name}}
- **Version / date:** {{...}}
- **Stack:** {{brief}}

## 2. Summary
{{2–3 sentences: what the product is and its current state}}

## 3. What Was Built
- {{module/feature 1}} — {{status}}
- {{module/feature 2}} — {{status}}

## 4. Test Results
- {{N tests, coverage, what they check}}
- {{run command}}

## 5. Security
- {{secrets, what is gitignored, how keys are stored}}

## 6. Open Issues & Deviations
- {{what was deferred / where you deviated from the plan and why}}

## 7. File Map
```
{{tree of key files with one-line descriptions}}
```

## 8. How to Run
{{brief instructions or link to docs/HOW_TO_DEPLOY.md}}
