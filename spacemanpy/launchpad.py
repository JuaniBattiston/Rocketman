from spacemanpy.types.launchpad import LaunchPadData
from spacemanpy.utils.objects import BaseClass


class LaunchPad(BaseClass):
    def __init__(self, data: LaunchPadData):
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
