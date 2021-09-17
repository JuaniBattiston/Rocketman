class Dragon():

    __slots__ = (
    "heat_shield",
    "lauch_payload_mass",
    "launch_payload_vol",
    "return_payload_mass",
    "return_payload_vol",
    "pressurized_capsule",
    "trunk",
    "height_w_trunk",
    "diameter",
    "first_flight",
    "flickr_images",
    "name",
    "type",
    "active",
    "crew_capacity",
    "orbit_duration_yr",
    "dry_mass_kg",
    "dry_mass_lb",
    "thrusters",
    "wikipedia",
    "description",
    "id"
    )

    def __init__(self, content):
        self.heat_shield:dict = content["heat_shield"]
        self.lauch_payload_mass:dict = content["launch_payload_mass"]
        self.launch_payload_vol:dict = content["launch_payload_vol"]
        self.return_payload_vol:dict = content["return_payload_vol"]
        self.pressurized_capsule:dict = content["pressurized_capsule"]
        self.trunk:dict = content["trunk"]
        self.height_w_trunk:dict = content["height_w_trunk"]
        self.diameter:dict = content["diameter"]
        self.first_flight:str = content["first_flight"]
        self.flickr_images:list = content["flickr_images"]
        self.name:str = content["name"]
        self.type:str = content["type"]
        self.active:bool = content["active"]
        self.crew_capacity:int = content["crew_capacity"]
        self.orbit_duration_yr:int = content["orbit_duration_yr"]
        self.dry_mass_kg:int = content["dry_mass_kg"]
        self.dry_mass_lb:int = content["dry_mass_lb"]
        self.thrusters:list = content["thrusters"]
        self.wikipedia:str = content["wikipedia"]
        self.description:str = content["description"]
        self.id:str = content["id"]