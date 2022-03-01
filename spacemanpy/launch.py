from spacemanpy.types.launch import FailureData, FairingData, LaunchData
from spacemanpy.utils.objects import BaseClass


class Fairing(BaseClass):
    def __init__(self, data: FairingData):
        self._objects = {}
        self._update(data)


class Failure(BaseClass):
    def __init__(self, data: FailureData):
        self._objects = {}
        self._update(data)


class Launch(BaseClass):
    def __init__(self, data: LaunchData):
        self.data = data
        self._objects = {"failures": Failure, "fairings": Fairing}
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
