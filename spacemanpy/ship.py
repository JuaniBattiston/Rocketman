from spacemanpy.types.ship import ShipData
from spacemanpy.utils.objects import BaseClass


class Ship(BaseClass):

    """
    Represents a Ship.

    Attributes
    ----------
    id: :class:`str`
        Ship's ID.
    last_ais_update: Union[:class:`str`, None]
        Ship's lasr ais update.
    legacy_id: Union[:class:`str`, None]
        Ship's legacy ID.
    model: Union[:class:`str`, None]
        Ship's model.
    type: :class:`str`
        Ship's type.
    roles: List[:class:`str`]
        Ship's roles.
    imo: :class:`int`
        Ship's imo.
    mmsi: :class:`int`
        Ship's mmsi.
    abs: :class:`int`
        Ship's abs.
    _class: :class:`int`
        Ship's class.
    mass_kg: :class:`int`
        Ship's mass in kg.
    mass_lbs: :class:`int`
        Ship's mass in lbs.
    year_built: :class:`int`
        Ship's built year.
    home_port: :class:`str`
        Ship's home port.
    status: Union[:class:`str`, None]
        Ship's status.
    speed_kn: Union[:class:`int`, None]
        Ship's speed.
    course_deg: Union[:class:`int`, None]
        Ship's course degree.
    latitude: Union[:class:`float`, None]
        Ship's latitude.
    longitude: Union[:class:`float`, None]
        Ship's longitude.
    link: :class:`str`
        Ship's link.
    image: :class:`str`
        Ship's image.
    name: :class:`str`
        Ship's name.
    active: :class:`bool`
        Ship's active status.
    launches: List[:class:`str`]
        All ship's launches.
    """

    __slots__ = (
        "id",
        "last_ais_update",
        "legacy_id",
        "model",
        "type",
        "roles",
        "imo",
        "mmsi",
        "abs",
        "_class",
        "mass_kg",
        "mass_lbs",
        "year_built",
        "home_port",
        "status",
        "speed_kn",
        "course_deg",
        "latitude",
        "longitude",
        "link",
        "image",
        "name",
        "active",
        "launches",
    )

    def __init__(self, data: ShipData) -> None:
        self._objects = {}
        self._update(data)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        attrs = {
            "id": self.id,
            "name": self.name,
            "active": self.active,
        }
        info = " ".join(f"{k}={v}" for k, v in attrs.items())
        return f"<{__class__.__name__} {info}>"
