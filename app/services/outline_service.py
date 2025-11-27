class OutlineService:
    def create_outline(self, topic: str, analysis: dict) -> dict:
        # Create a simple 3-4 section outline using top terms
        top_terms = analysis.get("top_terms", [])[:6]
        outline = {
            "h1": topic.title(),
            "h2": [
                f"What is {topic}",
                f"Why {top_terms[0] if top_terms else 'it'} matters",
                f"Top tools / approaches",
                f"How to choose the right option",
                "Conclusion",
            ],
            "h3": {
                "Top tools / approaches": [f"Overview of {t}" for t in top_terms[:4]]
            }
        }
        return outline
    
# Generates a structured outline based on extracted keywords.

# This class creates a ready-to-use article structure with headings and
# subheadings based on the topic and top keywords.