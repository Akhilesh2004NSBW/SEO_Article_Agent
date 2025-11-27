from pydantic import BaseModel
from typing import List, Dict

class ArticleOut(BaseModel):
    title: str
    meta_description: str
    outline: Dict[str, List[str]]
    content: str
    keywords: Dict[str, List[str]]
    json_ld: Dict
    
# Represents an article output object.

