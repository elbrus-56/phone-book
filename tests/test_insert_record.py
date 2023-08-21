import json
from unittest import TestCase

from service import DataManager


class DataManagerTest(TestCase):

    def setUp(self):
        self.data = DataManager()
        self.result = {
            "first_name": "Татьяна",
            "last_name": "Алексеева",
            "middle_name": "Петровна",
            "company": "ИП Петрова",
            "phone_1": "891212121212",
            "phone_2": "891727718271"

        }

    def test_insert_record(self):
        result = self.data.insert_record(
            first_name="Татьяна",
            last_name="Алексеева",
            middle_name="Петровна",
            company="ИП Петрова",
            phone_1="891212121212",
            phone_2="891727718271"

        )
        self.assertTrue(result)

        result = self.data.insert_record(
            first_name="Татьяна",
            last_name="Алексеева",
            middle_name="Петровна",
            company="ИП Петрова",
            phone_1="891212121212",
            phone_2="891727718271"

        )
        self.assertFalse(result)

        with open("../phone_book/data.json", "r") as fp:
            records = json.load(fp)

        self.assertEqual(self.result, records[-1])
