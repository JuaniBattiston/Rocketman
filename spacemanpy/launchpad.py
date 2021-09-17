class LaunchPad():

    __slots__ = (
        "images",
        "name",
        "full_name",
        "locality",
        "region",
        "latitude",
        "longitude",
        "launch_attempts",
        "launch_successes",
        "rockets",
        "timezone",
        "launches",
        "status",
        "details",   
        "id"
    )

    def __init__(self, content):
        self.images:dict = content["images"]
        self.name:str = content["name"]
        self.full_name:str = content["full_name"]
        self.locality:str = content["locality"]
        self.region:str = content["region"]
        self.latitude:float = content["latitude"]
        self.longitude:float = content["longitude"]
        self.launch_attempts:int = content["launch_attempts"]
        self.launch_successes:int = content["launch_successes"]
        self.rockets:list = content["rockets"]
        self.timezone:str = content["timezone"]
        self.launches:list = content["launches"]
        self.status:str = content["status"]
        self.details:str = content["details"]
        self.id:str = content["id"]