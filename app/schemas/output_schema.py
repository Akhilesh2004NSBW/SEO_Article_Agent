from pydantic import BaseModel
from typing import Any, Dict

class GenerateResponse(BaseModel):
    title: str
    meta_description: str
    outline: Dict[str, Any]
    article: str
    keywords: Dict[str, Any]
    structured_data: Dict[str, Any]