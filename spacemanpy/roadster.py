from spacemanpy.types.roadster import RoadsterData
from spacemanpy.utils.objects import BaseClass


class Roadster(BaseClass):

    """
    Represents the Roadster.

    Attributes
    ----------
    id: :class:`str`
        Roadster's ID.
    name: :class:`str`
        Roadster's name.
    launch_date_utc: :class:`str`
        Roadster's launch date in utc time.
    launch_date_unix: :class:`int`
        Roadster's launch date in unix.
    launch_mass_kg: :class:`int`
        Roadster's mass in kg.
    launch_mass_lbs: :class:`int`
        Roadster's mass in lbs.
    norad_id: :class:`int`
        Roadster's norad id.
    epoch_jd: :class:`float`
        Roadster's epoch.
    orbit_type: :class:`str`
        Roadster's orbit type.
    apoapsis_au: :class:`float`
        Roadster's apoapsis.
    periapsis_aui: :class:`float`
        Roadster's periapsis.
    semi_major_axis_au: :class:`float`
        Roadster's semi major axis.
    eccentricity: :class:`float`
        Roadster's eccentricity.
    inclination: :class:`float`
        Roadster's inclination.
    longitude: :class:`float`
        Roadster's longitude.
    periapsis_arg: :class:`float`
        Roadster's periapsis arg.
    period_days: :class:`float`
        Roadster's period days.
    speed_kph: :class:`float`
        Roadster's speed in kph.
    speed_mph: :class:`float`
        Roadster's speed in mph.
    earth_distance_km: :class:`float`
        Roadster's earth distance in km.
    earth_distance_mi: :class:`float`
        Roadster's earth distance in mi.
    mars_distance_km: :class:`float`
        Roadster's mars distance in km.
    mars_distance_mi: :class:`float`
        Roadster's mars distance in mi.
    flickr_images: :class:`str`
        Roadster's flickr images list.
    wikipedia: :class:`str`
        Roadster's wikipedia page.
    video: :class:`str`
        Roadster's video.
    details: :class:`str`
        Roadster's details.
    """

    __slots__ = (
        "id",
        "name",
        "launch_date_utc",
        "launch_date_unix",
        "launch_mass_kg",
        "launch_mass_lbs",
        "norad_id",
        "epoch_jd",
        "orbit_type",
        "apoapsis_au",
        "periapsis_au",
        "semi_major_axis_au",
        "eccentricity",
        "inclination",
        "longitude",
        "periapsis_arg",
        "period_days",
        "speed_kph",
        "speed_mph",
        "earth_distance_km",
        "earth_distance_mi",
        "mars_distance_km",
        "mars_distance_mi",
        "flickr_images",
        "wikipedia",
        "video",
        "details",
    )

    def __init__(self, data: RoadsterData):
        self._objects = {}
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
