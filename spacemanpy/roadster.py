from spacemanpy.types.roadster import RoadsterData
from spacemanpy.utils.objects import BaseClass


class Roadster(BaseClass):

    __slots__ = (
        "id",
        "name",
        "launch_date_utc",
        "launch_date_unix",
        "launch_mass_kg",
        "launch_mass_lbs",
        "norad_id",
        "epoch_jd",
        "orbit_type",
        "apoapsis_au",
        "periapsis_au",
        "semi_major_axis_au",
        "eccentricity",
        "inclination",
        "longitude",
        "periapsis_arg",
        "period_days",
        "speed_kph",
        "speed_mph",
        "earth_distance_km",
        "earth_distance_mi",
        "mars_distance_km",
        "mars_distance_mi",
        "flickr_images",
        "wikipedia",
        "video",
        "details",
    )

    def __init__(self, data: RoadsterData):
        self._objects = {}
        self._update(data)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        attrs = {
            "id": self.id,
            "name": self.name,
        }
        info = " ".join(f"{k}={v}" for k, v in attrs.items())
        return f"<{__class__.__name__} {info}>"
