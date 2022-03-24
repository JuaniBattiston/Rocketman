from typing import List, TypedDict


class CoreData(TypedDict):
    id: str
    block: int
    reuse_count: int
    rtls_attempts: int
    asds_landings: int
    last_update: str
    launches: List[str]
    serial: str
    status: str
