from fastapi import FastAPI

from app.api.events import router as events_router


app = FastAPI(
    title="KU Event API",
    description="고려대학교 그룹 일정 통합 관리 서비스 API",
    version="0.1.0"
)


app.include_router(events_router)


@app.get("/")
def root():
    return {
        "message": "KU Event Backend"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }