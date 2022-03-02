from spacemanpy.common import Mass, Measurement, Volume
from spacemanpy.types.dragon import (
    CargoData,
    DragonData,
    HeatShieldData,
    ThrusterData,
    TrunkData,
)
from spacemanpy.utils.objects import BaseClass


class HeatShield(BaseClass):

    __slots__ = (
        "material",
        "size",
        "temp_degrees",
        "dev_partner",
    )

    def __init__(self, data: HeatShieldData):
        self._objects = {}
        self._update(data)


class Cargo(BaseClass):

    __slots__ = (
        "solar_array",
        "unpressurized_cargo",
    )

    def __init__(self, data: CargoData):
        self._objects = {}
        self._update(data)


class Trunk(BaseClass):
    __slots__ = (
        "cargo",
        "trunk_volume",
    )

    def __init__(self, data: TrunkData):
        self._objects = {"cargo": Cargo}
        self._update(data)


class Thruster(BaseClass):

    __slots__ = (
        "amount",
        "fuel_1",
        "fuel_2",
        "isp",
        "pods",
        "thrust",
        "type",
    )

    def __init__(self, data: ThrusterData):
        self._objects = {}
        self._update(data)


class Dragon(BaseClass):

    __slots__ = (
        "id",
        "heat_shield",
        "launch_payload_mass",
        "launch_payload_vol",
        "return_payload_mass",
        "return_payload_vol",
        "pressurized_capsule",
        "trunk",
        "height_w_trunk",
        "diamenter",
        "first_flight",
        "flickr_images",
        "name",
        "type",
        "active",
        "crew_capacity",
        "sidewall_angle_deg",
        "orbit_duration_yr",
        "dry_mass_kg",
        "dry_mass_lb",
        "thrusters",
        "wikipedia",
        "description",
    )

    def __init__(self, data: DragonData):
        self._objects = {
            "heat_shield": HeatShield,
            "trunk": Trunk,
            "thrusters": Thruster,
            "launch_payload_mass": Mass,
            "launch_payload_vol": Volume,
            "return_payload_mass": Mass,
            "return_payload_vol": Volume,
            "pressurized_capsule": Volume,
            "height_w_trunk": Measurement,
            "diamenter": Measurement,
        }
        self._update(data)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        attrs = {
            "id": self.id,
            "name": self.name,
        }
        info = " ".join(f"{k}={v}" for k, v in attrs.items())
        return f"<{__class__.__name__} {info}>"
