from spacemanpy.types.launch import FailureData, FairingData, LaunchData
from spacemanpy.utils.objects import BaseClass


class Fairing(BaseClass):

    __slots__ = (
        "recovered",
        "recovery_attempt",
        "reused",
        "ships",
    )

    def __init__(self, data: FairingData):
        self._objects = {}
        self._update(data)


class Failure(BaseClass):

    __slots__ = (
        "time",
        "altitude",
        "reason",
    )

    def __init__(self, data: FailureData):
        self._objects = {}
        self._update(data)


class Launch(BaseClass):

    __slots__ = (
        "id",
        "fairings",
        "links",
        "static_fire_date_utc",
        "static_fire_date_unix",
        "net",
        "window",
        "rocket",
        "success",
        "failures",
        "details",
        "crew",
        "ships",
        "capsules",
        "payloads",
        "launchpad",
        "flight_number",
        "name",
        "date_utc",
        "date_unix",
        "date_local",
        "tbd",
        "launch_library_id",
    )

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
