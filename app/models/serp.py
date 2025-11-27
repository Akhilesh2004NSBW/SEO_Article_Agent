from pydantic import BaseModel

class SerpResult(BaseModel):
    rank: int
    url: str
    title: str
    snippet: str
    
# This (class SerpResult(BaseModel):) class defines what a search result looks like, 
# and Pydantic makes sure the data is correct and clean.