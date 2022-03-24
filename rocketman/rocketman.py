import asyncio
import aiohttp

from rocketman.crewmember import CrewMember
from rocketman.capsule import Capsule
from rocketman.company import Company
from rocketman.core import Core
from rocketman.dragon import Dragon
from rocketman.history import HistoricEvent
from rocketman.landingpad import LandingPad
from rocketman.launch import Launch
from rocketman.launchpad import LaunchPad
from rocketman.payload import Payload
from rocketman.roadster import Roadster
from rocketman.rocket import Rocket
from rocketman.ship import Ship
from rocketman.starlink import Starlink
from rocketman.http import HTTPClient

from typing import List, Optional

__all__ = ("Spaceman",)


class Rocketman:
    def __init__(
        self,
        loop: Optional[asyncio.AbstractEventLoop] = None,
        timeout: Optional[aiohttp.ClientTimeout] = None,
    ):
        self._http = HTTPClient(loop)
        self.timeout = timeout

    async def get_capsules(self) -> List[Capsule]:

        """|coro|

        Get all capsules.

        Returns
        --------
        List[:class:`Capsule`]
            List of capsules.
        """

        data = await self._http.request(
            method="GET", path="capsules", timeout=self.timeout
        )
        return [Capsule(i) for i in data]

    async def get_capsule(self, id: str) -> Capsule:

        """|coro|

        Get capsule.

        Paramenters
        --------
        id: :class:`str`
            Capsule ID.

        Returns
        --------
        :class:`Capsule`
        """

        data = await self._http.request(
            method="GET", path="capsules/" + id, timeout=self.timeout
        )
        return Capsule(data)

    async def company_info(self) -> Company:

        """|coro|

        Get company info.

        Returns
        --------
        :class:`Company`
        """

        data = await self._http.request(
            method="GET", path="company", timeout=self.timeout
        )
        return Company(data)

    async def get_cores(self) -> List[Core]:

        """|coro|

        Get all cores.

        Returns
        --------
        List[:class:`Core`]
            List of cores.
        """

        data = await self._http.request(
            method="GET", path="cores", timeout=self.timeout
        )
        return [Core(i) for i in data]

    async def get_core(self, id: str) -> Core:

        """|coro|

        Get core.

        Paramenters
        --------
        id: :class:`str`
            Core ID.

        Returns
        --------
        :class:`Core`
        """

        data = await self._http.request(
            method="GET", path="cores/" + id, timeout=self.timeout
        )
        return Core(data)

    async def get_crewmembers(self) -> List[CrewMember]:

        """|coro|

        Get all crewmembers.

        Returns
        --------
        List[:class:`CrewMember`]
            List of crewmembers.
        """

        data = await self._http.request(method="GET", path="crew", timeout=self.timeout)
        return [CrewMember(i) for i in data]

    async def get_crew_member(self, id: str) -> CrewMember:

        """|coro|

        Get crewmember.

        Paramenters
        --------
        id: :class:`str`
            Crewmember ID.

        Returns
        --------
        :class:`CrewMember`
        """

        data = await self._http.request(
            method="GET", path="crew/" + id, timeout=self.timeout
        )
        return CrewMember(data)

    async def get_dragons(self) -> List[Dragon]:

        """|coro|

        Get all dragon capsules.

        Returns
        --------
        List[:class:`Dragon`]
            List of dragon.
        """

        data = await self._http.request(
            method="GET", path="dragons", timeout=self.timeout
        )
        return [Dragon(i) for i in data]

    async def get_dragon(self, id: str) -> Dragon:

        """|coro|

        Get dragon.

        Paramenters
        --------
        id: :class:`str`
            Dragon ID.

        Returns
        --------
        :class:`Dragon`
        """

        data = await self._http.request(
            method="GET", path="dragons/" + id, timeout=self.timeout
        )
        return Dragon(data)

    async def get_historic_events(self) -> List[HistoricEvent]:

        """|coro|

        Get all Space'x historic events.

        Returns
        --------
        List[:class:`HistoricEvent`]
            List of historic events.
        """

        data = await self._http.request(
            method="GET", path="history", timeout=self.timeout
        )
        return [HistoricEvent(i) for i in data]

    async def historic_event(self, id: str) -> HistoricEvent:

        """|coro|

        Get historic event.

        Paramenters
        --------
        id: :class:`str`
            Historic event ID.

        Returns
        --------
        :class:`HistoricEvent`
        """

        data = await self._http.request(
            method="GET", path="history/" + id, timeout=self.timeout
        )
        return HistoricEvent(data)

    async def get_landpads(self) -> List[LandingPad]:

        """|coro|

        Get all Space'x landpads.

        Returns
        --------
        List[:class:`LandingPad`]
            List of landpads.
        """

        data = await self._http.request(
            method="GET", path="landpads", timeout=self.timeout
        )
        return [LandingPad(i) for i in data]

    async def get_landpad(self, id: str) -> LandingPad:

        """|coro|

        Get landpad.

        Paramenters
        --------
        id: :class:`str`
            Landpad's ID.

        Returns
        --------
        :class:`LandingPad`
        """

        data = await self._http.request(
            method="GET", path="landpads/" + id, timeout=self.timeout
        )
        return LandingPad(data)

    async def get_launches(self) -> List[Launch]:

        """|coro|

        Get all Space'x launches.

        Returns
        --------
        List[:class:`Launch`]
            List of launches.
        """

        data = await self._http.request(
            method="GET", path="launches", timeout=self.timeout
        )
        return [Launch(i) for i in data]

    async def get_launch(self, id: str) -> Launch:

        """|coro|

        Get launch.

        Paramenters
        --------
        id: :class:`str`
            Launch ID.

        Returns
        --------
        :class:`Launch`
        """

        data = await self._http.request(
            method="GET", path="launches/" + id, timeout=self.timeout
        )
        return Launch(data)

    async def latest_launch(self) -> Launch:

        """|coro|

        Get latest launch.

        Paramenters
        --------
        id: :class:`str`
            Launch ID.

        Returns
        --------
        :class:`Launch`
        """

        data = await self._http.request(
            method="GET", path="launches/latest", timeout=self.timeout
        )
        return Launch(data)

    async def next_launch(self) -> Launch:

        """|coro|

        Get next launch.

        Paramenters
        --------
        id: :class:`str`
            Launch ID.

        Returns
        --------
        :class:`Launch`
        """

        data = await self._http.request(
            method="GET", path="launches/next", timeout=self.timeout
        )
        return Launch(data)

    async def upcoming_launches(self) -> List[Launch]:

        """|coro|

        Get all Space'x upcoming launches.

        Returns
        --------
        List[:class:`Launch`]
            List of upcoming launches.
        """

        data = await self._http.request(
            method="GET", path="launches/upcoming", timeout=self.timeout
        )
        return [Launch(i) for i in data]

    async def get_launchpads(self) -> List[LaunchPad]:

        """|coro|

        Get all Space'x launchpads.

        Returns
        --------
        List[:class:`LaunchPad`]
            List of launchpads.
        """

        data = await self._http.request(
            method="GET", path="launchpads", timeout=self.timeout
        )
        return [LaunchPad(i) for i in data]

    async def launchpad(self, id: str) -> LaunchPad:

        """|coro|

        Get launchpad.

        Paramenters
        --------
        id: :class:`str`
            Launchpad's ID.

        Returns
        --------
        :class:`LaunchPad`
        """

        data = await self._http.request(
            method="GET", path="launchpad/" + id, timeout=self.timeout
        )
        return LaunchPad(data)

    async def get_payloads(self) -> List[Payload]:

        """|coro|

        Get all Space'x payloads.

        Returns
        --------
        List[:class:`Payload`]
            List of payloads.
        """

        data = await self._http.request(
            method="GET", path="payloads", timeout=self.timeout
        )
        return [Payload(i) for i in data]

    async def payload(self, id: str) -> Payload:

        """|coro|

        Get payload.

        Paramenters
        --------
        id: :class:`str`
            Payload's ID.

        Returns
        --------
        :class:`Payload`
        """

        data = await self._http.request(
            method="GET", path="payloads/" + id, timeout=self.timeout
        )
        return Payload(data)

    async def roadster(self) -> Roadster:

        """|coro|

        Get roadster.

        Paramenters
        --------
        id: :class:`str`
            Roadster ID.

        Returns
        --------
        :class:`Roadster`
        """

        data = await self._http.request(
            method="GET", path="roadster", timeout=self.timeout
        )
        return Roadster(data)

    async def get_rockets(self) -> List[Rocket]:

        """|coro|

        Get all Space'x rockets.

        Returns
        --------
        List[:class:`Rocket`]
            List of rockets.
        """

        data = await self._http.request(
            method="GET", path="rockets", timeout=self.timeout
        )
        return [Rocket(i) for i in data]

    async def get_rocket(self, id: str) -> Rocket:

        """|coro|

        Get rocket.

        Paramenters
        --------
        id: :class:`str`
            Rocket ID.

        Returns
        --------
        :class:`Rocket`
        """

        data = await self._http.request(
            method="GET", path="rockets/" + id, timeout=self.timeout
        )
        return Rocket(data)

    async def get_ships(self) -> List[Ship]:

        """|coro|

        Get all Space'x ships.

        Returns
        --------
        List[:class:`Ship`]
            List of ships.
        """

        data = await self._http.request(
            method="GET", path="ships", timeout=self.timeout
        )
        return [Ship(i) for i in data]

    async def ship(self, id: str) -> Ship:

        """|coro|

        Get ship.

        Paramenters
        --------
        id: :class:`str`
            Ship ID.

        Returns
        --------
        :class:`Ship`
        """

        data = await self._http.request(
            method="GET", path="ships/" + id, timeout=self.timeout
        )
        return Ship(data)

    async def get_starlinks(self) -> List[Starlink]:

        """|coro|

        Get all Space'x starlinks.

        Returns
        --------
        List[:class:`Starlink`]
            List of starlinks.
        """

        data = await self._http.request(
            method="GET", path="starlink", timeout=self.timeout
        )
        return [Starlink(i) for i in data]

    async def get_starlink(self, id: str) -> Starlink:

        """|coro|

        Get starlink.

        Paramenters
        --------
        id: :class:`str`
            Starlink's ID.

        Returns
        --------
        :class:`Starlink`
        """

        data = await self._http.request(
            method="GET", path="starlink/" + id, timeout=self.timeout
        )
        return Starlink(data)
