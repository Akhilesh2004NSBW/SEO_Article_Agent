

# SEO Article Agent

**SEO Article Agent** is an intelligent content generation platform designed for digital marketers, SEO specialists, and content creators to produce structured, SEO-optimized articles efficiently. Using FastAPI and Python, it analyzes search trends, generates outlines, and creates complete articles enriched with SEO metadata.

---

## 🚀 Features

* **Automated SEO Analysis:** Extracts top search terms from search results to guide article creation.
* **Dynamic Article Generation:** Creates structured articles with headings and subheadings based on keyword analysis.
* **SEO Optimized Output:** Generates meta descriptions, primary & secondary keywords, and JSON-LD structured data.
* **Interactive Frontend:** Simple HTML/JS interface for submitting topics and viewing results.
* **Modular Architecture:** Separate services for SERP fetching, analysis, outline creation, and article generation.
* **Extensible & Maintainable:** Designed to easily integrate advanced features, live APIs, or databases.

---

## 🏗️ Project Structure

```
seo-article-agent/
│
├── app/
│   ├── api/v1/routes.py
│   ├── core/config.py
│   ├── models/
│   ├── services/
│   ├── schemas/
│   ├── utils/helpers.py
│   └── __init__.py
│
├── data/mock_serp_data.json
├── tests/test_basic.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── main.py
├── requirements.txt
├── run.sh
├── README.md
└── 800-docs.doc
```

---

## ⚙️ Tech Stack

* **Backend:** Python, FastAPI
* **Frontend:** HTML, CSS, JavaScript
* **Data:** Mock SERP JSON, extensible to live API integration
* **Deployment:** Uvicorn for local development; scalable to production

---

## 💡 How It Works

1. **User Input:** Enter a topic in the frontend input box.
2. **SERP Fetching:** Backend fetches top search results (mock or real API).
3. **Keyword Analysis:** Extracts high-value keywords for the article.
4. **Outline Creation:** Generates structured headings and subheadings.
5. **Article Generation:** Produces a detailed article automatically.
6. **SEO Optimization:** Generates meta description, keywords, and JSON-LD structured data.
7. **View Results:** For full generated content, see the `800-docs.doc` file.

---

## ⚡ Quick Start

1. **Clone the repository:**

```bash
git clone https://github.com/Akhilesh2004NSBW/SEO_Article_Agent.git
cd SEO_Article_Agent
```

2. **Install dependencies:**

```bash
python -m pip install -r requirements.txt
```

3. **Run the backend:**

```bash
python -m uvicorn main:app --reload --port 8001
```

4. **Open the frontend:**
   Open `frontend/index.html` in your browser to submit topics and view generated results.

5. **View generated articles:**
   For detailed examples of generated content, refer to `800-docs.doc`.

---

## 📈 Future Enhancements

* Integration with real-time SERP API for live search results.
* AI-powered content suggestions using GPT models.
* User authentication and article history tracking.
* Export articles in PDF or Markdown formats.
* Enhanced frontend UI with modern frameworks (React/Vue).

---

## 🔒 License

This project is open-source and free to use, modify, and distribute.

---


