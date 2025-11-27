
# SEO Article Agent — Starter

[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.122.0-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

*SEO Article Agent* is a FastAPI-based backend service that generates *SEO-optimized articles* for any given topic.  
It simulates SERP analysis, keyword extraction, outline creation, article generation, and SEO metadata production.  

This project is a starter template for building *intelligent content generation systems*.

---

## 📋 Table of Contents

- [Project Structure](#project-structure)  
- [Installation](#installation)  
- [Running the App](#running-the-app)  
- [API Endpoints](#api-endpoints)  
- [Running Tests](#running-tests)  
- [Features](#features)  
- [Notes](#notes)  
- [License](#license)  

---

## 📁 Project Structure

seo-article-agent/ ├── app/ │   ├── init.py │   ├── main.py │   ├── api/ │   │   └── v1/ │   │       └── routes.py │   ├── core/ │   │   ├── config.py │   │   └── utils.py │   ├── models/ │   │   ├── serp.py │   │   ├── article.py │   │   └── job.py │   ├── services/ │   │   ├── serp_service.py │   │   ├── analysis_service.py │   │   ├── outline_service.py │   │   ├── article_service.py │   │   └── seo_service.py │   └── schemas/ │       ├── input_schema.py │       └── output_schema.py ├── data/ │   └── mock_serp_data.json ├── tests/ │   └── test_basic.py ├── requirements.txt ├── README.md └── run.sh

---

## ⚙ Installation

1. *Clone the repository*

```bash
git clone <your-repo-url>
cd seo-article-agent

2. Make run.sh executable



chmod +x run.sh

3. Run the project



./run.sh

> This will create a virtual environment, install dependencies, and start the FastAPI server.




---

🚀 API Endpoints

Health Check

GET /

Response:

{
  "status": "ok"
}


---

Generate Article

POST /api/v1/generate

Request Body Example:

{
  "topic": "best smartphones under 20000",
  "word_count": 500
}

Response Example:

{
  "title": "Best Smartphones Under 20000 — Complete Guide",
  "meta_description": "Learn about best smartphones under 20000 — overview, top approaches, and how to choose the best option.",
  "outline": {
    "h1": "Best Smartphones Under 20000",
    "h2": [
      "What is best smartphones under 20000",
      "Why phone matters",
      "Top tools / approaches",
      "How to choose the right option",
      "Conclusion"
    ],
    "h3": {
      "Top tools / approaches": [
        "Overview of phone",
        "Overview of camera",
        "Overview of performance",
        "Overview of battery"
      ]
    }
  },
  "article": "Full article content...",
  "keywords": {
    "primary": ["best smartphones under 20000"],
    "secondary": ["phone", "camera", "battery", "performance"]
  },
  "structured_data": {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "Best Smartphones Under 20000 — Complete Guide",
    "keywords": ["phone", "camera", "battery", "performance"],
    "description": "Learn about best smartphones under 20000 — overview, top approaches, and how to choose the best option."
  }
}


---

🧪 Running Tests

Use pytest to run tests:

pytest -v

Tests included:

Health check endpoint

Article generation workflow



---

⚡ Features

Fetches top SERP results (mocked)

Extracts common keywords from SERP data

Generates structured article outlines

Produces human-readable article content

Builds SEO metadata (title, meta description, JSON-LD)

Fully tested with Pytest

Easily extendable to real SERP API integration



---

📌 Notes

Mock SERP data located at data/mock_serp_data.json

Customize word count in the generation request

This starter is fully extendable to integrate with live SERP APIs



---

📝 License

MIT License

---
