class Core():

    __slots__ = (
        "response",
        "id"
    )

    def __init__(self, response):
        self.response:dict = response
        self.id:str = response["id"]

    @property
    def block(self) -> int:
        """
        Returns the core block
        """
        return self.response["block"]

    @property
    def reuse_count(self) -> int:
        """
        Returns the core reuses count
        """
        return self.response["reuse_count"]

    @property
    def rtls_attempts(self) -> int:
        """
        Returns the core rtls attempts count
        """
        return self.response["rtls_attempts"]

    @property
    def rtls_landings(self) -> int:
        """
        Returns the core rtls landings count
        """
        return self.response["rtls_landings"]

    @property
    def asds_attempts(self) -> int:
        """
        Returns the core asds attempts count
        """
        return self.response["asds_attempts"]

    @property
    def asds_landings(self) -> int:
        """
        Returns the core asds landings count
        """
        return self.response["asds_landings"]

    @property
    def asds_landings(self) -> int:
        """
        Returns the core asds landings count
        """
        return self.response["asds_landings"]

    @property
    def last_update(self) -> str:
        """
        Returns the core last update
        """
        return self.response["last_update"]

    @property
    def launches(self) -> list:
        """
        Returns a list of launch id involving the core
        """
        return self.response["launches"]

    @property
    def serial(self) -> str:
        """
        Returns the core serial
        """
        return self.response["serial"]

    @property
    def status(self) -> str:
        """
        Returns the core status
        """
        return self.response["status"]