from spacemanpy.types.ship import ShipData
from spacemanpy.utils.objects import BaseClass


class Ship(BaseClass):
    def __init__(self, data: ShipData) -> None:
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
