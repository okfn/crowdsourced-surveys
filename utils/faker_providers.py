import random
from faker.providers import BaseProvider


class TanzaniaLocation(BaseProvider):

    tanzania_boundaries = {
        "n": -4.187392,
        "s": -8.331082,
        "w": 31.700238,
        "e": 38.166503
    }

    def tz_location(self):
        return {
            "lat": random.uniform(
                self.tanzania_boundaries['n'],
                self.tanzania_boundaries['s']
            ),
            "lon": random.uniform(
                self.tanzania_boundaries['w'],
                self.tanzania_boundaries['e']
            )
        }
