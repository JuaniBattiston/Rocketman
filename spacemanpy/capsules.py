class Capsule():

    __slots__ = (
        "reuse_count",
        "water_landings",
        "land_landings",
        "last_update",
        "launches",
        "serial",
        "status",
        "type",
        "id"
    )

    def __init__(self, content):
        self.reuse_count:int = content["reuse_count"]
        self.water_landings:int = content["water_landings"]
        self.land_landings:int = content["land_landings"]
        self.last_update:str = content["last_update"]
        self.launches:list = content["launches"]
        self.serial:str = content["serial"]
        self.status:str = content["status"]
        self.type:str = content["type"]
        self.id:str = content["id"]