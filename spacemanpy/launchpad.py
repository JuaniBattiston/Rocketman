from spacemanpy.types.launchpad import LaunchPadData
from spacemanpy.utils.objects import BaseClass


class LaunchPad(BaseClass):

    """
    Represents a launch pad.

    Attributes
    ----------
    id: :class:`str`
        The launch pad's ID.
    images: Dict[:class:`str`, List[:class:`str`]]
        Launch pad's images.
    name: :class:`str`
        The launch pad's name.
    full_name: :class:`str`
        The launch pad's full name.
    status: :class:`str`
        The launch pad's status
    locality: :class:`str`
        The launch pad's locality.
    region: :class:`str`
        The launch pad's region.
    latitude: :class:`bool`
        The launch pad's latitude.
    longitud: :class:`bool`
        The launch pad's longitude.
    launch_attempts: :class:`int`
        The ammount of launch attempts.
    launch_attempts: :class:`int`
        The ammount of successful launch attempts.
    rockets: List[:class:`str`]
        The list of rockets IDs.
    timezone: :class:`str`
        The launch pad's timezone.
    launches: List[:class:`str`]
        The launches in which launch pad's was used.
    details: :class:`str`
        The launch pad's details.
    """

    __slots__ = (
        "id",
        "images",
        "name",
        "full_name",
        "locality",
        "region",
        "latitude",
        "longitud",
        "launch_attempts",
        "launch_successes",
        "rockets",
        "timezone",
        "launches",
        "status",
        "details",
    )

    def __init__(self, data: LaunchPadData):
        self._objects = {}
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
