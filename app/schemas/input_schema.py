from pydantic import BaseModel

class GenerateRequest(BaseModel):
    topic: str
    word_count: int = 1500
    language: str = "en"