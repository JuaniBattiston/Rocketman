class Roadster():

    __slots__ = (
        "response",
        "id"
    )

    def __init__(self, response):
        self.response = response
        self.id = response["id"]

    @property
    def name(self) -> list:
        """
        Returns roadster images
        """
        return self.response["flickr_images"]

    @property
    def name(self) -> str:
        """
        Returns roadster's name
        """
        return self.response["name"]

    @property
    def launch_date_utc(self) -> str:
        """
        Returns roadster's launch date in utc time
        """
        return self.response["launch_date_utc"]
    
    @property
    def launch_date_unix(self) -> int:
        """
        Returns roadster's launch date in unix time
        """
        return self.response["launch_date_unix"]

    @property
    def launch_mass_kg(self) -> int:
        """
        Returns roadster's launch mass in kg
        """
        return self.response["launch_mass_kg"]

    @property
    def launch_mass_lbs(self) -> int:
        """
        Returns roadster's launch mass in lbs
        """
        return self.response["launch_mass_lbs"]

    @property
    def norad_id(self) -> int:
        """
        Returns roadster's norad id
        """
        return self.response["norad_id"]

    @property
    def epoch_js(self) -> float:
        """
        Returns roadster's epoch js
        """
        return self.response["epoch_js"]

    @property
    def orbit_type(self) -> str:
        """
        Returns roadster's orbit type
        """
        return self.response["orbit_type"]

    @property
    def orbit_type(self) -> str:
        """
        Returns roadster's orbit type
        """
        return self.response["orbit_type"]

    @property
    def apoapsis_au(self) -> float:
        """
        Returns roadster's apoapsis
        """
        return self.response["apoapsis_au"]

    @property
    def periapsis_au(self) -> float:
        """
        Returns roadster's periapsis
        """
        return self.response["periapsis_au"]

    @property
    def semi_major_axis_au(self) -> float:
        """
        Returns roadster's semi major axis
        """
        return self.response["semi_major_axis_au"]

    @property
    def eccentricity(self) -> float:
        """
        Returns roadster's eccentricity
        """
        return self.response["eccentricity"]

    @property
    def inclination(self) -> float:
        """
        Returns roadster's inclination
        """
        return self.response["inclination"]

    @property
    def longitude(self) -> float:
        """
        Returns roadster's longitude
        """
        return self.response["longitude"]

    @property
    def periapsis_arg(self) -> float:
        """
        Returns roadster's periapsis arg
        """
        return self.response["periapsis_arg"]

    @property
    def period_days(self) -> float:
        """
        Returns roadster's period days
        """
        return self.response["period_days"]

    @property
    def speed_kph(self) -> float:
        """
        Returns roadster's speed in kph
        """
        return self.response["speed_kph"]

    @property
    def speed_mph(self) -> float:
        """
        Returns roadster's speed in mph
        """
        return self.response["speed_mph"]

    @property
    def earth_distance_km(self) -> float:
        """
        Returns roadster's earth distance in km
        """
        return self.response["earth_distance_km"]

    @property
    def earth_distance_mi(self) -> float:
        """
        Returns roadster's earth distance in mi
        """
        return self.response["earth_distance_mi"]

    @property
    def mars_distance_km(self) -> float:
        """
        Returns roadster's mars distance in km
        """
        return self.response["mars_distance_km"]

    @property
    def mars_distance_mi(self) -> float:
        """
        Returns roadster's mars distance in mi
        """
        return self.response["mars_distance_mi"]

    @property
    def wikipedia(self) -> str:
        """
        Returns roadster's wikipedia page
        """
        return self.response["wikipedia"]

    @property
    def video(self) -> str:
        """
        Returns roadster's launch video
        """
        return self.response["video"]

    @property
    def details(self) -> str:
        """
        Returns roadster's details
        """
        return self.response["details"]