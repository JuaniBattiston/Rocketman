class Company():

    __slots__ = (
        "response",
        "id"
    )

    def __init__(self, response):
        self.response:dict = response
        self.id:str = response["id"]

    @property
    def headquarters(self) -> dict:
        """
        Returns a dict with headquarters location info
        """
        return self.response["headquarters"]

    @property
    def links(self) -> dict:
        """
        Returns a dict containing SpaceX's social media links
        """
        return self.response["links"]

    @property
    def name(self) -> str:
        """
        Returns the company name
        """
        return self.response["name"]

    @property
    def founder(self) -> str:
        """
        Returns the company's founder
        """
        return self.response["founder"]

    @property
    def founded(self) -> str:
        """
        Returns the company's foundation year
        """
        return self.response["founded"]

    @property
    def employees(self) -> int:
        """
        Returns the company's employees count
        """
        return self.response["employees"]

    @property
    def vehicles(self) -> int:
        """
        Returns the company's vehicles count
        """
        return self.response["vehicles"]

    @property
    def launch_sites(self) -> int:
        """
        Returns the company's launch sites count
        """
        return self.response["launch_sites"]

    @property
    def test_sites(self) -> int:
        """
        Returns the company's test sites count
        """
        return self.response["test_sites"]

    @property
    def ceo(self) -> str:
        """
        Returns the company's ceo
        """
        return self.response["ceo"]

    @property
    def cto(self) -> str:
        """
        Returns the company's cto
        """
        return self.response["cto"]

    @property
    def coo(self) -> str:
        """
        Returns the company's coo
        """
        return self.response["coo"]

    @property
    def cto_propulsion(self) -> str:
        """
        Returns the company's propulsion cto
        """
        return self.response["cto_propulsion"]

    @property
    def valuation(self) -> int:
        """
        Returns the company's net worth
        """
        return self.response["valuation"]

    @property
    def summary(self) -> str:
        """
        Returns a summary of the company
        """
        return self.response["summary"]