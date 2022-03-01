from typing import Dict, List, TypedDict, Union
from spacemanpy.types.common import (
    Thrust,
    Measurement,
    Weight,
    Mass,
)


class Stage(TypedDict):
    burn_time: Union[int, None]
    engines: int
    fuel_amount_tons: int
    reusable: bool
    thrust_sea_level: Thrust
    thrust_vacuum: Thrust
    payloads: Union[Dict, None]
    option_1: Union[str, None]
    thrust: Union[str, None]


class Engine(TypedDict):
    engine_loss_max: Union[int, None]
    isp: Dict[str, int]
    layout: Union[str, None]
    number: int
    propellant_1: str
    propellant_2: str
    thrust_sea_level: Thrust
    thrust_to_weight: int
    thrust_vacuum: Thrust
    type: str
    version: str


class LandingLeg(TypedDict):
    material: str
    number: int


class RocketData(TypedDict):
    id: str
    height: Measurement
    diameter: Measurement
    mass: Mass
    first_stage: Stage
    second_stage: Stage
    engines: Engine
    landing_legs: LandingLeg
    payload_weights: List[Weight]
    flickr_images: List[str]
    name: str
    type: str
    active: bool
    stages: int
    boosters: int
    cost_per_launch: int
    success_rate_pct: int
    first_flight: str
    country: str
    company: str
    wikipedia: str
    description: str
