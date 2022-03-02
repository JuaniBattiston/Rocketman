from spacemanpy.types.common import (
    MassType,
    MeasurementType,
    ThrustType,
    VolumeType,
    WeightType,
)
from spacemanpy.utils.objects import BaseClass


class Mass(BaseClass):

    __slots__ = (
        "kg",
        "lb",
    )

    def __init__(self, data: MassType) -> None:
        self._objects = {}
        self._update(data)


class Weight(BaseClass):

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

    __slots__ = (
        "cubic_meters",
        "cubic_feet",
    )

    def __init__(self, data: VolumeType) -> None:
        self._objects = {}
        self._update(data)


class Measurement(BaseClass):

    __slots__ = (
        "feet",
        "meters",
    )

    def __init__(self, data: MeasurementType) -> None:
        self._objects = {}
        self._update(data)


class Thrust(BaseClass):

    __slots__ = (
        "kN",
        "lbf",
    )

    def __init__(self, data: ThrustType) -> None:
        self._objects = {}
        self._update(data)
