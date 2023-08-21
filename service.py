import json


class DataManager:

    def select_all_records(self) -> None:
        """
        Функция выводит список всех записей из файла
        """
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, FileExistsError) as e:
            print(f"Произошла ошибка чтения файла - {e}")
            return False
        except json.JSONDecodeError:
            print(
                "Файл 'data.json' не должен быть пустым. JSON поддерживает: 'None, {}, []'")
            return False
        else:

            # {Индекс|Длина строки}
            template = "{0:5}|{1:10}|{2:10}|{3:15}|{4:23}|{5:17}|{6:15}"
            print(template.format("id", "Фамилия", "Имя",
                                  "Отчество", "Название организации",
                                  "Рабочий телефон", "Личный телефон"))
            print("-" * 100)

            if data:
                for id, record in enumerate(data, start=1):
                    print(template.format(id, *record.values()))
                return data
            else:
                print("Записей не существует")
                return []

    def insert_record(self,
                      first_name: str,
                      last_name: str,
                      middle_name: str,
                      company: str,
                      phone_1: str,
                      phone_2: str) -> bool:
        """
        Функция добавляет новую запись в файл
        :return: True | False
        """

        record = {"last_name": last_name,
                  "first_name": first_name,
                  "middle_name": middle_name,
                  "company": company,
                  "phone_1": phone_1,
                  "phone_2": phone_2
                  }
        try:
            with open("data.json", "r") as fp:
                data = json.load(fp)
        except (FileNotFoundError, FileExistsError) as e:
            print(f"Произошла ошибка чтения файла - {e}")
            return False
        else:
            if record not in data:
                data.append(record)
            else:
                print("Запись уже существует")
                return False

        try:
            with open("data.json", "w") as fp:
                json.dump(data, fp, ensure_ascii=False, indent=4)
        except (FileNotFoundError, FileExistsError) as e:
            print(f"Произошла ошибка записи в файл - {e}")
            return False
        else:
            print("Запись успешно добавлена")
            return True

    def update_record(self) -> str:
        """
        Функция обновляет выбранную запись
        """
        pass

    def search_record(self) -> list:
        """
        Функция ищет запись по параметрам
        """
        pass
