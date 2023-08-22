import json
from typing import Optional


class DataManager:

    @staticmethod
    def say_hello() -> None:
        print("Добро пожаловать в приложение 'Телефонный справочник'. \n"
              "Для получения справки выполните команду 'python app.py -h'")

    @staticmethod
    def _output_records_as_a_table(records: list,
                                   page: int = 1,
                                   items_per_page: int = 1000) -> list:
        """
        Функция выводит записи в виде таблицы
        """

        # {Индекс|Длина строки}
        template = "{0:5}|{1:10}|{2:10}|{3:15}|{4:23}|{5:17}|{6:15}"
        print(template.format("id", "Фамилия", "Имя",
                              "Отчество", "Название организации",
                              "Рабочий телефон", "Личный телефон"))
        print("-" * 100)

        index = items_per_page * page

        if records:
            for id, record in enumerate(records[index - items_per_page:index],
                                        start=(index - items_per_page) + 1):
                print(template.format(id, *record.values()))
            return records
        else:
            print("Записей не существует")
            return []

    @staticmethod
    def _read_data_json() -> Optional[list]:
        """
        Функция считывает данные из json файла
        """

        try:
            with open("data.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, FileExistsError) as e:
            print(f"Произошла ошибка чтения файла - {e}")
            return None
        except json.JSONDecodeError:
            print(
                "Файл 'data.json' не должен быть пустым. JSON поддерживает: \
                    'None, {}, []'")
            return None

    def _write_data_json(self, data: list) -> bool:
        """
        Функция записывает данные в json файл
        """

        try:
            with open("data.json", "w") as fp:
                json.dump(data, fp, ensure_ascii=False, indent=4)
            return True
        except (FileNotFoundError, FileExistsError) as e:
            print(f"Произошла ошибка записи в файл - {e}")
            return False

    @classmethod
    def select_all_records(cls, page: int = 1,
                           items_per_page: int = 1000) -> Optional[list]:
        """
        Функция выводит список всех записей из файла
        """

        data = cls._read_data_json()

        if data:
            return cls._output_records_as_a_table(data, page, items_per_page)
        return None

    def insert_record(self,
                      first_name: str,
                      last_name: str,
                      middle_name: str,
                      company: str,
                      phone_1: str,
                      phone_2: str) -> Optional[bool]:
        """
        Функция добавляет новую запись в файл
        """

        if not isinstance(first_name, str):
            print("Значение 'first_name' должно быть строкой")
            return False
        if not isinstance(last_name, str):
            print("Значение 'last_name' должно быть строкой")
            return False
        if not isinstance(middle_name, str):
            print("Значение 'middle_name' должно быть строкой")
            return False
        if not isinstance(company, str):
            print("Значение 'company' должно быть строкой")
            return False
        if not isinstance(phone_1, str):
            print("Значение 'phone_1' должно быть строкой")
            return False
        if not isinstance(phone_2, str):
            print("Значение 'phone_2' должно быть строкой")
            return False

        record = {"last_name": last_name,
                  "first_name": first_name,
                  "middle_name": middle_name,
                  "company": company,
                  "phone_1": phone_1,
                  "phone_2": phone_2
                  }

        data = self._read_data_json()

        if data:
            if record not in data:
                data.append(record)
            else:
                print("Запись уже существует")
                return False

            new_data = self._write_data_json(data)

            if new_data:
                print("Запись успешно добавлена")
                return True
        return None

    def update_record(self, record_id: int,
                      last_name: Optional[str] = None,
                      first_name: Optional[str] = None,
                      middle_name: Optional[str] = None,
                      company: Optional[str] = None,
                      phone_1: Optional[str] = None,
                      phone_2: Optional[str] = None
                      ) -> Optional[bool]:
        """
        Функция обновляет выбранную запись
        """

        if not isinstance(record_id, int):
            print("record_id должно быть целым числом")
            return False

        data = self._read_data_json()

        if data:

            if record_id - 1 >= len(data):
                print("Нет записи с таким номером")
                return False

            record = data[record_id - 1]

            if last_name is None:
                last_name = record["last_name"]
            if first_name is None:
                first_name = record["first_name"]
            if middle_name is None:
                middle_name = record["middle_name"]
            if company is None:
                company = record["company"]
            if phone_1 is None:
                phone_1 = record["phone_1"]
            if phone_2 is None:
                phone_2 = record["phone_2"]

            record.update(
                last_name=last_name,
                first_name=first_name,
                middle_name=middle_name,
                company=company,
                phone_1=phone_1,
                phone_2=phone_2
            )

            new_data = self._write_data_json(data)

            if new_data:
                print(f"Запись {record} успешно изменена")
                return True
        return None

    def search_record(self,
                      last_name: Optional[str] = None,
                      first_name: Optional[str] = None,
                      middle_name: Optional[str] = None,
                      company: Optional[str] = None,
                      phone_1: Optional[str] = None,
                      phone_2: Optional[str] = None) -> Optional[list]:
        """
        Функция ищет записи по параметрам
        """

        data = self._read_data_json()

        if data:

            search_fields = []

            if last_name is not None:
                search_fields.append(last_name)
            if first_name is not None:
                search_fields.append(first_name)
            if middle_name is not None:
                search_fields.append(middle_name)
            if company is not None:
                search_fields.append(company)
            if phone_1 is not None:
                search_fields.append(phone_1)
            if phone_2 is not None:
                search_fields.append(phone_2)

            result = []

            for record in data:
                check_list = []
                for field in search_fields:
                    if field in record.values() or field.title() in record.values():
                        check_list.append(True)
                    else:
                        check_list.append(False)

                if all(check_list):
                    result.append(record)

            return self._output_records_as_a_table(result)
        return None
