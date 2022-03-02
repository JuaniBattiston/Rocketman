from typing import TypedDict


class HeadquartersData(TypedDict):
    address: str
    city: str
    state: str


class CompanyLinksData(TypedDict):
    website: str
    flickr: str
    twitter: str
    elon_twitter: str


class CompanyData(TypedDict):
    id: str
    headquarters: HeadquartersData
    links: CompanyLinksData
    name: str
    founder: str
    founded: int
    employees: int
    vehicles: int
    launch_sites: int
    test_sites: int
    ceo: str
    cto: str
    coo: str
    cto_propulsion: str
    valuation: int
    summary: str
