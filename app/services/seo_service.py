import json

class SEOService:
    def build(self, topic: str, article: str, outline: dict, analysis: dict) -> dict:
        title_tag = f"{topic.title()} — Complete Guide"
        meta = f"Learn about {topic} — overview, top approaches, and how to choose the best option."
        keywords = {
            "primary": [topic],
            "secondary": analysis.get('top_terms', [])[:8]
        }
        json_ld = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": title_tag,
            "description": meta
        }
        return {"title_tag": title_tag, "meta_description": meta, "keywords": keywords, "json_ld": json_ld}
        
        
# Produces SEO metadata, keyword lists, and JSON-LD structured data.

# class SEOService: A service to create SEO-related data for an article.

# This class prepares SEO-friendly information for an article so search
# engines can understand and rank it better.
