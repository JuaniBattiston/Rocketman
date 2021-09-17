class Core():

    __slots__ = (
        "block",
        "reuse_count",
        "rtls_attempts",
        "rtls_landings",
        "asds_attempts",
        "last_update",
        "launches",
        "serial",
        "status",
        "id"
    )

    def __init__(self, content):
        self.block:int = content["block"]
        self.reuse_count:int = content["reuse_count"]
        self.rtls_attempts:int = content["rtls_attempts"]
        self.rtls_landings:int = content["rtls_landings"]
        self.asds_attempts:int = content["asds_attempts"]
        self.last_update:str = content["last_update"]
        self.launches:list = content["launches"]
        self.serial:str = content["serial"]
        self.status:str = content["status"]
        self.id:str = content["id"]