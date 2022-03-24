from typing import Dict, TypedDict


class HistoricEventData(TypedDict):
    id: str
    links: Dict[str, str]
    title: str
    event_date_utc: str
    event_date_unix: int
    details: str
