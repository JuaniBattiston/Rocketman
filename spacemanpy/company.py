class Company():

    __slots__ = (
    "headquarters",
    "links",
    "name",
    "founder",
    "founded",
    "employees",
    "vehicles",
    "launch_sites",
    "test_sites",
    "ceo",
    "cto",
    "coo",
    "cto_propulsion",
    "valuation",
    "summary",
    "id"
    )

    def __init__(self, content):
        self.headquarters:dict = content["headquarters"]
        self.links:dict = content["links"]
        self.name:str = content["name"]
        self.founder:str = content["founder"]
        self.founded:int = content["founded"]
        self.employees:int = content["employees"]
        self.vehicles:int = content["vehicles"]
        self.launch_sites:int = content["launch_sites"]
        self.test_sites:int = content["test_sites"]
        self.ceo:str = content["ceo"]
        self.cto:str = content["cto"]
        self.coo:str = content["coo"]
        self.cto_propulsion:str = content["cto_propulsion"]
        self.valuation:int = content["valuation"]
        self.summary:str = content["summary"]
        self.id:str = content["id"]
