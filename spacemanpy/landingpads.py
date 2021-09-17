class LandingPad():

    __slots__ = (
        "response",
        "id"
    )

    def __init__(self, response):
        self.response:dict = response
        self.id:str = response["id"]

    @property
    def images(self) -> dict:
        """
        Returns a dict with images
        """
        return self.response["images"]

    @property
    def name(self) -> str:
        """
        Returns the shortened name of the landing pad
        """
        return self.response["name"]

    @property
    def full_name(self) -> str:
        """
        Returns the full name of the landing pad
        """
        return self.response["full_name"]

    @property
    def status(self) -> str:
        """
        Returns the landing pad status
        """
        return self.response["status"]

    @property
    def lp_type(self) -> str:
        """
        Returns the landing pad type
        """
        return self.response["type"]
    
    @property
    def locality(self) -> str:
        """
        Returns the locality of the landing pad
        """
        return self.response["locality"]

    @property
    def region(self) -> str:
        """
        Returns the region of the landing pad
        """
        return self.response["region"]

    @property
    def latitude(self) -> float:
        """
        Returns the landing pad's latitude
        """
        return self.response["latitude"]

    @property
    def longitud(self) -> float:
        """
        Returns the landing pad's longitud
        """
        return self.response["longitud"]

    @property
    def landing_attempts(self) -> int:
        """
        Returns the landing attempts count
        """
        return self.response["landing_attempts"]

    @property
    def landing_successes(self) -> int:
        """
        Returns the landing successes count
        """
        return self.response["landing_successes"]

    @property
    def wikipedia(self) -> str:
        """
        Returns the wikipedia link of the landing pad
        """
        return self.response["wikipedia"]

    @property
    def details(self) -> str:
        """
        Returns details about the landing pad
        """
        return self.response["details"]

    @property
    def launches(self) -> str:
        """
        Returns launches in which the landing pad was involved
        """
        return self.response["launches"]