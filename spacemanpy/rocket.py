from spacemanpy.common import BaseClass, Mass, Measurement, Thrust, Weight
from spacemanpy.types.rocket import (
    EngineType,
    LandingLegType,
    RocketData,
    StageType,
    LandingLegType,
    EngineType,
    StageType,
)


class Stage(BaseClass):
    def __init__(self, data: StageType) -> None:
        self._objects = {"thrust_sea_level": Thrust, "thrust_vacuum": Thrust}
        self._update(data)


class Engine(BaseClass):
    def __init__(self, data: EngineType) -> None:
        self._objects = {"thrust_sea_level": Thrust, "thrust_vacuum": Thrust}
        self._update(data)


class LandingLeg(BaseClass):
    def __init__(self, data: LandingLegType) -> None:
        self._update(data)


class Rocket(BaseClass):
    def __init__(self, data: RocketData):
        self._objects = {
            "height": Measurement,
            "diameter": Measurement,
            "mass": Mass,
            "first_stage": Stage,
            "second_stage": Stage,
            "engines": Engine,
            "landing_legs": LandingLeg,
            "payload_weights": Weight,
        }
        self._update(data)
        # print(data)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        attrs = {
            "id": self.id,
            "name": self.name,
            "type": self.type,
        }
        info = " ".join(f"{k}={v}" for k, v in attrs.items())
        return f"<{__class__.__name__} {info}>"
