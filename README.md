# AI Endpoint Template

A FastAPI-based AI service that exposes a reliable `POST /ask` endpoint using the OpenAI Responses API. The project includes token-usage tracking, estimated cost per request, a Streamlit demo interface, and public deployment support.

## Features

* FastAPI backend
* `GET /health` endpoint
* `POST /ask` endpoint
* OpenAI Responses API integration
* Pydantic request and response validation
* Token-usage reporting
* Estimated API cost per request
* Streamlit user interface
* Environment-based configuration
* Public HTTPS deployment

## API Response

The `/ask` endpoint returns structured JSON:

```json
{
  "answer": "An AI-generated response.",
  "tokens_used": 120,
  "cost_usd": 0.0000513
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

## Public API

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
Add the deployed Streamlit URL here
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

## License

This project is available under the MIT License.
