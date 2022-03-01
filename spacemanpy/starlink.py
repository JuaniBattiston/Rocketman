from spacemanpy.types.starlink import StarlinkData, SpaceTrackData


class SpaceTrack:
    def __init__(self, data: SpaceTrackData) -> None:
        self._update(data)

    def _update(self, data: SpaceTrackData) -> None:
        for k, v in data.items():
            setattr(self, k.lower(), v)


class Starlink:
    def __init__(self, data: StarlinkData) -> None:
        self._objects = {"spaceTrack": SpaceTrack}
        self._update(data)

    def _update(self, data: StarlinkData) -> None:
        for k, v in data.items():
            if k in self._objects:
                setattr(self, k.lower(), self._objects[k](v))
                continue

            setattr(self, k.lower(), v)

    def __repr__(self) -> str:
        attrs = {
            "id": self.id,
            "version": self.version,
        }
        info = " ".join(f"{k}={v}" for k, v in attrs.items())
        return f"<{__class__.__name__} {info}>"
