from .types.payload import PayloadData, DragonPayloadData
from .utils.objects import BaseClass


class DragonPayload(BaseClass):

    """
    Represents Dragon's Payload.

    Attributes
    ----------
    capsule: Union[:class:`str`, None]
        The payload's capsule.
    flight_time_sec: Union[:class:`int`, None]
        The payload's flight time in seconds.
    land_landing: Union[:class:`bool`, None]
        Has the payload done a land landing.
    manifest: Union[:class:`str`, None]
        The payload's manifest.
    mass_returned_kg: Union[:class:`int`, None]
        Payload's mass on return in kg.
    mass_returned_lbs: Union[:class:`int`, None]
        Payload's mass on return in lbs.
    water_landing: Union[:class:`bool`, None]
        Has the payload done a water landing.
    """

    __slots__ = (
        "capsule",
        "flight_time_sec",
        "land_landing",
        "manifest",
        "mass_returned_kg",
        "mass_returned_lbs",
        "water_landing",
    )

    def __init__(self, data: DragonPayloadData):
        self._objects = {}
        self._update(data)


class Payload(BaseClass):

    """
    Represents a Payload.

    Attributes
    ----------
    id: :class:`str`
        The payload ID.
    dragon: :class:`DragonPayload`
        Dragon payload object.
    name: :class:`name`
        The payload's name.
    type: :class:`str`
        The payload's type.
    reused: :class:`bool`
        Payload has been reused.
    launch: :class:`str`
        Payload's launch ID.
    customers: List[:class:`str`]
        Payload's customers list.
    norad_ids: List[:class:`str`]
        Payload's norad ids list.
    nationalities: List[:class:`str`]
        Payload's nationalities list.
    manufacturers: List[:class:`str`]
        Payload's manufacturers list.
    mass_kg: :class:`int`
        Payload's mass in kg.
    mass_lbs: :class:`str`
        Payload's mass in lbs.
    orbit: :class:`str`
        Payload's orbit.
    reference_system: :class:`str`
        Payload's reference system.
    regime: :class:`str`
        Payload's regime.
    longitude: Union[:class:`str`, None]
        Payload's longitude.
    semi_major_axis_km: Union[:class:`str`, None]
        Payload's semi major axis in km.
    eccentricity: Union[:class:`str`, None]
        Payload's eccentricity.
    periapsis_km: :class:`int`
        Payload's periapsis in km.
    apoapsis_km: :class:`int`
        Payload's apoapsis in km.
    inclination_deg: :class:`int`
        Payload's inclination degree.
    period_min: Union[:class:`int`, None]
        Payload's minimum period.
    lifespan_years: Union[:class:`int`, None]
        Payload's lifespan years.
    epoch: Union[:class:`int`, None]
        Payload's epoch.
    mean_motion: Union[:class:`int`, None]
        Payload's mean motion.
    raan: Union[:class:`int`, None]
        Payload's raan.
    arg_of_pericenter: Union[:class:`int`, None]
        Payload's arg of pericenter.
    mean_anomaly: Union[:class:`int`, None]
        Payload's mean anomaly.
    """

    __slots__ = (
        "id",
        "dragon",
        "name",
        "type",
        "reused",
        "launch",
        "customers",
        "norad_ids",
        "nationalities",
        "manufacturers",
        "mass_kg",
        "mass_lbs",
        "orbit",
        "reference_system",
        "regime",
        "longitude",
        "semi_major_axis_km",
        "eccentricity",
        "periapsis_km",
        "apoapsis_km",
        "inclination_deg",
        "period_min",
        "lifespan_years",
        "epoch",
        "mean_motion",
        "raan",
        "arg_of_pericenter",
        "mean_anomaly",
    )

    def __init__(self, data: PayloadData):
        self._objects = {"dragon": DragonPayload}
        self._update(data)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        attrs = {
            "id": self.id,
            "name": self.name,
        }
        info = " ".join(f"{k}={v}" for k, v in attrs.items())
        return f"<{__class__.__name__} {info}>"
