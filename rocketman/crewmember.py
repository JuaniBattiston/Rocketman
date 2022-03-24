from .types.crewmember import CrewMemberData
from .utils.objects import BaseClass


class CrewMember(BaseClass):

    """
    Represents a crew member.

    Attributes
    ----------
    id: :class:`str`
        The crew member's ID.
    name: :class:`str`
        The crew member's name.
    agency: :class:`str`
        The crew member's agency of origin.
    image: :class:`str`
        An image of the crew member.
    wikipedia: :class:`str`
        The crew member's Wikipedia page.
    launches: :class:`str`
        A list of launches IDS in which the crew member participated.
    status: :class:`str`
        The crew member's status.
    """

    __slots__ = (
        "id",
        "name",
        "agency",
        "image",
        "wikipedia",
        "launches",
        "status",
    )

    def __init__(self, data: CrewMemberData):
        self._objects = {}
        self._update(data)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        attrs = {
            "id": self.id,
            "name": self.name,
            "agency": self.agency,
        }
        info = " ".join(f"{k}={v}" for k, v in attrs.items())
        return f"<{__class__.__name__} {info}>"
