from spacemanpy.types.landingpad import LandingPadData
from spacemanpy.utils.objects import BaseClass


class LandingPad(BaseClass):

    """
    Represents a landing pad.

    Attributes
    ----------
    id: :class:`str`
        The landing pad's ID.
    images: Dict[:class:`str`, List[:class:`str`]]
        Landing pad's images.
    name: :class:`str`
        The landing pad's name.
    full_name: :class:`str`
        The landing pad's full name.
    status: :class:`str`
        The landing pad's status
    type: :class:`str`
        The landing pad's type.
    locality: :class:`str`
        The landing pad's locality.
    region: :class:`str`
        The landing pad's region.
    latitude: :class:`bool`
        The landing pad's latitude.
    longitud: :class:`bool`
        The landing pad's longitude.
    landing_attempts: :class:`int`
        The ammount of landing attempts.
    landing_attempts: :class:`int`
        The ammount of successful landing attempts.
    wikipedia: :class:`str`
        The landing pad's wikipedia page.
    details: :class:`str`
        The landing pad's details.
    launches: List[:class:`str`]
        The launches in which landing pad's was used.
    """

    __slots__ = (
        "id",
        "images",
        "name",
        "full_name",
        "status",
        "type",
        "locality",
        "region",
        "latitude",
        "longitude",
        "landing_attempts",
        "landing_successes",
        "wikipedia",
        "details",
        "launches",
    )

    def __init__(self, data: LandingPadData):
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
