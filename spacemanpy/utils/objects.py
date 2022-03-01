from typing import Dict


class BaseClass:
    def __init__(self, data: Dict):
        self._objects = {}
        self._update(data)

    def _basic_update(self, data) -> None:
        for k, v in data.items():
            setattr(self, k.lower(), v)

    def _extended_update(self, data) -> None:
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

    def _update(self, data) -> None:

        if hasattr(self, "_objects"):
            self._extended_update(data)

        self._basic_update(data)
