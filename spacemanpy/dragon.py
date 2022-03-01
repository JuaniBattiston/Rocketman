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
    def __init__(self, data: HeatShieldData):
        self._objects = {}
        self._update(data)


class Cargo(BaseClass):
    def __init__(self, data: CargoData):
        self._objects = {}
        self._update(data)


class Trunk(BaseClass):
    def __init__(self, data: TrunkData):
        self._objects = {"cargo": Cargo}
        self._update(data)


class Thruster(BaseClass):
    def __init__(self, data: ThrusterData):
        self._objects = {}
        self._update(data)


class Dragon(BaseClass):
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
