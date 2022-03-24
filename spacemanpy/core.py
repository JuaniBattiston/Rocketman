from spacemanpy.types.core import CoreData
from spacemanpy.utils.objects import BaseClass


class Core(BaseClass):

    """
    Represents a Core.

    Attributes
    ----------
    id: :class:`str`
        The core ID.
    block: :class:`int`
        The core block number.
    reuse_count: :class:`int`
        The amount of reuses.
    rtls_attempts: :class:`int`
        The amount of RTLS attempts.
    asds_landings: :class:`int`
        The amount of ASDS attempts.
    last_update: :class:`str`
        The last official update on the core.
    launches: List[:class:`str`]
        A list of launches IDS in which the core participated.
    serial: :class:`str`
        The core's serial.
    status: :class:`str`
        The core's status.
    """

    __slots__ = (
        "id",
        "block",
        "reuse_count",
        "rtls_attempts",
        "asds_landings",
        "last_update",
        "launches",
        "serial",
        "status",
    )

    def __init__(self, data: CoreData):
        self._objects = {}
        self._update(data)

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
