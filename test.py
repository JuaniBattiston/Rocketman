import asyncio
from spacemanpy.spaceman import Spaceman

import sys


if (
    sys.version_info[0] == 3
    and sys.version_info[1] >= 8
    and sys.platform.startswith("win")
):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

loop = asyncio.new_event_loop()
spaceman = Spaceman(loop)


async def main():
    a = await spaceman.get_starlinks()
    print(a[0].spacetrack.site)


loop.run_until_complete(main())
