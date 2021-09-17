import requests
from capsules import Capsule
from company import Company
from cores import Core
from crewmember import CrewMember
from dragon import Dragon
from landingpads import LandingPad
from launches import Launch
from launchpad import LaunchPad

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
    def get_crew_members(self):

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

    @property
    def get_landpads(self):

        req = self._get("landpads")

        return [LandingPad(i) for i in req]

    def get_landpad(self, _id):

        req = self._get(f"Landpads/{_id}")

        return LandingPad(req)

    @property
    def get_launches(self):

        req = self._get("launches")

        return [Launch(i) for i in req]

    def get_launch(self, _id):

        req = self._get(f"launches/{_id}")

        return Launch(req)

    def latest_launch(self):

        req = self._get("launches/latest")

        return Launch(req)

    def next_launch(self):

        req = self._get("launches/next")

        return Launch(req)

    @property
    def upcoming_launches(self):

        req = self._get("launches/upcoming")

        return [Launch(i) for i in req]

    @property
    def get_launchpads(self):

        req = self._get("launchpads")

        return [LaunchPad(i) for i in req]

    def launchpad(self, _id):

        req = self._get(f"launchpads/{_id}")

        return LaunchPad(req)
