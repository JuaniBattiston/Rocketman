from typing import List, TypedDict, Union


class ShipData(TypedDict):
    id: str
    last_ais_update: Union[str, None]
    legacy_id: Union[str, None]
    model: Union[str, None]
    type: str
    roles: List[str]
    imo: int
    mmsi: int
    abs: int
    _class: int
    mass_kg: int
    mass_lbs: int
    year_built: int
    home_port: str
    status: Union[str, None]
    speed_kn: Union[int, None]
    course_deg: Union[int, None]
    latitude: Union[float, None]
    longitude: Union[float, None]
    link: str
    image: str
    name: str
    active: bool
    launches: List[str]
