from rocketman.common import BaseClass, Mass, Measurement, Thrust, Weight
from rocketman.types.rocket import (
    EngineType,
    LandingLegType,
    RocketData,
    StageType,
    LandingLegType,
    EngineType,
    StageType,
)


class Stage(BaseClass):

    """
    Represents a Stage.

    Attributes
    ----------
    burn_time: Union[:class:`int`, None]
        Landing leg's material.
    engines: :class:`int`
        Landing leg's number.
    fuel_amount_tons: :class:`int`
        Landing leg's number.
    reusable: :class:`bool`
        Landing leg's number.
    thrust_sea_level: :class:`Thrust`
        Landing leg's number.
    thrust_vacuum: :class:`Thrust`
        Landing leg's number.
    payloads: Optional[Union[:class:`Dict`, None]]
        Landing leg's number.
    option_1: Optional[Union[:class:`str`, None]]
        Landing leg's number.
    thrust: Union[:class:`str`, None]
        Landing leg's number.
    """

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

    """
    Represents an Engine.

    Attributes
    ----------
    engine_loss_max: Union[:class:`int`, None]
        Engine's max loss.
    isp: Dict[:class:`str`, :class:`int`]
        Engine's isp.
    layout: Union[:class:`str`, None]
        Engine's layout.
    number: :class:`int`
        Engine's number.
    propellant_1: :class:`str`
        Engine's first propellant.
    propellant_2: :class:`str`
        Engine's second propellant.
    thrust_sea_level: :class:`Thrust`
        Engine's thrust at sea level.
    thrust_to_weight: :class:`int`
        Engine's thrust to weight ratio.
    thrust_vacuum: :class:`Thrust`
        Engine's thrust in vacuum.
    type: :class:`str`
        Engine's type.
    version: :class:`str`
        Engine's version.
    """

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

    """
    Represents a Landing Leg.

    Attributes
    ----------
    material: :class:`str`
        Landing leg's material.
    number: :class:`int`
        Landing leg's number.
    """

    __slots__ = (
        "material",
        "number",
    )

    def __init__(self, data: LandingLegType) -> None:
        self._objects = {}
        self._update(data)


class Rocket(BaseClass):

    """
    Represents a Rocket.

    Attributes
    ----------
    id: :class:`str`
        Rockets's ID.
    height: :class:`Measurement`
        Rockets's measurement.
    diameter: :class:`Measurement`
        Rockets's diameter.
    mass: :class:`Mass`
        Rockets's mass.
    first_stage: :class:`Stage`
        Rockets's first stage.
    second_stage: :class:`Stage`
        Rockets's second stage.
    engines: :class:`Engine`
        Rockets's engines.
    landing_legs: :class:`LandingLeg`
        Rockets's landing legs.
    payload_weights: List[:class:`Weight`]
        Rockets's payload weights.
    flickr_images: List[:class:`str`]
        Rockets's flickr images.
    name: :class:`str`
        Rockets's name.
    type: :class:`str`
        Rockets's type.
    active: :class:`bool`
        Rockets's activity state.
    stages: :class:`int`
        Rockets's stages.
    boosters: :class:`int`
        Rockets's boosters.
    cost_per_launch: :class:`int`
        Rockets's cost per launch.
    success_rate_pct: :class:`int`
        Rockets's success rate.
    first_flight: :class:`str`
        Rockets's first flight
    country: :class:`str`
        Rockets's country.
    company: :class:`str`
        Rockets's company.
    wikipedia: :class:`str`
        Rockets's wikipedia page.
    description: :class:`str`
        Rockets's description.
    """

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
