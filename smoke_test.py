"""Smoke test for the deployed /health and /ask endpoints."""

import os
import sys

import httpx

API_URL = os.getenv(
    "API_URL",
    "https://ai-endpoint-template.onrender.com/ask",
)
HEALTH_URL = os.getenv(
    "HEALTH_URL",
    API_URL.removesuffix("/ask") + "/health",
)
TIMEOUT_SECONDS = 60.0
HEALTH_TIMEOUT_SECONDS = 10.0

QUESTIONS = [
    "What is an AI endpoint?",
    "What is FastAPI?",
    "What is token usage in LLM APIs?",
]


def validate_health_response(data: dict) -> list[str]:
    """Return a list of validation error messages (empty if valid)."""
    errors = []

    status = data.get("status")
    if status != "healthy":
        errors.append('status must be "healthy"')

    return errors


def validate_response(data: dict) -> list[str]:
    """Return a list of validation error messages (empty if valid)."""
    errors = []

    if "answer" not in data or not isinstance(data["answer"], str) or not data["answer"].strip():
        errors.append("answer must be a non-empty string")

    tokens_used = data.get("tokens_used")
    if not isinstance(tokens_used, int) or tokens_used <= 0:
        errors.append("tokens_used must be a positive integer")

    cost_usd = data.get("cost_usd")
    if not isinstance(cost_usd, (int, float)) or cost_usd <= 0:
        errors.append("cost_usd must be a positive float")

    return errors


def run_health_test(client: httpx.Client) -> bool:
    print(f"\nHealth check: GET {HEALTH_URL}")

    try:
        response = client.get(HEALTH_URL, timeout=HEALTH_TIMEOUT_SECONDS)
    except httpx.HTTPError as exc:
        print(f"FAIL - request error: {exc}")
        return False

    if response.status_code != 200:
        print(f"FAIL - expected status 200, got {response.status_code}")
        print(f"Response body: {response.text}")
        return False

    try:
        data = response.json()
    except ValueError:
        print("FAIL - response is not valid JSON")
        return False

    errors = validate_health_response(data)
    if errors:
        print("FAIL - invalid response:")
        for error in errors:
            print(f"  - {error}")
        print(f"Response body: {data}")
        return False

    print("PASS")
    print(f"  status: {data['status']}")
    return True


def run_test(client: httpx.Client, question: str) -> bool:
    print(f"\nQuestion: {question!r}")

    try:
        response = client.post(API_URL, json={"question": question})
    except httpx.HTTPError as exc:
        print(f"FAIL - request error: {exc}")
        return False

    if response.status_code != 200:
        print(f"FAIL - expected status 200, got {response.status_code}")
        print(f"Response body: {response.text}")
        return False

    try:
        data = response.json()
    except ValueError:
        print("FAIL - response is not valid JSON")
        return False

    errors = validate_response(data)
    if errors:
        print("FAIL - invalid response:")
        for error in errors:
            print(f"  - {error}")
        print(f"Response body: {data}")
        return False

    print("PASS")
    print(f"  answer: {data['answer'][:80]}{'...' if len(data['answer']) > 80 else ''}")
    print(f"  tokens_used: {data['tokens_used']}")
    print(f"  cost_usd: {data['cost_usd']}")
    return True


def main() -> int:
    print("Running smoke tests")
    print(f"  Health: {HEALTH_URL}")
    print(f"  Ask:    {API_URL}")

    results = []
    with httpx.Client(timeout=TIMEOUT_SECONDS) as client:
        results.append(run_health_test(client))
        for question in QUESTIONS:
            results.append(run_test(client, question))

    passed = sum(results)
    total = len(results)

    print(f"\nSummary: {passed}/{total} passed")

    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
