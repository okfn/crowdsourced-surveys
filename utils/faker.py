import random
from faker import Faker
from .faker_providers import TanzaniaLocation
from .api import ApiWrapper


class FakeData():

    data = {}
    fake = Faker()
    api = ApiWrapper()


class FakeTanzaniaData(FakeData):

    wards = [
        "Daa",
        "Dabalo",
        "Dabil",
        "Dalai",
        "Daraja Mbili",
        "Dareda",
        "Digodigo",
        "Dodoma Makulu",
        "Dungunyi",
        "Duru"
    ]

    types = [
        "Pre-school",
        "Primary school",
        "Secondary school"
    ]

    def __init__(self):
        self.fake.add_provider(TanzaniaLocation)

        # # Labels stored separately to easily change them when needed
        # self.labels = {
        #     "school_name": "Name of school",
        #     "ward_name": "Name of ward",
        #     "school_type": "Type of school",
        #     "location": "Location",
        #     "school_address": "School address",
        #     "notes": "Additional notes",
        #     "feedback": "Feedback"
        # }
        # self.data = {v: None for (k, v) in self.labels.items()}
        fake = self.fake

        self.data = {
            "Name of school": fake.name(),
            "Name of ward": random.choice(self.wards),
            "Type of school": random.choice(self.types),
            "Location": fake.tz_location(),
            "School address": fake.street_name(),
            "Additional notes": fake.text(max_nb_chars=90, ext_word_list=None),
            "Feedback": fake.text(max_nb_chars=200, ext_word_list=None)
        }

    def payload(self, form_id):
        attributes = self.api.get_form_attributes(form_id, keys=True)
        # data = {v: self.data[k] for (k, v) in attributes}
        fake = self.fake

        payload = {
            "title": self.data["Name of ward"],
            "content": self.data["Name of school"],
            "values": {
                attributes["Type of school"]: [random.choice(self.types)],
                attributes["Location"]: [fake.tz_location()],
                attributes["School address"]: [fake.street_name()],
                attributes["Additional notes"]: [fake.text(max_nb_chars=90)],
                attributes["Feedback"]: [fake.text(max_nb_chars=200)]
            },
            "form": {
                "id": int(form_id),
            },
        }
        return payload

    def __str__(self):
        return str(self.data)
