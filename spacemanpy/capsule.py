from spacemanpy.types.capsule import CapsuleData
from spacemanpy.utils.objects import BaseClass


class Capsule(BaseClass):
    def __init__(self, data: CapsuleData):
        self._objects = {}
        self._update(data)

    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        attrs = {
            "id": self.id,
            "status": self.status,
        }
        info = " ".join(f"{k}={v}" for k, v in attrs.items())
        return f"<{__class__.__name__} {info}>"
