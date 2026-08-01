from app.schemas.ask import AskResponse
from app.core.config import settings
from openai import OpenAI



SYSTEM_PROMPT = """
You are a helpful assistant that can answer questions and help with tasks.
Answer clearly and concisely in no more than 3 sentences.
"""

class ReasoningService:

    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)

    def answer_question(self, question: str) -> AskResponse:
        
        response = self.client.responses.create(            
            model=settings.openai_model,
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question}
            ],
            max_output_tokens=150,
        )

        
        usage = response.usage
        cost_usd= (
            usage.input_tokens * settings.openai_input_price_per_million / 1_000_000 
            + usage.output_tokens * settings.openai_output_price_per_million / 1_000_000
        )

        return AskResponse(
            answer=response.output_text,
            tokens_used= usage.total_tokens,
            cost_usd= round(cost_usd, 8),
        )
