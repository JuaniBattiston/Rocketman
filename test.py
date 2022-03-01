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
    a = await spaceman.get_capsules()
    # print(a[0].engines.thrust_vacuum.kn)
    print(a[0].id)


loop.run_until_complete(main())
