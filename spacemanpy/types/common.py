from typing import TypedDict, Union


class Mass(TypedDict):
    kg: Union[int, None]
    lb: Union[int, None]


class Weight(TypedDict):
    id: str
    kg: int
    lb: int
    name: str


class Volume(TypedDict):
    cubic_meters: Union[int, None]
    cubic_feet: Union[int, None]


class Measurement(TypedDict):
    feet: Union[int, None]
    meters: Union[int, None]


class Thrust(TypedDict):
    kN: Union[float, None]
    lbf: Union[int, None]
