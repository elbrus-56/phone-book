import json
from unittest import TestCase

from service import DataManager


class DataManagerTest(TestCase):

    def setUp(self):
        self.data = DataManager()

    def test_search_record_with_correct_field(self):
        result = self.data.search_record(
            first_name="Иван"
        )

        expexted_data = [{
            "last_name": "Иванов",
            "first_name": "Иван",
            "middle_name": "Иванович",
            "company": "ООО Компания 1",
            "phone_1": "+73519998877",
            "phone_2": "+79129998877"
        }]
        self.assertEqual(expexted_data, result)

        result = self.data.search_record(
            first_name="Иванович"
        )

        expexted_data = [
            {
                "last_name": "Иванов",
                "first_name": "Иван",
                "middle_name": "Иванович",
                "company": "ООО Компания 1",
                "phone_1": "+73519998877",
                "phone_2": "+79129998877"
            },
            {
                "last_name": "Петров",
                "first_name": "Сергей",
                "middle_name": "Иванович",
                "company": "ООО Компания 2",
                "phone_1": "+73219998877",
                "phone_2": "+79229928837"
            }]

        self.assertEqual(expexted_data, result)

    def test_search_record_with_wrong_field(self):
        result = self.data.search_record(
            first_name="qwqwssss"
        )
        self.assertEqual([], result)

    def test_search_record_with_correct_and_wrong_fields(self):
        result = self.data.search_record(
            first_name="Иван",
            last_name="qwert"

        )
        self.assertEqual([], result)
