import json
from pathlib import Path
from app.models.serp import SerpResult

class SerpService:
    def __init__(self):
        self.mock_file = Path(__file__).parents[2] / "data" / "mock_serp_data.json"

    def fetch_top_10(self, topic: str) -> list[SerpResult]:
        # For the starter project we return mocked SERP results
        with open(self.mock_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        results = [SerpResult(**r) for r in data[:10]]
        return results

    
# This class simulates getting the top 10 search results from a JSON file
# and returns them as structured SerpResult objects.