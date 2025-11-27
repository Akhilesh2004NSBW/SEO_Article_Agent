from fastapi import FastAPI
from app.api.v1 import routes

app = FastAPI(title="SEO Article Agent - Starter")
app.include_router(routes.router, prefix="/api/v1")

@app.get("/")
async def health():
    return {"status": "ok"}
