from spacemanpy.types.starlink import StarlinkData, SpaceTrackData
from spacemanpy.utils.objects import BaseClass


class SpaceTrack(BaseClass):

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
