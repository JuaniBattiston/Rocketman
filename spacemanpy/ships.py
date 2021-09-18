class Ship():

    __slots__ = (
        "response",
        "id"
    )

    def __init__(self, response):
        self.response = response
        self.id = response["id"]

    @property
    def legacy_id(self) -> str:
        """
        Returns the legacy id of the ship
        """
        return self.response["legacy_id"]
    
    @property
    def model(self) -> str:
        """
        Returns the ship's model
        """
        return self.response["model"]
    
    @property
    def ship_type(self) -> str:
        """
        Returns the ship's type
        """
        return self.response["type"]
    
    @property
    def roles(self) -> list:
        """
        Returns the ship's roles
        """
        return self.response["roles"]
    
    @property
    def imo(self) -> int:
        """
        Returns the ship's imo
        """
        return self.response["imo"]

    @property
    def mmsi(self) -> int:
        """
        Returns the ship's mmsi
        """
        return self.response["mmsi"]

    @property
    def ships_abs(self) -> int:
        """
        Returns the ship's abs
        """
        return self.response["abs"]

    @property
    def ship_class(self) -> int:
        """
        Returns the ship's class
        """
        return self.response["ship_class"]

    @property
    def mass_kg(self) -> int:
        """
        Returns the ship's mass in kgs
        """
        return self.response["mass_kg"]

    @property
    def mass_lbs(self) -> int:
        """
        Returns the ship's mass in lbs
        """
        return self.response["mass_lbs"]

    @property
    def year_built(self) -> int:
        """
        Returns the ship's build year
        """
        return self.response["year_built"]

    @property
    def home_port(self) -> str:
        """
        Returns the ship's home port
        """
        return self.response["home_port"]

    @property
    def status(self) -> str:
        """
        Returns the ship's status
        """
        return self.response["status"]

    @property
    def speed(self) -> float:
        """
        Returns the ship's speed in kn
        """
        return self.response["speed_kn"]

    @property
    def course_deg(self) -> float:
        """
        Returns the ship's course deg
        """
        return self.response["course_deg"]

    @property
    def latitude(self) -> float:
        """
        Returns the ship's latitude
        """
        return self.response["latitude"]
    
    @property
    def longitude(self) -> float:
        """
        Returns the ship's longitude
        """
        return self.response["longitude"]

    @property
    def last_ais_update(self) -> str:
        """
        Returns the ship's last ais update
        """
        return self.response["last_ais_update"]

    @property
    def link(self) -> str:
        """
        Returns the ship's link
        """
        return self.response["link"]

    @property
    def image(self) -> str:
        """
        Returns a ship's image
        """
        return self.response["image"]

    @property
    def launches(self) -> list:
        """
        Returns a ship's launches
        """
        return self.response["launches"]

    @property
    def name(self) -> str:
        """
        Returns a ship's name
        """
        return self.response["name"]

    @property
    def active(self) -> bool:
        """
        Returns a ship's activity state
        """
        return self.response["active"]