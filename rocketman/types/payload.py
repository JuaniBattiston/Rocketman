from typing import List, TypedDict, Union


class DragonPayloadData(TypedDict):
    capsule: Union[str, None]
    flight_time_sec: Union[int, None]
    land_landing: Union[bool, None]
    manifest: Union[str, None]
    mass_returned_kg: Union[int, None]
    mass_returned_lbs: Union[int, None]
    water_landing: Union[bool, None]


class PayloadData(TypedDict):
    id: str
    dragon: DragonPayloadData
    name: str
    type: str
    reused: bool
    launch: str
    customers: List[str]
    norad_ids: List[str]
    nationalities: List[str]
    manufacturers: List[str]
    mass_kg: int
    mass_lbs: int
    orbit: str
    reference_system: str
    regime: str
    longitude: Union[float, None]
    semi_major_axis_km: Union[str, None]
    eccentricity: Union[str, None]
    periapsis_km: int
    apoapsis_km: int
    inclination_deg: int
    period_min: Union[int, None]
    lifespan_years: Union[int, None]
    epoch: Union[int, None]
    mean_motion: Union[int, None]
    raan: Union[int, None]
    arg_of_pericenter: Union[int, None]
    mean_anomaly: Union[int, None]
