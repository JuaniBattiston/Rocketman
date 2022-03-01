import asyncio

from spacemanpy.crewmember import CrewMember
from spacemanpy.capsule import Capsule
from spacemanpy.company import Company
from spacemanpy.core import Core
from spacemanpy.dragon import Dragon
from spacemanpy.history import HistoricEvent
from spacemanpy.landingpad import LandingPad
from spacemanpy.launch import Launch
from spacemanpy.launchpad import LaunchPad
from spacemanpy.payload import Payload
from spacemanpy.roadster import Roadster
from spacemanpy.rocket import Rocket
from spacemanpy.ship import Ship
from spacemanpy.starlink import Starlink
from spacemanpy.http import HTTPClient

from typing import List, Optional

from spacemanpy.types.starlink import StarlinkData


class Spaceman:
    def __init__(self, loop: Optional[asyncio.AbstractEventLoop] = None):
        self._http = HTTPClient(loop)
        self.base_url = "https://api.spacexdata.com/v4/"

    async def get_capsules(self) -> List[Capsule]:

        data = await self._http.request(method="GET", path="capsules")
        return [Capsule(i) for i in data]

    async def get_capsule(self, id: str) -> Capsule:

        data = await self._http.request(method="GET", path="capsules/" + id)
        return Capsule(data)

    async def company_info(self) -> Company:

        data = await self._http.request(method="GET", path="company")
        return Company(data)

    async def get_cores(self) -> List[Core]:

        data = await self._http.request(method="GET", path="cores")
        return [Core(i) for i in data]

    async def get_core(self, id: str) -> Core:

        data = await self._http.request(method="GET", path="cores/" + id)
        return Core(data)

    async def get_crewmembers(self) -> List[CrewMember]:

        data = await self._http.request(method="GET", path="crew")
        return [CrewMember(i) for i in data]

    async def get_crew_member(self, id: str) -> CrewMember:

        data = await self._http.request(method="GET", path="crew/" + id)
        return CrewMember(data)

    async def get_dragons(self) -> List[Dragon]:

        data = await self._http.request(method="GET", path="dragons")
        return [Dragon(i) for i in data]

    async def get_dragon(self, id: str) -> Dragon:

        data = await self._http.request(method="GET", path="dragons/" + id)
        return Dragon(data)

    async def get_historic_events(self) -> List[HistoricEvent]:

        data = await self._http.request(method="GET", path="history")
        return [HistoricEvent(i) for i in data]

    async def historic_event(self, id: str) -> HistoricEvent:

        data = await self._http.request(method="GET", path="history/" + id)
        return HistoricEvent(data)

    async def get_landpads(self) -> List[LandingPad]:

        data = await self._http.request(method="GET", path="landpads")
        return [LandingPad(i) for i in data]

    async def get_landpad(self, id: str) -> LandingPad:

        data = await self._http.request(method="GET", path="landpads/" + id)
        return LandingPad(data)

    async def get_launches(self) -> List[Launch]:

        data = await self._http.request(method="GET", path="launches")
        return [Launch(i) for i in data]

    async def get_launch(self, id: str) -> Launch:

        data = await self._http.request(method="GET", path="launches/" + id)
        return Launch(data)

    async def latest_launch(self) -> Launch:

        data = await self._http.request(method="GET", path="launches/latest")
        return Launch(data)

    async def next_launch(self) -> Launch:

        data = await self._http.request(method="GET", path="launches/next")
        return Launch(data)

    async def upcoming_launches(self) -> List[Launch]:

        data = await self._http.request(method="GET", path="launches/upcoming")
        return [Launch(i) for i in data]

    async def get_launchpads(self) -> List[LaunchPad]:

        data = await self._http.request(method="GET", path="launchpads")
        return [LaunchPad(i) for i in data]

    async def launchpad(self, id: str) -> LaunchPad:

        data = await self._http.request(method="GET", path="launchpad/" + id)
        return LaunchPad(data)

    async def get_payloads(self) -> List[Payload]:

        data = await self._http.request(method="GET", path="payloads")
        return [Payload(i) for i in data]

    async def payload(self, id: str) -> Payload:

        data = await self._http.request(method="GET", path="payloads/" + id)
        return Payload(data)

    async def roadster(self) -> Roadster:

        data = await self._http.request(method="GET", path="roadster")
        return Roadster(data)

    async def get_rockets(self) -> List[Rocket]:

        data = await self._http.request(method="GET", path="rockets")
        return [Rocket(i) for i in data]

    async def rocket(self, id: str) -> Rocket:

        data = await self._http.request(method="GET", path="rockets/" + id)
        return Rocket(data)

    async def get_ships(self) -> List[Ship]:

        data = await self._http.request(method="GET", path="ships")
        return [Ship(i) for i in data]

    async def ship(self, id: str) -> Ship:

        data = await self._http.request(method="GET", path="ships/" + id)
        return Ship(data)

    async def get_starlinks(self) -> List[Starlink]:

        data = await self._http.request(method="GET", path="starlink")
        return [Starlink(i) for i in data]

    async def get_starlink(self, id: str) -> Starlink:

        data: StarlinkData = await self._http.request(
            method="GET", path="starlink/" + id
        )
        return Starlink(data)
