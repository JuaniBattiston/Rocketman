from spacemanpy.types.payload import PayloadData


class Payload:
    def __init__(self, data: PayloadData):
        self._update(data)

    def _update(self, data: PayloadData):
        for k, v in data.items():
            setattr(self, k, v)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        attrs = {
            "id": self.id,
            "name": self.name,
        }
        info = " ".join(f"{k}={v}" for k, v in attrs.items())
        return f"<{__class__.__name__} {info}>"
