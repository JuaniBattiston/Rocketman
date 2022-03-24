from .types.starlink import StarlinkData, SpaceTrackData
from .utils.objects import BaseClass


class SpaceTrack(BaseClass):

    """
    Represents Starlink info provided by Spacetrack.

    Attributes
    ----------
    apoapsis :class:`float`
    arg_of_pericenter: :class:`float`
    bstar: :class:`float`
    ccsds_omm_vers: :class:`str`
    center_name: :class:`str`
    classification_type: :class:`str`
    comment: :class:`str`
    country_code: :class:`str`
    creation_date: :class:`str`
    decayed: :class:`int`
    decay_date: Union[:class:`int`, None]
    eccentricity: :class:`float`
    element_set_no: :class:`int`
    ephemeris_type: :class:`int`
    epoch: :class:`str`
    file: :class:`int`
    gp_id: :class:`int`
    inclination: :class:`float`
    launch_date: :class:`str`
    mean_anomaly: :class:`float`
    mean_element_theory: :class:`str`
    mean_motion: :class:`float`
    mean_motion_ddot: :class:`int`
    mean_motion_dot: :class:`float`
    norad_cat_id: :class:`int`
    object_id: :class:`str`
    object_name: :class:`str`
    object_type: :class:`str`
    originator: :class:`str`
    periapsis: :class:`float`
    period: :class:`float`
    ra_of_asc_node: :class:`float`
    rcs_size: Union[:class:`int`, None]
    ref_frame: :class:`str`
    rev_at_epoch: :class:`int`
    semimajor_axis: :class:`float`
    site: :class:`str`
    time_system: :class:`str`
    tle_line0: :class:`str`
    tle_line1: :class:`str`
    tle_line2: :class:`str`

    """

    __slots__ = (
        "apoapsis",
        "arg_of_pericenter",
        "bstar",
        "ccsds_omm_vers",
        "center_name",
        "classification_type",
        "comment",
        "country_code",
        "creation_date",
        "decayed",
        "decay_date",
        "eccentricity",
        "element_set_no",
        "ephemeris_type",
        "epoch",
        "file",
        "gp_id",
        "inclination",
        "launch_date",
        "mean_anomaly",
        "mean_element_theory",
        "mean_motion",
        "mean_motion_ddot",
        "mean_motion_dot",
        "norad_cat_id",
        "object_id",
        "object_name",
        "object_type",
        "originator",
        "periapsis",
        "period",
        "ra_of_asc_node",
        "rcs_size",
        "ref_frame",
        "rev_at_epoch",
        "semimajor_axis",
        "site",
        "time_system",
        "tle_line0",
        "tle_line1",
        "tle_line2",
    )

    def __init__(self, data: SpaceTrackData) -> None:
        self._objects = {}
        self._update(data)


class Starlink(BaseClass):

    """
    Represents a Starlink satelite.

    Attributes
    ----------
    id: :class:`str`
        Starlink's ID.
    spacetrack: :class:`SpaceTrack`
        Starlink's spacetrack info.
    height_km: :class:`float`
        Starlink's height in km.
    latitude: :class:`float`
        Starlink's latitude.
    longitude: :class:`float`
        Starlink's longitude.
    launch: :class:`str`
        Starlink's launch.
    velocity_kms: :class:`float`
        Starlink's velocity in kms.
    version: :class:`str`
        Starlink's version.
    """

    __slots__ = (
        "id",
        "spacetrack",
        "height_km",
        "latitude",
        "launch",
        "longitude",
        "velocity_kms",
        "version",
    )

    def __init__(self, data: StarlinkData) -> None:
        self._objects = {"spaceTrack": SpaceTrack}
        self._update(data)

    def __repr__(self) -> str:
        attrs = {
            "id": self.id,
            "version": self.version,
        }
        info = " ".join(f"{k}={v}" for k, v in attrs.items())
        return f"<{__class__.__name__} {info}>"
