from spacemanpy.types.payload import PayloadData, DragonPayloadData
from spacemanpy.utils.objects import BaseClass


class DragonPayload(BaseClass):

    __slots__ = (
        "capsule",
        "flight_time_sec",
        "land_landing",
        "manifest",
        "mass_returned_kg",
        "mass_returned_lbs",
        "water_landing",
    )

    def __init__(self, data: DragonPayloadData):
        self._objects = {}
        self._update(data)


class Payload(BaseClass):

    __slots__ = (
        "id",
        "dragon",
        "name",
        "type",
        "reused",
        "launch",
        "customers",
        "norad_ids",
        "nationalities",
        "manufacturers",
        "mass_kg",
        "mass_lbs",
        "orbit",
        "reference_system",
        "regime",
        "longitude",
        "semi_major_axis_km",
        "eccentricity",
        "periapsis_km",
        "apoapsis_km",
        "inclination_deg",
        "period_min",
        "lifespan_years",
        "epoch",
        "mean_motion",
        "raan",
        "arg_of_pericenter",
        "mean_anomaly",
    )

    def __init__(self, data: PayloadData):
        self._objects = {"dragon": DragonPayload}
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
