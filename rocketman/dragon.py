from rocketman.common import Mass, Measurement, Volume
from rocketman.types.dragon import (
    CargoData,
    DragonData,
    HeatShieldData,
    ThrusterData,
    TrunkData,
)
from rocketman.utils.objects import BaseClass


class HeatShield(BaseClass):

    """
    Represents a heat shield.

    Attributes
    ----------
    material: :class:`str`
        The heat shield material.
    size: :class:`float`
        The heat shield's size.
    temp_degrees: :class:`int`
        The max temperature.
    dev_partner: :class:`int`
        The heat shield dev partner.
    """

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

    """
    Represents dragon cargo.

    Attributes
    ----------
    solar_array: :class:`int`
        The amount of solar arrays in dragon.
    unpressurized_cargo: :class:`bool`
        Bool value stating if cargo in pressurised or not.
    """

    __slots__ = (
        "solar_array",
        "unpressurized_cargo",
    )

    def __init__(self, data: CargoData):
        self._objects = {}
        self._update(data)


class Trunk(BaseClass):

    """
    Represents dragon trunk.

    Attributes
    ----------
    cargo: :class:`Cargo`
        Dragon cargo.
    trunk_volume: :class:`Volume`
        The trunk's volume.
    """

    __slots__ = (
        "cargo",
        "trunk_volume",
    )

    def __init__(self, data: TrunkData):
        self._objects = {"cargo": Cargo}
        self._update(data)


class Thruster(BaseClass):

    """
    Represents dragon thrusters.

    Attributes
    ----------
    amount: :class:`int`
        The amount of thrusters.
    fuel_1: :class:`str`
        Fuel type 1.
    fuel_2: :class:`str`
        Fuel type 2.
    isp: :class:`int`
        Dragon's isp.
    pods: :class:`int`
        Dragon's pods.
    thrust: :class:`Thrust`
        The thruster thrust.
    type: :class:`str`
        The thruster type.
    """

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

    """
    Represents a Dragon capsule.

    Attributes
    ----------
    id: :class:`str`
        The dragon's ID.
    heat_shield: :class:`HeatShield`
        The dragon's heat shield.
    launch_payload_mass: :class:`Mass`
        The payload mass at launch.
    launch_payload_vol: :class:`Volume`
        The payload volume at launch.
    return_payload_mass: :class:`Mass`
        The payload mass when returning.
    return_payload_vol: :class:`Volume`
        The payload volume when returning.
    pressurized_capsule: :class:`Volume`
        The pressurized capsule volume.
    trunk: :class:`Trunk`
        The dragon's trunk.
    height_w_trunk: :class:`Measurement`
        The dragon's height with trunk.
    diamenter: :class:`Measurement`
        The dragon's diameter.
    first_flight: :class:`str`
        The dragon's first flight id.
    flickr_images: List[:class:`str`]
        A list of capsule images.
    name: class:`str`
        The dragon's name.
    type: class:`str`
        The dragon's type.
    active: class:`bool`
        The dragon's status.
    crew_capacity: class:`int`
        The dragon's crew capacity.
    sidewall_angle_deg: class:`int`
        The dragon's sidewall angle in degrees.
    orbit_duration_yr: class:`int`
        The dragon's orbit duration.
    dry_mass_kg: class:`int`
        The dragon's dry mass in kg.
    dry_mass_lb: class:`int`
        The dragon's dry mass in lb.
    thrusters: List[class:`Thruster`]
        The dragon's thrusters.
    wikipedia: class:`str`
        The dragon's wikipedia page.
    wikipedia: class:`str`
        The dragon's description.
    """

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
