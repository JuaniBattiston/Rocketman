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

    __slots__ = (
        "burn_time",
        "engines",
        "fuel_amount_tons",
        "reusable",
        "thrust_sea_level",
        "thrust_vacuum",
        "payloads",
        "option_1",
        "thrust",
    )

    def __init__(self, data: StageType) -> None:
        self._objects = {"thrust_sea_level": Thrust, "thrust_vacuum": Thrust}
        self._update(data)


class Engine(BaseClass):

    __slots__ = (
        "engine_loss_max",
        "isp",
        "layout",
        "number",
        "propellant_1",
        "propellant_2",
        "thrust_sea_level",
        "thrust_to_weight",
        "thrust_vacuum",
        "type",
        "version",
    )

    def __init__(self, data: EngineType) -> None:
        self._objects = {"thrust_sea_level": Thrust, "thrust_vacuum": Thrust}
        self._update(data)


class LandingLeg(BaseClass):

    __slots__ = (
        "material",
        "number",
    )

    def __init__(self, data: LandingLegType) -> None:
        self._objects = {}
        self._update(data)


class Rocket(BaseClass):

    __slots__ = (
        "id",
        "height",
        "diameter",
        "mass",
        "first_stage",
        "second_stage",
        "engines",
        "landing_legs",
        "payload_weights",
        "flickr_images",
        "name",
        "type",
        "active",
        "stages",
        "boosters",
        "cost_per_launch",
        "success_rate_pct",
        "first_flight",
        "country",
        "company",
        "wikipedia",
        "description",
    )

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
