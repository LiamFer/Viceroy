from pydantic import BaseModel
from typing import Optional

class MockModel(BaseModel):
    id: Optional[int] = None
    method: str
    path: str
    response: dict
    status_code: int = 200
    delay_ms: int = 0
