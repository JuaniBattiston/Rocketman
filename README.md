# Rocketman

A lightweight API wrapper for the r/SpaceX API

# Installation

**Python 3.9 or higher is recommended**

```
python3 -m pip install rocketman
```

Clone repository:

```
$ git clone https://github.com/Batucho/Rocketman
```

```py
import sys
import asyncio
from rocketman import Rocketman


async def main():
    r = Rocketman()
    a = await r.get_launches()
    print(a[-1].id)


if sys.platform.startswith("win"): # Dumb asyncio stuff
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(main())
```

### [More examples here!](https://github.com/Batucho/Rocketman/tree/main/examples)

**Feel free to contribute or inform any bug!**
