class Capsule():

    __slots__ = (
        "response",
        "id"
    )

    def __init__(self, response):
        self.response:dict = response
        self.id:str = response["id"]

    @property
    def reuse_count(self) -> int:
        """
        Returns the reuse count of the capsule
        """
        return self.response["reuse_count"]

    @property
    def water_landings(self) -> int:
        """
        Returns the water landings count of the capsule
        """
        return self.response["water_landings"]

    @property
    def land_landings(self) -> int:
        """
        Returns the land landings count of the capsule
        """
        return self.response["land_landings"]
    
    @property
    def last_update(self) -> str:
        """
        Returns the last update of the capsule
        """
        return self.response["last_update"]

    @property
    def launches(self) -> list:
        """
        Returns a list of launch id involving the capsule
        """
        return self.response["launches"]

    @property
    def serial(self) -> list:
        """
        Returns the capsule serial
        """
        return self.response["serial"]

    @property
    def status(self) -> list:
        """
        Returns the capsule status
        """
        return self.response["status"]

    @property
    def capsule_type(self) -> list:
        """
        Returns the capsule type
        """
        return self.response["type"]