class CrewMember():

    __slots__ = (
        "name",
        "agency",
        "image",
        "wikipedia",
        "launches",
        "status",
        "id"
    )

    def __init__(self, content):
        self.name:str = content["name"]
        self.agency:str = content["agency"]
        self.image:str = content["image"]
        self.wikipedia:str = content["wikipedia"]
        self.launches:list = content["launches"]
        self.status:str = content["status"]
        self.id:str = content["id"]