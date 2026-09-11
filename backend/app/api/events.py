from datetime import date, datetime
from typing import List, Optional

from fastapi import APIRouter, Query

from app.schemas.event import EventResponse


router = APIRouter(
    prefix="/events",
    tags=["events"]
)


mock_events = [
    {
        "id": 1,
        "group_id": 1,
        "group_name": "고려대학교 인공지능학과",
        "title": "학과 정기회의",
        "description": "이번 학기 주요 일정과 학사 관련 사항을 논의합니다.",
        "start_at": "2026-09-11T14:00:00",
        "end_at": "2026-09-11T16:00:00",
        "target": "전체 멤버",
        "location": "애기능생활관 301호"
    },
    {
        "id": 2,
        "group_id": 2,
        "group_name": "스터디 모임",
        "title": "주간 스터디",
        "description": "이번 주 스터디 내용을 함께 공부합니다.",
        "start_at": "2026-09-12T19:00:00",
        "end_at": "2026-09-12T21:00:00",
        "target": "스터디 멤버",
        "location": "하나스퀘어"
    },
    {
        "id": 3,
        "group_id": 1,
        "group_name": "고려대학교 인공지능학과",
        "title": "졸업 논문 발표",
        "description": "졸업 예정자의 논문 발표가 진행됩니다.",
        "start_at": "2026-09-20T10:00:00",
        "end_at": "2026-09-20T12:00:00",
        "target": "전체 멤버",
        "location": "우정정보관"
    }
]


@router.get("", response_model=List[EventResponse])
def get_events(
    start_date: Optional[date] = Query(default=None),
    end_date: Optional[date] = Query(default=None)
):
    events = mock_events

    if start_date is not None:
        events = [
            event
            for event in events
            if datetime.fromisoformat(event["start_at"]).date() >= start_date
        ]

    if end_date is not None:
        events = [
            event
            for event in events
            if datetime.fromisoformat(event["start_at"]).date() <= end_date
        ]

    return events