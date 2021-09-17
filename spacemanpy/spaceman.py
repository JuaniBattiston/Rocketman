import requests
from capsules import Capsule
from company import Company
from cores import Core
from crewmember import CrewMember
from dragon import Dragon

class Spaceman():

    def __init__(self):
        self

    def _get(self, method):

        base_url = f"https://api.spacexdata.com/v4/{method}"
        req = requests.get(url = base_url, timeout = 5)
        req.raise_for_status()

        return req.json()

    @property
    def get_capsules(self):

        req = self._get("capsules")

        return [Capsule(i) for i in req]

    def get_capsule(self, _id):

        req = self._get(f"capsules/{_id}")

        return Capsule(req)

    @property
    def company_info(self):

        req = self._get("company")
        return Company(req)

    @property
    def get_cores(self):

        req = self._get("cores")

        return [Core(i) for i in req]

    def get_core(self, _id):

        req = self._get(f"cores/{_id}")

        return Core(req)

    @property
    def get_crew(self):

        req = self._get("crew")

        return [CrewMember(i) for i in req]

    def get_crew_member(self, _id):

        req = self._get(f"crew/{_id}")

        return CrewMember(req)

    @property
    def get_dragons(self):

        req = self._get("dragons")

        return [Dragon(i) for i in req]

    def get_dragon(self, _id):

        req = self._get(f"dragons/{_id}")

        return Dragon(req)

spacex = Spaceman()
print(spacex.get_dragon("5e9d058759b1ff74a7ad5f8f").__slots__)