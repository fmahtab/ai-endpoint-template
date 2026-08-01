from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        max_length=500,
        description="The question to ask the AI.",
        examples=["What is an AI endpoint?"],
    )


class AskResponse(BaseModel):
    answer: str
