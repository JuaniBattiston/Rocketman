from spacemanpy.types.starlink import StarlinkData, SpaceTrackData
from spacemanpy.utils.objects import BaseClass


class SpaceTrack(BaseClass):
    def __init__(self, data: SpaceTrackData) -> None:
        self._objects = {}
        self._update(data)


class Starlink(BaseClass):
    def __init__(self, data: StarlinkData) -> None:
        self._objects = {"spaceTrack": SpaceTrack}
        self._update(data)

    def __repr__(self) -> str:
        attrs = {
            "id": self.id,
            "version": self.version,
        }
        info = " ".join(f"{k}={v}" for k, v in attrs.items())
        return f"<{__class__.__name__} {info}>"
