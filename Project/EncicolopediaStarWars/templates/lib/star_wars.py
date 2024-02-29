from dataclasses import dataclass
from typing import List, Optional


@dataclass
class DataStarWars:
    name: str
    height: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str


@dataclass
class AllResults:
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: list[DataStarWars]



