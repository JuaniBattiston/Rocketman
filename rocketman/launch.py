from rocketman.types.launch import FailureData, FairingData, LaunchData
from rocketman.utils.objects import BaseClass


class Fairing(BaseClass):

    """
    Represents a fairing.

    Attributes
    ----------
    recovered: :class:`bool`
        Returns bool stating state of recovery.
    recovery_attempt: :class:`bool`
        Returns bool stating if recovery was attempted.
    reused: :class:`int`
        Returns bool stating if fairing was reused.
    ships: List[:class:`int`]
        A list of IDs in which the fairing took part.
    """

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

    """
    Represents a launch failure.

    Attributes
    ----------
    time: Union[:class:`int`, None]
        Time of failure.
    altitude: Union[:class:`float`, None]
        Failure altitude.
    reason: Union[:class:`str`, None]
        Reason of failure.
    """

    __slots__ = (
        "time",
        "altitude",
        "reason",
    )

    def __init__(self, data: FailureData):
        self._objects = {}
        self._update(data)


class Launch(BaseClass):

    """
    Represents a launch.

    Attributes
    ----------
    id: :class:`str`
        The launch ID.
    fairings: :class:`Fairing`
        The launch fairing.
    links: :class:`Dict`
        Launch links.
    static_fire_date_utc: :class:`str`
        Static fire date in UTC.
    static_fire_date_utc: :class:`int`
        Static fire date in unix time.
    net: :class:`bool`
        Returns bool stating if a net was used.
    window: :class:`int`
        Returns launch window.
    rocket: :class:`str`
        The rockets ID.
    success: :class:`bool`
        Returns bool stating if launch was a success.
    failures: List[:class:`Failure`]
        The launch failures.
    details: :class:`str`
        The launch details.
    crew: List[:class:`str`]
        The crew members ID involved in the launch.
    ships: List[:class:`str`]
        The ships ID involved in the launch.
    capsules: List[:class:`str`]
        The capsules ID involved in the launch.
    payloads: List[:class:`str`]
        The payloads ID involved in the launch.
    launchpad: :class:`str`
        The launch pad ID.
    flight_number: :class:`int`
        The flight number.
    name: :class:`str`
        The flight name.
    date_utc: :class:`str`
        The flight date in UTC.
    date_unix: :class:`int`
        The flight date in UNIX time.
    date_local: :class:`str`
        The flight date in local time.
    tbd: :class:`bool`
        Returns bool stating if launch date is tbd.
    launch_library_id: Union[:class:`str`, None]
        The launch library ids.
    """

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
