from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class Visit:
    date: datetime
    reason: str
    symptoms: List[str]
    temperature: Optional[float] = None