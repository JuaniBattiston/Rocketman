from typing import Dict, List, TypedDict, Union
from spacemanpy.types.common import (
    ThrustType,
    MeasurementType,
    WeightType,
    MassType,
)


class StageType(TypedDict):
    burn_time: Union[int, None]
    engines: int
    fuel_amount_tons: int
    reusable: bool
    thrust_sea_level: ThrustType
    thrust_vacuum: ThrustType
    payloads: Union[Dict, None]
    option_1: Union[str, None]
    thrust: Union[str, None]


class EngineType(TypedDict):
    engine_loss_max: Union[int, None]
    isp: Dict[str, int]
    layout: Union[str, None]
    number: int
    propellant_1: str
    propellant_2: str
    thrust_sea_level: ThrustType
    thrust_to_weight: int
    thrust_vacuum: ThrustType
    type: str
    version: str


class LandingLegType(TypedDict):
    material: str
    number: int


class RocketData(TypedDict):
    id: str
    height: MeasurementType
    diameter: MeasurementType
    mass: MassType
    first_stage: StageType
    second_stage: StageType
    engines: EngineType
    landing_legs: LandingLegType
    payload_weights: List[WeightType]
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
