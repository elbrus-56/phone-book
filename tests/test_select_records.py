import json
from unittest import TestCase, skip

from service import DataManager


class DataManagerTest(TestCase):

    def setUp(self):
        self.data = DataManager()

    def test_select_all_data(self):
        result = self.data.select_all_records()
        with open("../phone_book/data.json", "r") as fp:
            records = json.load(fp)

        self.assertEqual(records, result)

    @skip("Работает с пустым файлом")
    def test_select_all_data_with_clear_file(self):
        result = self.data.select_all_records()
        self.assertFalse(result)
