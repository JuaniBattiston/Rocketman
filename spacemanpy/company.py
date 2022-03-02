from spacemanpy.types.company import CompanyData, CompanyLinksData, HeadquartersData
from spacemanpy.utils.objects import BaseClass


class Headquarters(BaseClass):
    __slots__ = (
        "address",
        "city",
        "state",
    )

    def __init__(self, data: HeadquartersData):
        self._objects = {}
        self._update(data)


class CompanyLinks(BaseClass):

    __slots__ = (
        "website",
        "flickr",
        "twitter",
        "elon_twitter",
    )

    def __init__(self, data: CompanyLinksData):
        self._objects = {}
        self._update(data)


class Company(BaseClass):

    __slots__ = (
        "id",
        "headquarters",
        "links",
        "name",
        "founder",
        "founded",
        "employees",
        "vehicles",
        "launch_sites",
        "test_sites",
        "ceo",
        "cto",
        "coo",
        "cto_propulsion",
        "valuation",
        "summary",
    )

    def __init__(self, data: CompanyData):
        self._objects = {"headquarters": Headquarters, "links": CompanyLinks}
        self._update(data)

    def __repr__(self) -> str:
        attrs = {
            "name": self.name,
            "founder": self.founder,
        }
        info = " ".join(f"{k}={v}" for k, v in attrs.items())
        return f"<{__class__.__name__} {info}>"
