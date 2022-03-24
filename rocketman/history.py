from .types.history import HistoricEventData
from .utils.objects import BaseClass


class HistoricEvent(BaseClass):

    """
    Represents a historic event.

    Attributes
    ----------
    id: :class:`str`
        The event ID.
    links: Dict[:class:`str`, :class:`str`]
        Event relevant links.
    title: :class:`str`
        The event's title.
    event_date_utc: :class:`str`
        The event's date in UTC.
    event_date_unix: :class:`int`
        The event's date in unix time.
    details: :class:`str`
        The event's details.
    """

    __slots__ = (
        "id",
        "links",
        "title",
        "event_date_utc",
        "event_date_unix",
        "details",
    )

    def __init__(self, data: HistoricEventData):
        self._objects = {}
        self._update(data)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        attrs = {
            "id": self.id,
            "title": self.title,
        }
        info = " ".join(f"{k}={v}" for k, v in attrs.items())
        return f"<{__class__.__name__} {info}>"
