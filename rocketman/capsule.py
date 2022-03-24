from .types.capsule import CapsuleData
from .utils.objects import BaseClass


class Capsule(BaseClass):

    """
    Represents a Capsule.

    Attributes
    ----------
    id: :class:`str`
        The capsule id.
    reuse_count: :class:`int`
        The amount of times the capsule was reused.
    water_landings: :class:`int`
        The amount of water landings.
    last_update: :class:`str`
        The last official status update on the capsule.
    launches: List[:class:`str`]
        A list of the capsule launches ids.
    serial: :class:`str`
        The capsule serial.
    status: :class:`str`
        The capsule status.
    type: :class:`str`
        The capsule type,
    """

    __slots__ = (
        "id",
        "reuse_count",
        "water_landings",
        "last_update",
        "launches",
        "serial",
        "status",
        "type",
    )

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
