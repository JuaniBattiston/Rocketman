from typing import Dict, List, TypedDict, Union


class Fairing(TypedDict):
    recovered: bool
    recovery_attempt: bool
    reused: bool
    ships: List[str]


class Failure(TypedDict):
    altitude: Union[float, None]
    reason: str


class LaunchData(TypedDict):
    id: str
    fairings: Fairing
    links: Dict
    static_fire_date_utc: str
    static_fire_date_unix: int
    net: bool
    window: int
    rocket: str
    success: bool
    failures: List[Failure]
    details: str
    crew: List[str]
    ships: List[str]
    capsules: List[str]
    payloads: List[str]
    launchpad: str
    flight_number: int
    name: str
    date_utc: str
    date_unix: int
    date_local: str
    tbd: bool
    launch_library_id: Union[str, None]
