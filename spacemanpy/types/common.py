from typing import TypedDict, Union


class MassType(TypedDict):
    kg: Union[int, None]
    lb: Union[int, None]


class WeightType(TypedDict):
    id: str
    kg: int
    lb: int
    name: str


class VolumeType(TypedDict):
    cubic_meters: Union[int, None]
    cubic_feet: Union[int, None]


class MeasurementType(TypedDict):
    feet: Union[int, None]
    meters: Union[int, None]


class ThrustType(TypedDict):
    kN: Union[float, None]
    lbf: Union[int, None]
