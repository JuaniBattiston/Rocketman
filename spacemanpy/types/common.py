from typing import Optional, TypedDict, Union


class MassType(TypedDict):
    kg: Union[int, None]
    lb: Union[int, None]


class WeightType(TypedDict):
    id: Optional[str]
    kg: int
    lb: int
    name: Optional[str]


class VolumeType(TypedDict):
    cubic_meters: Union[int, None]
    cubic_feet: Union[int, None]


class MeasurementType(TypedDict):
    meters: Union[int, None]
    feet: Union[int, None]


class ThrustType(TypedDict):
    kN: Union[float, None]
    lbf: Union[int, None]
