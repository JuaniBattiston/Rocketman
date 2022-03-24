from typing import List, TypedDict


class CapsuleData(TypedDict):
    id: str
    reuse_count: int
    water_landings: int
    last_update: str
    launches: List[str]
    serial: str
    status: str
    type: str
