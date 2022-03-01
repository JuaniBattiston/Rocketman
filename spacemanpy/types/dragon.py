from typing import List, TypedDict
from spacemanpy.types.common import (
    VolumeType,
    ThrustType,
    MassType,
    MeasurementType,
)


class HeatShield(TypedDict):
    material: str
    size: float
    temp_degrees: int
    dev_partner: str


class Cargo(TypedDict):
    solar_array: int
    unpressurized_cargo: bool


class Trunk(TypedDict):
    cargo: Cargo
    trunk_volume: VolumeType


class Thruster(TypedDict):
    amount: int
    fuel_1: str
    fuel_2: str
    isp: int
    pods: int
    thrust: ThrustType
    type: str


class DragonData(TypedDict):
    id: str
    heat_shield: HeatShield
    launch_payload_mass: MassType
    launch_payload_vol: VolumeType
    return_payload_mass: MassType
    return_payload_vol: VolumeType
    pressurized_capsule: VolumeType
    trunk: Trunk
    height_w_trunk: MeasurementType
    diamenter: MeasurementType
    first_flight: str
    flickr_images: List[str]
    name: str
    type: str
    active: bool
    crew_capacity: int
    sidewall_angle_deg: int
    orbit_duration_yr: int
    dry_mass_kg: int
    dry_mass_lb: int
    thrusters: List[Thruster]
    wikipedia: str
    description: str
