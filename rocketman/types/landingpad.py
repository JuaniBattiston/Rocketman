from typing import Dict, List, TypedDict


class LandingPadData(TypedDict):
    id: str
    images: Dict[str, List[str]]
    name: str
    full_name: str
    status: str
    type: str
    locality: str
    region: str
    latitude: float
    longitude: float
    landing_attempts: int
    landing_successes: int
    wikipedia: str
    details: str
    launches: List[str]
