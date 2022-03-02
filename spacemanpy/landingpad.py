from spacemanpy.types.landingpad import LandingPadData
from spacemanpy.utils.objects import BaseClass


class LandingPad(BaseClass):

    __slots__ = (
        "id",
        "images",
        "name",
        "full_name",
        "status",
        "type",
        "locality",
        "region",
        "latitude",
        "longitude",
        "landing_attempts",
        "landing_successes",
        "wikipedia",
        "details",
        "launches",
    )

    def __init__(self, data: LandingPadData):
        self._objects = {}
        self._update(data)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        attrs = {
            "id": self.id,
            "name": self.name,
            "status": self.status,
        }
        info = " ".join(f"{k}={v}" for k, v in attrs.items())
        return f"<{__class__.__name__} {info}>"
