import json
from unittest import TestCase

from service import DataManager


class DataManagerTest(TestCase):

    def setUp(self):
        self.data = DataManager()

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

        expected_data = {
            "first_name": "Татьяна",
            "last_name": "Алексеева",
            "middle_name": "Петровна",
            "company": "ИП Петрова",
            "phone_1": "891212121212",
            "phone_2": "891727718271"

        }

        self.assertEqual(expected_data, records[-1])

    def test_insert_record_with_wrong_type_field(self):
        result = self.data.insert_record(
            first_name=1,
            last_name="Алексеева",
            middle_name="Петровна",
            company="ИП Петрова",
            phone_1="891212121212",
            phone_2="891727718271"

        )
        self.assertFalse(result)

        result = self.data.insert_record(
            first_name="Алена",
            last_name="Алексеева",
            middle_name={"Имя": "Петровна"},
            company="ИП Петрова",
            phone_1="891212121212",
            phone_2="891727718271"

        )
        self.assertFalse(result)

    def test_insert_record_without_fields(self):

        with self.assertRaises(TypeError) as context:
            result = self.data.insert_record(
                first_name="Татьяна",
                last_name="Алексеева",
                middle_name="Петровна",
                company="ИП Петрова"

            )

        self.assertEqual(
            str(TypeError(
                "insert_record() missing 2 required positional arguments: 'phone_1' and 'phone_2'")),
            str(context.exception))
