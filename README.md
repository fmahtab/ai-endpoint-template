# AI Endpoint Template

A FastAPI-based AI service that exposes a reliable `POST /ask` endpoint using the OpenAI Responses API. The project includes token-usage tracking, estimated cost per request, a Streamlit demo interface, and public deployment support.

## 🚀 Live Demo

- **🌐 Streamlit UI:** https://ai-endpoint-template.streamlit.app/
- **📖 Swagger API Docs:** https://ai-endpoint-template.onrender.com/docs
- **❤️ Health Check:** https://ai-endpoint-template.onrender.com/health

## Features

- FastAPI REST API
- GET /health endpoint
- POST /ask endpoint
- OpenAI Responses API integration
- Pydantic request/response validation
- Token usage tracking
- Cost estimation per request
- Streamlit frontend
- Environment-based configuration
- Public cloud deployment
- Smoke tests for deployed endpoints

## Screenshots

### Streamlit UI

(image)

### Swagger API

(image)

## API Response

The `/ask` endpoint returns structured JSON:

```json
{
  "answer": "An AI endpoint is a specific online address or API where applications can access artificial intelligence services, such as machine learning models or natural language processing. It allows developers to send data to the AI service and receive processed results in return. This facilitates integration of AI capabilities into various applications and systems.",
  "tokens_used": 104,
  "cost_usd": 0.0000417
}
```

## Project Structure

```text
ai-endpoint-template/
├── app/
│   ├── api/
│   │   ├── ask.py
│   │   └── health.py
│   ├── core/
│   │   └── config.py
│   ├── schemas/
│   │   └── ask.py
│   ├── services/
│   │   └── reasoning.py
│   └── main.py
├── streamlit_app.py
├── .env.example
├── requirements.txt
└── README.md
```

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/fmahtab/ai-endpoint-template.git
cd ai-endpoint-template
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and provide the required values:

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o-mini
OPENAI_INPUT_PRICE_PER_MILLION=0.15
OPENAI_OUTPUT_PRICE_PER_MILLION=0.60
```

Do not commit the `.env` file.

## Run the FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Health endpoint:

```text
http://127.0.0.1:8000/health
```

## Run the Streamlit UI

Open a second terminal, activate the virtual environment, and run:

```bash
streamlit run streamlit_app.py
```

The UI will normally open at:

```text
http://localhost:8501
```

## Smoke Test

Run:

```bash
python smoke_test.py
```

## Deployment

FastAPI documentation:

```text
https://ai-endpoint-template.onrender.com/docs
```

Health endpoint:

```text
https://ai-endpoint-template.onrender.com/health
```

Streamlit application:

```text
https://ai-endpoint-template.streamlit.app/
```

## Public API Test

PowerShell:

```powershell
Invoke-RestMethod `
  -Method Post `
  -Uri "https://ai-endpoint-template.onrender.com/ask" `
  -ContentType "application/json" `
  -Body '{"question":"What is an AI endpoint?"}'
```

## Request Flow

```text
User
  ↓
Streamlit UI
  ↓
POST /ask
  ↓
FastAPI Router
  ↓
ReasoningService
  ↓
OpenAI Responses API
  ↓
Structured JSON response
```

## Technology Stack

* Python
* FastAPI
* Pydantic
* OpenAI Python SDK
* Streamlit
* HTTPX
* Uvicorn
* Render

## Future Improvements

- Streaming responses
- Conversation history
- Structured Outputs
- Authentication
- Docker support
- CI/CD
- Unit tests

## License

This project is available under the MIT License.
