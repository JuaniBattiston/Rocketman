from typing import List, TypedDict


class RoadsterData(TypedDict):
    id: str
    name: str
    launch_date_utc: str
    launch_date_unix: int
    launch_mass_kg: int
    launch_mass_lbs: int
    norad_id: int
    epoch_jd: float
    orbit_type: str
    apoapsis_au: float
    periapsis_au: float
    semi_major_axis_au: float
    eccentricity: float
    inclination: float
    longitude: float
    periapsis_arg: float
    period_days: float
    speed_kph: float
    speed_mph: float
    earth_distance_km: float
    earth_distance_mi: float
    mars_distance_km: float
    mars_distance_mi: float
    flickr_images: List[str]
    wikipedia: str
    video: str
    details: str
