from rocketman.types.company import CompanyData, CompanyLinksData, HeadquartersData
from rocketman.utils.objects import BaseClass


class Headquarters(BaseClass):

    """
    Represents SpaceX's Headquearters.

    Attributes
    ----------
    address: :class:`str`
        Headquearter's address.
    city: :class:`str`
        Headquearter's city.
    state: :class:`str`
        Headquearter's state.
    """

    __slots__ = (
        "address",
        "city",
        "state",
    )

    def __init__(self, data: HeadquartersData):
        self._objects = {}
        self._update(data)


class CompanyLinks(BaseClass):

    """
    Represents SpaceX's Links.

    Attributes
    ----------
    website: :class:`str`
        SpaceX's website.
    flickr: :class:`str`
        SpaceX's flickr.
    twitter: :class:`str`
        SpaceX's twitter.
    elon_twitter: :class:`str`
        Elon Musk's (CEO) twitter.
    """

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

    """
    Represents SpaceX's company information.

    Attributes
    ----------
    id: :class:`str`
        Company's internal ID.
    headquarters: :class:`Headquarters`
        SpaceX's headquarter.
    links: :class:`CompanyLinks`
        SpaceX's links of interest.
    name: :class:`str`
        SpaceX's name.
    founder: :class:`str`
        SpaceX's founder's name.
    founded: :class:`int`
        SpaceX's foundation date.
    employees: :class:`int`
        SpaceX's employees count.
    vehicles: :class:`int`
        SpaceX's vehicles count.
    launch_sites: :class:`int`
        SpaceX's launch sites count.
    test_sites: :class:`str`
        SpaceX's test sites count.
    ceo: :class:`str`
        SpaceX's CEO.
    cto: :class:`str`
        SpaceX's CTO.
    coo: :class:`str`
        SpaceX's COO.
    cto_propulsion: :class:`str`
        SpaceX's CTO of Propulsion.
    valuation: :class:`str`
        SpaceX's valuation.
    summary: :class:`str`
        SpaceX's company summary.
    """

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
