from spacemanpy.types.core import CoreData
from spacemanpy.utils.objects import BaseClass


class Core(BaseClass):
    def __init__(self, data: CoreData):
        self._objects = {}
        self._update(data)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        attrs = {
            "id": self.id,
            "serial": self.serial,
            "status": self.status,
        }
        info = " ".join(f"{k}={v}" for k, v in attrs.items())
        return f"<{__class__.__name__} {info}>"
