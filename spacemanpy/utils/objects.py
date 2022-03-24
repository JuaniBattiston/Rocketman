from typing import Dict


class BaseClass:
    def __init__(self, data: Dict):
        self._objects = {}
        self._update(data)

    def _update(self, data) -> None:

        if not data:
            return

        for k, v in data.items():
            if k in self._objects:
                if isinstance(v, list):
                    setattr(
                        self,
                        k.lower(),
                        self._objects[k](v[0])
                        if len(v) == 1
                        else [self._objects[k](i) for i in v],
                    )
                    continue

                setattr(self, k.lower(), self._objects[k](v))
                continue

            setattr(self, k.lower(), v)
