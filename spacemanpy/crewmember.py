from spacemanpy.types.crewmember import CrewMemberData
from spacemanpy.utils.objects import BaseClass


class CrewMember(BaseClass):
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
