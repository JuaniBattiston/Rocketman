import sys
import asyncio
from rocketman import Rocketman


async def main():
    r = Rocketman()
    a = await r.get_launches()
    print(a[-1].id)


if sys.platform.startswith("win"):  # Dumb asyncio stuff
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(main())
