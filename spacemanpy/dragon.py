class Dragon():

    __slots__ = (
    "response",
    "id"
    )

    def __init__(self, response):
        self.response:dict = response
        self.id:str = response["id"]

    @property
    def heat_shield(self) -> dict:
        """
        Returns a dict with heat_shield info
        """
        return self.response["heat_shield"]

    @property
    def launch_payload_mass(self) -> dict:
        """
        Returns a dict with launch payload mass info
        """
        return self.response["launch_payload_mass"]

    @property
    def launch_payload_vol(self) -> dict:
        """
        Returns a dict with launch payload volume info
        """
        return self.response["launch_payload_vol"]

    @property
    def return_payload_mass(self) -> dict:
        """
        Returns a dict with return payload mass info
        """
        return self.response["return_payload_mass"]

    @property
    def return_payload_vol(self) -> dict:
        """
        Returns a dict with return payload vol info
        """
        return self.response["return_payload_vol"]

    @property
    def pressurized_capsule(self) -> dict:
        """
        Returns a dict with capsule info
        """
        return self.response["pressurized_capsule"]

    @property
    def trunk(self) -> dict:
        """
        Returns a dict with trunk info
        """
        return self.response["trunk"]

    @property
    def height_w_trunk(self) -> dict:
        """
        Returns a dict with the trunks's height in different unities
        """
        return self.response["height_w_trunk"]

    @property
    def diameter(self) -> dict:
        """
        Returns a dict with diameter info in different unities
        """
        return self.response["diameter"]

    @property
    def first_flight(self) -> str:
        """
        Returns dragon's first flight date
        """
        return self.response["first_flight"]

    @property
    def flickr_images(self) -> list:
        """
        Returns a list of images of the dragon
        """
        return self.response["flickr_images"]

    @property
    def name(self) -> str:
        """
        Returns the dragon's name
        """
        return self.response["name"]

    @property
    def dragon_type(self) -> str:
        """
        Returns the dragon's type
        """
        return self.response["type"]

    @property
    def is_active(self) -> bool:
        """
        Returns a bool value representing dragon's state
        """
        return self.response["active"]

    @property
    def crew_capacity(self) -> int:
        """
        Returns the dragon's crew capacity number
        """
        return self.response["crew_capacity"]

    @property
    def sidewall_angle(self) -> int:
        """
        Returns the dragon's sidewall angle in degrees
        """
        return self.response["sidewall_angle_deg"]

    @property
    def orbit_duration_yr(self) -> int:
        """
        Returns the dragon's orbit duration year
        """
        return self.response["orbit_duration_yr"]

    @property
    def dry_mass_kg(self) -> int:
        """
        Returns the dragon's dry mass in kg
        """
        return self.response["dry_mass_kg"]

    @property
    def dry_mass_lb(self) -> int:
        """
        Returns the dragon's dry mass in lb
        """
        return self.response["dry_mass_lb"]

    @property
    def thrusters(self) -> list:
        """
        Returns info about the dragon's thrusters
        """
        return self.response["thrusters"]

    @property
    def wikipedia(self) -> str:
        """
        Returns the dragon's wikipedia page
        """
        return self.response["wikipedia"]

    @property
    def description(self) -> str:
        """
        Returns the dragon's description
        """
        return self.response["description"]