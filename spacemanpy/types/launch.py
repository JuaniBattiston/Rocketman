from typing import Dict, List, TypedDict, Union


class FairingData(TypedDict):
    recovered: bool
    recovery_attempt: bool
    reused: bool
    ships: List[str]


class FailureData(TypedDict):
    time: Union[int, None]
    altitude: Union[float, None]
    reason: Union[str, None]


class LaunchData(TypedDict):
    id: str
    fairings: FairingData
    links: Dict
    static_fire_date_utc: str
    static_fire_date_unix: int
    net: bool
    window: int
    rocket: str
    success: bool
    failures: List[FailureData]
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
