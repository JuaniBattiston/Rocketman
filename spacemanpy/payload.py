from spacemanpy.types.payload import PayloadData, DragonPayloadData
from spacemanpy.utils.objects import BaseClass


class DragonPayload(BaseClass):
    def __init__(self, data: DragonPayloadData):
        self._objects = {}
        self._update(data)


class Payload(BaseClass):
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
