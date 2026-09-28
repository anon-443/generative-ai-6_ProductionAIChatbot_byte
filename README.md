# Production AI Chatbot

AVIP 2026 Generative AI — Task 6. A deployable chatbot foundation with provider abstraction, retrieval-ready context, conversation transcripts, safety checks, observability hooks, and an evaluation set.

## Run
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python app.py
```

The default app runs in deterministic demo mode so the repository is testable without exposing a key. Replace the provider adapter only after documenting the exact hosted/local model and license.

## Resume-grade engineering
- Explicit `Provider` interface keeps UI independent from model vendor.
- Input/output safety gates are auditable and conservative.
- Session transcripts are JSONL and suitable for evaluation.
- Evaluation prompts cover factuality, refusal behavior, instruction following, and prompt injection.

## AVIP evidence
- `conversations/`: 10-session transcript template
- `eval/cases.jsonl`: evaluation set
- `app.py`: local demo and safety-aware request flow
- `MODEL_CARD.md`: model/license record
