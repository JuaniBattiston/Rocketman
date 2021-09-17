class LandingPad():

    __slots__ = (
        "images",
        "name",
        "full_name",
        "status",
        "type",
        "locality",
        "region",
        "latitude",
        "longitude",
        "landing_attempts",
        "landing_successes",
        "wikipedia",
        "details",
        "launches",
        "id"
    )

    def __init__(self, content):
        self.images:dict = content["images"]
        self.name:str = content["name"]
        self.full_name:str = content["full_name"]
        self.status:str = content["status"]
        self.type:str = content["type"]
        self.locality:int = content["locality"]
        self.region:int = content["region"]
        self.latitude:float = content["latitude"]
        self.longitude:float = content["longitude"]
        self.landing_attempts:int = content["landing_attempts"]
        self.landing_successes:int = content["landing_successes"]
        self.wikipedia:str = content["wikipedia"]
        self.details:str = content["details"]
        self.launches:list = content["launches"]
        self.id:str = content["id"]