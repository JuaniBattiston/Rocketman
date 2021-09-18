class HistoricEvent():

    __slots__ = (
        "response",
        "id"
    )

    def __init__(self, response):
        self.response:dict = response
        self.id:str = response["id"]

    @property
    def title(self) -> str:
        """
        Returns event's title
        """
        return self.response["title"]

    @property
    def event_date_utc(self) -> str:
        """
        Returns event's date in utc time
        """
        return self.response["event_date_utc"]

    @property
    def event_date_unix(self) -> int:
        """
        Returns event's date in unix time
        """
        return self.response["event_date_unix"]

    @property
    def details(self) -> str:
        """
        Returns event's details
        """
        return self.response["details"]

    @property
    def links(self) -> dict:
        """
        Returns event's links
        """
        return self.response["links"]
