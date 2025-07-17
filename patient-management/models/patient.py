from models.visit import Visit
from dataclasses import dataclass, field
from typing import List

@dataclass
class Patient:
    id: str
    name: str
    birthdate: str
    has_insurance: bool
    visits: List[Visit] = field(default_factory=list)
    score: int = 0