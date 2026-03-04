from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Plan:
    to_create: List[Dict] = field(default_factory=list)
    to_remove: List[str] = field(default_factory=list)
    to_update: List[Dict] = field(default_factory=list)