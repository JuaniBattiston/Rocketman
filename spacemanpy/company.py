from spacemanpy.types.company import CompanyData


class Company:
    def __init__(self, data: CompanyData):
        self._update(data)

    def _update(self, data: CompanyData) -> None:
        for k, v in data.items():
            setattr(self, k, v)

    def __repr__(self) -> str:
        attrs = {
            "name": self.name,
            "founder": self.founder,
        }
        info = " ".join(f"{k}={v}" for k, v in attrs.items())
        return f"<{__class__.__name__} {info}>"
