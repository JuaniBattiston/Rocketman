from typing import List, TypedDict


class CrewMemberData(TypedDict):
    id: str
    name: str
    agency: str
    image: str
    wikipedia: str
    launches: List[str]
    status: str
