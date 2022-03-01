import aiohttp
import asyncio

from typing import Optional


class HTTPClient:
    def __init__(
        self,
        loop: Optional[asyncio.AbstractEventLoop] = None,
    ) -> None:
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.BASE_URL = "https://api.spacexdata.com/v4/"
        self._http = aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(verify_ssl=False, loop=self.loop),
            loop=self.loop,
            timeout=aiohttp.ClientTimeout(total=None),
        )

    async def request(self, method, path="", timeout=None):
        async with self._http as session:
            req = await session.request(method=method, url=self.BASE_URL + path)
            return await req.json()
