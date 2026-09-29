# Production AI Chatbot

AVIP 2026 Generative AI — Task 6. A Flask chatbot service with a provider boundary, safety gate, JSONL-compatible conversation evidence, and a ten-case evaluation set.

## Run locally
```bash
pip install -r requirements.txt
export CHAT_API_KEY=your_key
export CHAT_MODEL=gpt-5-mini
python app.py
```

Without a provider key, the service returns a clearly labeled offline response for local route testing. API keys are read from environment variables and are never stored in this repository.

## Evidence
- `conversations/`: 10 captured model sessions with token metadata
- `eval/cases.jsonl`: evaluation prompts covering factuality, clarity, grounding, safety, privacy, and prompt injection
- `MODEL_CARD.md`: model, API, safety policy, and limitations
- `app.py`: HTTP service and safety-aware request flow

## Example
```bash
curl -X POST http://localhost:8000/chat -H 'Content-Type: application/json' -d '{"message":"Explain generative AI simply"}'
```
