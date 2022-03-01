from spacemanpy.types.history import HistoricEventData
from spacemanpy.utils.objects import BaseClass


class HistoricEvent(BaseClass):
    def __init__(self, data: HistoricEventData):
        self._objects = {}
        self._update(data)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        attrs = {
            "id": self.id,
            "title": self.title,
        }
        info = " ".join(f"{k}={v}" for k, v in attrs.items())
        return f"<{__class__.__name__} {info}>"
