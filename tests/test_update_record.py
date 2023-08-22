import json
from unittest import TestCase

from service import DataManager


class DataManagerTest(TestCase):

    def setUp(self):
        self.data = DataManager()

    def test_insert_record(self):
        result = self.data.update_record(1,
                                         first_name="Test",
                                         last_name="Test",
                                         company="Test",
                                         phone_1="Test"
                                         )
        self.assertTrue(result)

        expected_data = {
            "last_name": "Test",
            "first_name": "Test",
            "middle_name": "Иванович",
            "company": "Test",
            "phone_1": "Test",
            "phone_2": "+79129998877"
        }

        with open("data.json", "r") as fp:
            data = json.load(fp)

        self.assertEqual(expected_data, data[0])
