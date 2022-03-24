from rocketman.types.common import (
    MassType,
    MeasurementType,
    ThrustType,
    VolumeType,
    WeightType,
)
from rocketman.utils.objects import BaseClass


class Mass(BaseClass):

    """
    Represents the mass of an object.

    Attributes
    ----------
    kg: Union[:class:`int`, None]
        The mass in kg.
    lb: Union[:class:`int`, None]
        The mass in lb.
    """

    __slots__ = (
        "kg",
        "lb",
    )

    def __init__(self, data: MassType) -> None:
        self._objects = {}
        self._update(data)


class Weight(BaseClass):

    """
    Represents the weight of an object.

    Attributes
    ----------
    id: Optional[:class:`str`]
        *Used only with payloads* ID of the payload.
    kg: Union[:class:`int`, None]
        The mass in kg.
    lb: Union[:class:`int`, None]
        The mass in lb.
    name: Optional[:class:`str`]
        *Used only with payloads* Name of the payload.
    """

    __slots__ = (
        "id",
        "kg",
        "lb",
        "name",
    )

    def __init__(self, data: WeightType) -> None:
        self._objects = {}
        self._update(data)


class Volume(BaseClass):

    """
    Represents the volume of an object.

    Attributes
    ----------
    cubic_meters: Union[:class:`int`, None]
        The volume in cubic meters.
    cubic_feet: Union[:class:`int`, None]
        The volume in cubic feet.
    """

    __slots__ = (
        "cubic_meters",
        "cubic_feet",
    )

    def __init__(self, data: VolumeType) -> None:
        self._objects = {}
        self._update(data)


class Measurement(BaseClass):

    """
    Represents measurements of an object.

    Attributes
    ----------
    meters: Union[:class:`int`, None]
        The measurement in meters.
    feet: Union[:class:`int`, None]
        The measurement in feet.
    """

    __slots__ = (
        "feet",
        "meters",
    )

    def __init__(self, data: MeasurementType) -> None:
        self._objects = {}
        self._update(data)


class Thrust(BaseClass):

    """
    Represents Thrust of an engine.

    Attributes
    ----------
    kN: Union[:class:`float`, None]
        The thrust in kN.
    lbf: Union[:class:`int`, None]
        The thrust in lbf.
    """

    __slots__ = (
        "kN",
        "lbf",
    )

    def __init__(self, data: ThrustType) -> None:
        self._objects = {}
        self._update(data)
