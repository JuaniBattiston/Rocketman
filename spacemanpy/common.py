from spacemanpy.types.common import (
    MassType,
    MeasurementType,
    ThrustType,
    VolumeType,
    WeightType,
)
from spacemanpy.utils.objects import BaseClass


class Mass(BaseClass):
    def __init__(self, data: MassType) -> None:
        self._objects = {}
        self._update(data)


class Weight(BaseClass):
    def __init__(self, data: WeightType) -> None:
        self._objects = {}
        self._update(data)


class Volume(BaseClass):
    def __init__(self, data: VolumeType) -> None:
        self._objects = {}
        self._update(data)


class Measurement(BaseClass):
    def __init__(self, data: MeasurementType) -> None:
        self._objects = {}
        self._update(data)


class Thrust(BaseClass):
    def __init__(self, data: ThrustType) -> None:
        self._objects = {}
        self._update(data)
