import requests
from capsules import Capsule
from company import Company
from cores import Core
from crewmember import CrewMember
from dragon import Dragon
from landingpads import LandingPad
from launches import Launch
from launchpad import LaunchPad
from payloads import Payload
from roadster import Roadster
from rockets import Rocket
from ships import Ship
from starlink import Starlink
from history import HistoricEvent

class Spaceman():

    def __init__(self):
        pass

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

    @property
    def get_payloads(self):

        req = self._get("payloads")

        return [Payload(i) for i in req]

    def payload(self, _id):

        req = self._get(f"payloads/{_id}")

        return Payload(req)

    @property
    def roadster(self):

        req = self._get(f"roadster")

        return Roadster(req)

    @property
    def get_rockets(self):

        req = self._get("rockets")

        return [Rocket(i) for i in req]

    def rocket(self, _id):

        req = self._get(f"rockets/{_id}")

        return Rocket(req)

    @property
    def get_ships(self):

        req = self._get("ships")

        return [Ship(i) for i in req]

    def ship(self, _id):

        req = self._get(f"ships/{_id}")

        return Ship(req)

    @property
    def get_all_starlink(self):

        req = self._get("starlink")

        return [Starlink(i) for i in req]

    def starlink(self, _id):

        req = self._get(f"starlink/{_id}")

        return Starlink(req)

    @property
    def get_historic_events(self):

        req = self._get("history")

        return [HistoricEvent(i) for i in req]

    def historic_event(self, _id):

        req = self._get(f"history/{_id}")

        return HistoricEvent(req)