class Launch():

    __slots__ = (
        "fairings",
        "links",
        "static_fire_date_utc",
        "static_fire_date_unix",
        "tbd",
        "net",
        "window",
        "rocket",
        "success",
        "failures",
        "details",
        "crew",
        "ships",
        "capsules",
        "payloads",
        "launchpad",
        "auto_update",
        "flight_number",
        "name",
        "date_utc",
        "date_unix",
        "date_local",
        "date_precision",
        "upcoming",
        "cores",
        "id"
    )

    def __init__(self, content):
        self.fairings:dict = content["fairings"]
        self.links:dict = content["links"]
        self.static_fire_date_utc:str = content["static_fire_date_utc"]
        self.static_fire_date_unix:int = content["static_fire_date_unix"]
        self.tbd:bool = content["tbd"]
        self.net:bool = content["net"]
        self.window:int = content["window"]
        self.rocket:str = content["rocket"]
        self.success:bool = content["success"]
        self.failures:list = content["failures"]
        self.details:str = content["details"]
        self.crew:list = content["crew"]
        self.ships:list = content["ships"]
        self.capsules:list = content["capsules"]
        self.payloads:list = content["payloads"]
        self.launchpad:str = content["launchpad"]
        self.auto_update:bool = content["auto_update"]
        self.flight_number:int = content["flight_number"]
        self.name:str = content["name"]
        self.date_utc:str = content["date_utc"]
        self.date_unix:int = content["date_unix"]
        self.date_local:str = content["date_local"]
        self.date_precision:str = content["date_precision"]
        self.upcoming:bool = content["upcoming"]
        self.cores:list = content["cores"]
        self.id:str = content["id"]