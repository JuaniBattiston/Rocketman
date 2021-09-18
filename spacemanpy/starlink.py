class SpaceTrack():

    __slots__ = (
        "info",
        "CCSDS_OMM_VERS",
        "COMMENT",
        "CREATION_DATE",
        "ORIGINATOR",
        "OBJECT_NAME",
        "OBJECT_ID",
        "CENTER_NAME",
        "REF_FRAME",
        "TIME_SYSTEM",
        "MEAN_ELEMENT_THEORY",
        "EPOCH",
        "MEAN_MOTION",
        "ECCENTRICITY",
        "INCLINATION",
        "RA_OF_ASC_NODE",
        "ARG_OF_PERICENTER",
        "MEAN_ANOMALY",
        "EPHEMERIS_TYPE",
        "CLASSIFICATION_TYPE",
        "NORAD_CAT_ID",
        "ELEMENT_SET_NO",
        "REV_AT_EPOCH",
        "BSTAR",
        "MEAN_MOTION_DOT",
        "MEAN_MOTION_DDOT",
        "SEMIMAJOR_AXIS",
        "PERIOD",
        "APOAPSIS",
        "PERIAPSIS",
        "OBJECT_TYPE",
        "RCS_SIZE",
        "COUNTRY_CODE",
        "LAUNCH_DATE",
        "SITE",
        "DECAY_DATE",
        "DECAYED",
        "FILE",
        "GP_ID",
        "TLE_LINE0",
        "TLE_LINE1",
        "TLE_LINE2"
    )

    def __init__(self, info) -> None:
        self.info = info
        self.CCSDS_OMM_VERS = info["CCSDS_OMM_VERS"]
        self.COMMENT = info["COMMENT"]
        self.CREATION_DATE = info["CREATION_DATE"]
        self.ORIGINATOR = info["ORIGINATOR"]
        self.OBJECT_NAME = info["OBJECT_NAME"]
        self.OBJECT_ID = info["OBJECT_ID"]
        self.CENTER_NAME = info["CENTER_NAME"]
        self.REF_FRAME = info["REF_FRAME"]
        self.TIME_SYSTEM = info["TIME_SYSTEM"]
        self.MEAN_ELEMENT_THEORY = info["MEAN_ELEMENT_THEORY"]
        self.EPOCH = info["EPOCH"]
        self.MEAN_MOTION = info["MEAN_MOTION"]
        self.ECCENTRICITY = info["ECCENTRICITY"]
        self.INCLINATION = info["INCLINATION"]
        self.RA_OF_ASC_NODE = info["RA_OF_ASC_NODE"]
        self.ARG_OF_PERICENTER = info["ARG_OF_PERICENTER"]
        self.MEAN_ANOMALY = info["MEAN_ANOMALY"]
        self.EPHEMERIS_TYPE = info["EPHEMERIS_TYPE"]
        self.CLASSIFICATION_TYPE = info["CLASSIFICATION_TYPE"]
        self.NORAD_CAT_ID = info["NORAD_CAT_ID"]
        self.ELEMENT_SET_NO = info["ELEMENT_SET_NO"]
        self.REV_AT_EPOCH = info["REV_AT_EPOCH"]
        self.BSTAR = info["BSTAR"]
        self.MEAN_MOTION_DOT = info["MEAN_MOTION_DOT"]
        self.MEAN_MOTION_DDOT = info["MEAN_MOTION_DDOT"]
        self.SEMIMAJOR_AXIS = info["SEMIMAJOR_AXIS"]
        self.PERIOD = info["PERIOD"]
        self.APOAPSIS = info["APOAPSIS"]
        self.PERIAPSIS = info["PERIAPSIS"]
        self.OBJECT_TYPE = info["OBJECT_TYPE"]
        self.RCS_SIZE = info["RCS_SIZE"]
        self.COUNTRY_CODE = info["COUNTRY_CODE"]
        self.LAUNCH_DATE = info["LAUNCH_DATE"]
        self.SITE = info["SITE"]
        self.DECAY_DATE = info["DECAY_DATE"]
        self.DECAYED = info["DECAYED"]
        self.FILE = info["FILE"]
        self.GP_ID = info["GP_ID"]
        self.TLE_LINE0 = info["TLE_LINE0"]
        self.TLE_LINE1 = info["TLE_LINE1"]
        self.TLE_LINE2 = info["TLE_LINE2"]


class Starlink():

    __slots__ = (
        "response",
        "id"
    )

    def __init__(self, response) -> None:
        self.response = response
        self.id = response["id"]

    @property
    def space_track_info(self):
        """
        Returns satelite updated info provided by space track
        """
        return SpaceTrack(self.response["spaceTrack"])

    @property
    def version(self) -> str:
        """
        Returns satelite's version
        """
        return self.response["version"]

    @property
    def launch(self) -> str:
        """
        Returns satelite's deployement mission
        """
        return self.response["launch"]

    @property
    def longitude(self) -> float:
        """
        Returns satelite's longitude
        """
        return self.response["longitude"]

    @property
    def latitude(self) -> float:
        """
        Returns satelite's latitude
        """
        return self.response["latitude"]

    @property
    def height(self) -> float:
        """
        Returns satelite's height in km
        """
        return self.response["height"]

    @property
    def velocity(self) -> float:
        """
        Returns satelite's velocity in kms
        """
        return self.response["velocity"]