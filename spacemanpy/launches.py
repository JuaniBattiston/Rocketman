class Launch():

    __slots__ = (
        "response",
        "id"
    )

    def __init__(self, response):
        self.response:dict = response
        self.id:str = response["id"]

    @property
    def fairings(self) -> dict:
        """
        Returns a dict with info about the fairings
        """
        return self.response["fairings"]

    @property
    def links(self) -> dict:
        """
        Returns a dict with links related to the launch
        """
        return self.response["links"]

    @property
    def static_fire_date_utc(self) -> str:
        """
        Returns the static fire date in utc datetime format
        """
        return self.response["static_fire_date_utc"]

    @property
    def static_fire_date_unix(self) -> int:
        """
        Returns the static fire date in unix time
        """
        return self.response["static_fire_date_unix"]

    @property
    def tbd(self) -> bool:
        """
        Returns a bool value representing whether the launch
        date is yet to be defined or not
        """
        return self.response["tbd"]

    @property
    def net(self) -> bool:
        """
        Returns boolean value representing net
        """
        return self.response["net"]

    @property
    def window(self) -> int:
        """
        Returns launch window
        """
        return self.response["window"]

    @property
    def rocket(self) -> str:
        """
        Returns rocket involved in the launch
        """
        return self.response["rocket"]

    @property
    def success(self) -> bool:
        """
        Returns launch success state
        """
        return self.response["success"]

    @property
    def failures(self) -> list:
        """
        Returns a list of dicts containing all launch failures
        """
        return self.response["failures"]

    @property
    def details(self) -> str:
        """
        Returns details about the mission
        """
        return self.response["details"]

    @property
    def crew(self) -> list:
        """
        Returns list of the crew involved in the launch
        """
        return self.response["crew"]

    @property
    def ships(self) -> list:
        """
        Returns list of the ships involved in the launch
        """
        return self.response["ships"]

    @property
    def capsules(self) -> list:
        """
        Returns list of the capsules involved in the launch
        """
        return self.response["capsules"]

    @property
    def payloads(self) -> list:
        """
        Returns list of the payloads involved in the launch
        """
        return self.response["payloads"]

    @property
    def launchpad(self) -> str:
        """
        Returns the launchpad involved in the launch
        """
        return self.response["launchpad"]

    @property
    def auto_update(self) -> bool:
        """
        Returns a bool value stating whether the update of
        the launch is automated or not
        """
        return self.response["auto_update"]

    @property
    def flight_number(self) -> int:
        """
        Returns the flight number
        """
        return self.response["flight_number"]

    @property
    def name(self) -> str:
        """
        Returns the name of the mission
        """
        return self.response["name"]

    @property
    def date_utc(self) -> str:
        """
        Returns the launch date in utc datetime format
        """
        return self.response["date_utc"]

    @property
    def date_unix(self) -> int:
        """
        Returns the launch date in unix time
        """
        return self.response["date_unix"]

    @property
    def date_local(self) -> str:
        """
        Returns the launch date in local time
        """
        return self.response["date_local"]

    @property
    def date_precision(self) -> int:
        """
        Returns the launch date precision
        """
        return self.response["date_precision"]

    @property
    def upcoming(self) -> bool:
        """
        Returns a boolean value representing whether
        it is an upcoming launch or not
        """
        return self.response["upcoming"]

    @property
    def cores(self) -> list:
        """
        Returns a list of the cores involved in the launch
        """
        return self.response["cores"]