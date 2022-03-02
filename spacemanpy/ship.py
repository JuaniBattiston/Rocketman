from spacemanpy.types.ship import ShipData
from spacemanpy.utils.objects import BaseClass


class Ship(BaseClass):

    __slots__ = (
        "id",
        "last_ais_update",
        "legacy_id",
        "model",
        "type",
        "roles",
        "imo",
        "mmsi",
        "abs",
        "_class",
        "mass_kg",
        "mass_lbs",
        "year_built",
        "home_port",
        "status",
        "speed_kn",
        "course_deg",
        "latitude",
        "longitude",
        "link",
        "image",
        "name",
        "active",
        "launches",
    )

    def __init__(self, data: ShipData) -> None:
        self._objects = {}
        self._update(data)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        attrs = {
            "id": self.id,
            "name": self.name,
            "active": self.active,
        }
        info = " ".join(f"{k}={v}" for k, v in attrs.items())
        return f"<{__class__.__name__} {info}>"
