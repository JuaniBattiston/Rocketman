from spacemanpy.types.core import CoreData


class Core:
    def __init__(self, data: CoreData):
        self._update(data)

    def _update(self, data: CoreData):
        for k, v in data.items():
            setattr(self, k, v)

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
