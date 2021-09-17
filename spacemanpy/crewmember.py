class CrewMember():

    __slots__ = (
        "response",
        "id"
    )

    def __init__(self, response):
        self.response:dict = response
        self.id:str = response["id"]

    @property
    def name(self) -> str:
        """
        Returns the crew member's name
        """
        return self.response["name"]

    @property
    def agency(self) -> str:
        """
        Returns the crew member's agency
        """
        return self.response["agency"]

    @property
    def image(self) -> str:
        """
        Returns a crew member's image
        """
        return self.response["image"]

    @property
    def launches(self) -> list:
        """
        Returns a list of the crew member's launches ids
        """
        return self.response["launches"]

    @property
    def status(self) -> str:
        """
        Returns a crew member's status
        """
        return self.response["status"]