from fastapi import APIRouter
from pydantic import BaseModel
from app.schemas.input_schema import GenerateRequest
from app.services.serp_service import SerpService
from app.services.analysis_service import AnalysisService
from app.services.outline_service import OutlineService
from app.services.article_service import ArticleService
from app.services.seo_service import SEOService

router = APIRouter()

class GenerateResponse(BaseModel):
    title: str
    meta_description: str
    outline: dict
    article: str
    keywords: dict
    structured_data: dict

@router.post("/generate", response_model=GenerateResponse)
async def generate(req: GenerateRequest):
    # 1. fetch SERP
    serp = SerpService().fetch_top_10(req.topic)

    # 2. analyze
    analysis = AnalysisService().analyze(serp)

    # 3. outline
    outline = OutlineService().create_outline(req.topic, analysis)

    # 4. article
    article = ArticleService().generate(req.topic, outline, req.word_count)

    # 5. seo
    seo = SEOService().build(req.topic, article, outline, analysis)

    return {
        "title": seo["title_tag"],
        "meta_description": seo["meta_description"],
        "outline": outline,
        "article": article,
        "keywords": seo["keywords"],
        "structured_data": seo["json_ld"],
    }
    