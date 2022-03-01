from typing import TypedDict, Union


class SpaceTrackData(TypedDict):
    APOAPSIS: float
    ARG_OF_PERICENTER: float
    BSTAR: float
    CCSDS_OMM_VERS: str
    CENTER_NAME: str
    CLASSIFICATION_TYPE: str
    COMMENT: str
    COUNTRY_CODE: str
    CREATION_DATE: str
    DECAYED: int
    DECAY_DATE: Union[int, None]
    ECCENTRICITY: float
    ELEMENT_SET_NO: int
    EPHEMERIS_TYPE: int
    EPOCH: str
    FILE: int
    GP_ID: int
    INCLINATION: float
    LAUNCH_DATE: str
    MEAN_ANOMALY: float
    MEAN_ELEMENT_THEORY: str
    MEAN_MOTION: float
    MEAN_MOTION_DDOT: int
    MEAN_MOTION_DOT: float
    NORAD_CAT_ID: int
    OBJECT_ID: str
    OBJECT_NAME: str
    OBJECT_TYPE: str
    ORIGINATOR: str
    PERIAPSIS: float
    PERIOD: float
    RA_OF_ASC_NODE: float
    RCS_SIZE: Union[int, None]
    REF_FRAME: str
    REV_AT_EPOCH: int
    SEMIMAJOR_AXIS: float
    SITE: str
    TIME_SYSTEM: str
    TLE_LINE0: str
    TLE_LINE1: str
    TLE_LINE2: str


class StarlinkData(TypedDict):
    id: str
    spacetrack: SpaceTrackData
    height_km: float
    latitude: float
    launch: str
    longitude: float
    velocity_kms: float
    version: str
