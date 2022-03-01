from typing import TypedDict


class Headquarters(TypedDict):
    address: str
    city: str
    state: str


class CompanyLinks(TypedDict):
    website: str
    flickr: str
    twitter: str
    elon_twitter: str


class CompanyData(TypedDict):
    id: str
    headquaters: Headquarters
    links: CompanyLinks
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
