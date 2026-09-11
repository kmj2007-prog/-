from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class EventResponse(BaseModel):
    id: int
    group_id: int
    group_name: str

    title: str
    description: Optional[str] = None

    start_at: datetime
    end_at: Optional[datetime] = None

    target: Optional[str] = None
    location: Optional[str] = None