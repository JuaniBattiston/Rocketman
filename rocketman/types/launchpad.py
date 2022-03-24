from typing import Dict, List, TypedDict


class LaunchPadData(TypedDict):
    id: str
    images: Dict
    name: str
    full_name: str
    locality: str
    region: str
    latitude: float
    longitud: float
    launch_attempts: int
    launch_successes: int
    rockets: List[str]
    timezone: str
    launches: List[int]
    status: str
    details: str
