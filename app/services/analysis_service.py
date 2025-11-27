from collections import Counter
from app.models.serp import SerpResult

class AnalysisService:
    def analyze(self, serp_results: list[SerpResult]) -> dict:
        # Very simple analysis: collect frequent words in titles/snippets
        words = []
        for r in serp_results:
            words += r.title.lower().split()
            words += r.snippet.lower().split()
        # basic cleanup
        stop = set(["the","and","for","to","in","of","a","with","best","2025"])
        filtered = [w.strip(".,()!") for w in words if w.isalpha() and w not in stop]
        top = Counter(filtered).most_common(20)
        return {"top_terms": [t for t,_ in top], "top_counts": top}
    
# Extracts frequently occurring keywords from SERP results.

# Counter → Counts how many times each word appears.

# SerpResult → Data model for a single search result.

# This class extracts the 20 most frequent meaningful keywords
# from the titles and snippets of search results.