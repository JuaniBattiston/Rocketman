class LaunchPad():

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
        Returns the shortened name of the launch pad
        """
        return self.response["name"]

    @property
    def full_name(self) -> str:
        """
        Returns the full name of the launch pad
        """
        return self.response["full_name"]

    @property
    def locality(self) -> str:
        """
        Returns the locality of the launch pad
        """
        return self.response["locality"]

    @property
    def region(self) -> str:
        """
        Returns the region of the launch pad
        """
        return self.response["region"]

    @property
    def latitude(self) -> float:
        """
        Returns the launch pad's latitude
        """
        return self.response["latitude"]

    @property
    def longitud(self) -> float:
        """
        Returns the launch pad's longitud
        """
        return self.response["longitud"]

    @property
    def launch_attempts(self) -> int:
        """
        Returns the launch attempts count
        """
        return self.response["launch_attempts"]

    @property
    def launch_successes(self) -> int:
        """
        Returns the launch successes count
        """
        return self.response["launch_successes"]

    @property
    def rockets(self) -> list:
        """
        Returns the rockets that launched in the launch pad
        """
        return self.response["rockets"]

    @property
    def launches(self) -> list:
        """
        Returns launches in which the launch pad was involved
        """
        return self.response["launches"]

    @property
    def status(self) -> str:
        """
        Returns the launch pad status
        """
        return self.response["status"]