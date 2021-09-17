class Payload():

    __slots__ = (
        "response",
        "id"
    )

    def __init__(self, response):
        self.response = response
        self.id = response["id"]

    @property
    def dragon(self) -> dict:
        """
        Returns dragon info
        """
        return self.response["dragon"]

    @property
    def name(self) -> str:
        """
        Returns payload name
        """
        return self.response["name"]

    @property
    def payload_type(self) -> str:
        """
        Returns payload type
        """
        return self.response["type"]

    @property
    def reused(self) -> bool:
        """
        Returns reuse state
        """
        return self.response["reused"]

    @property
    def launch(self) -> str:
        """
        Returns launch id related to the payload
        """
        return self.response["launch"]

    @property
    def customers(self) -> list:
        """
        Returns a list of customers
        """
        return self.response["customers"]

    @property
    def nationalities(self) -> list:
        """
        Returns a list of nationalities related to the payload
        """
        return self.response["nationalities"]

    @property
    def mass_kg(self) -> int:
        """
        Returns the mass in kg of the payload
        """
        return self.response["mass_kg"]

    @property
    def mass_lbs(self) -> float:
        """
        Returns the mass in lbs of the payload
        """
        return self.response["mass_lbs"]

    @property
    def orbit(self) -> str:
        """
        Returns orbit type
        """
        return self.response["orbit"]

    @property
    def reference_system(self) -> str:
        """
        Returns orbit's reference system
        """
        return self.response["reference_system"]

    @property
    def regime(self) -> str:
        """
        Returns orbit's regime system
        """
        return self.response["regime"]

    @property
    def longitude(self):
        """
        Returns longitude
        """
        return self.response["longitude"]

    @property
    def semi_major_axis(self) -> float:
        """
        Returns orbit's semi major axis in km
        """
        return self.response["semi_major_axis_km"]

    @property
    def eccentricity(self) -> float:
        """
        Returns orbit's eccentricity
        """
        return self.response["eccentricity"]

    @property
    def periapsis(self) -> float:
        """
        Returns orbit's periapsis in km
        """
        return self.response["periapsis_km"]

    @property
    def apoapsis(self) -> float:
        """
        Returns orbit's apoapsis in km
        """
        return self.response["apoapsis_km"]

    @property
    def inclination(self) -> float:
        """
        Returns orbit's inclination in degrees
        """
        return self.response["inclination_deg"]

    @property
    def period_min(self) -> float:
        """
        Returns orbit's period min
        """
        return self.response["period_min"]

    @property
    def lifespan_years(self) -> int:
        """
        Returns payload's lifetime
        """
        return self.response["lifespan_years"]

    @property
    def epoch(self) -> str:
        """
        Returns epoch
        """
        return self.response["epoch"]

    @property
    def mean_motion(self) -> float:
        """
        Returns mean motion
        """
        return self.response["mean_motion"]

    @property
    def raan(self) -> float:
        """
        Returns raan
        """
        return self.response["raan"]

    @property
    def arg_of_pericenter(self) -> float:
        """
        Returns arg of pericenter
        """
        return self.response["arg_of_pericenter"]

    @property
    def mean_anomaly(self) -> float:
        """
        Returns mean anomaly
        """
        return self.response["mean_anomaly"]