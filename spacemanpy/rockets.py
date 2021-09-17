class Rocket():

    __slots__ = (
        "response",
        "id"
    )

    def __init__(self, response):
        self.response = response
        self.id = response["id"]

    @property
    def height(self) -> dict:
        """
        Returns rocket's height
        """
        return self.response["height"]

    @property
    def diameter(self) -> dict:
        """
        Returns rocket's diameter
        """
        return self.response["diameter"]

    @property
    def mass(self) -> dict:
        """
        Returns rocket's mass
        """
        return self.response["mass"]

    @property
    def first_stage(self) -> dict:
        """
        Returns rocket's first stage info
        """
        return self.response["first_stage"]

    @property
    def second_stage(self) -> dict:
        """
        Returns rocket's second stage info
        """
        return self.response["second_stage"]

    @property
    def engines(self) -> dict:
        """
        Returns rocket's engine info
        """
        return self.response["engines"]

    @property
    def landing_legs(self) -> dict:
        """
        Returns rocket's landing legs info
        """
        return self.response["landing_legs"]

    @property
    def payload_weights(self) -> dict:
        """
        Returns rocket's payload weights info
        """
        return self.response["payload_weights"]

    @property
    def flickr_images(self) -> list:
        """
        Returns rocket images
        """
        return self.response["flickr_images"]

    @property
    def name(self) -> str:
        """
        Returns rocket's name
        """
        return self.response["name"]

    @property
    def rocket_type(self) -> str:
        """
        Returns rocket's type
        """
        return self.response["type"]

    @property
    def is_active(self) -> bool:
        """
        Returns rocket's state
        """
        return self.response["active"]

    @property
    def stages(self) -> int:
        """
        Returns rocket's stages count
        """
        return self.response["stages"]

    @property
    def boosters(self) -> int:
        """
        Returns rocket's boosters count
        """
        return self.response["boosters"]

    @property
    def cost_per_launch(self) -> int:
        """
        Returns rocket's cost per launch
        """
        return self.response["cost_per_launch"]

    @property
    def success_rate(self) -> int:
        """
        Returns rocket's success rate
        """
        return self.response["success_rate"]

    @property
    def first_flight(self) -> str:
        """
        Returns rocket's first flight date
        """
        return self.response["first_flight"]

    @property
    def country(self) -> str:
        """
        Returns rocket's country
        """
        return self.response["country"]

    @property
    def company(self) -> str:
        """
        Returns rocket's company
        """
        return self.response["company"]

    @property
    def wikipedia(self) -> str:
        """
        Returns rocket's wikipedia page
        """
        return self.response["wikipedia"]

    @property
    def description(self) -> str:
        """
        Returns rocket's description
        """
        return self.response["description"]