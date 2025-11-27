import re

def clean_text(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()

# ✔ Removes extra spaces 
# ✔ Removes newlines 
# ✔ Makes the text clean and neat