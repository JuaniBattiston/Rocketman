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
    a = await spaceman.get_rocket("5e9d0d95eda69955f709d1eb")
    print(a.payload_weights.kg)


loop.run_until_complete(main())
