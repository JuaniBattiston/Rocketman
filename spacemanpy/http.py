import aiohttp
import asyncio
import sys
from typing import Optional, Union

from spacemanpy.errors import InvalidHTTPMethod, NotFound


class HTTPClient:
    def __init__(
        self,
        loop: Optional[asyncio.AbstractEventLoop] = None,
    ) -> None:
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.BASE_URL = "https://api.spacexdata.com/v4/"
        self._http = aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(
                verify_ssl=False,
                loop=self.loop,
            ),
            loop=self.loop,
            timeout=aiohttp.ClientTimeout(total=None),
        )

        user_agent = "Spaceman API Wrapper (https://github.com/Batucho/Spacemanpy) Python/{0[0]}.{0[1]} aiohttp/{1}"
        self.user_agent: str = user_agent.format(sys.version_info, aiohttp.__version__)

    async def request(
        self,
        method: str,
        path: str = "",
        timeout: Union[aiohttp.ClientTimeout, None] = None,
        **kwargs
    ):

        """|coro|
        Handles library requests.

        Parameters
        -----------
        method: :class:`str`
            Requested http method
        path: :class:`str`
            Url path.
        timeout Union[:class:`aiohttp.ClientTimeout`, None]

        Raises
        ------
        InvalidHTTPMethod
            Invalid HTTP method requested.
        NotFound
            Invalid id for requested object.
        """

        if method not in ("GET"):
            raise InvalidHTTPMethod

        if len(path.split("/")) > 1:
            _id = path.split("/")[1]

        headers = {"User-Agent": self.user_agent, "Content-Type": "application/json"}
        kwargs["headers"] = headers

        async with self._http as session:
            response = await session.request(
                method=method, url=self.BASE_URL + path, timeout=timeout, **kwargs
            )

            if response.status == 404:
                raise NotFound(_id)

            return await response.json()
