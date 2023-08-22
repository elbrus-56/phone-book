import argparse

from service import DataManager


def run() -> None:
    """
    Функция формирует интерфейс командной строки
    """

    global_parser = argparse.ArgumentParser(prog="phone_book")

    subparsers = global_parser.add_subparsers(
        title="subcommands", help="Телефонный справочник (Фамилия, Имя, Отчество, \
            Компания, Рабочий тлф, Личный тлф)")

    # select
    select_parser = subparsers.add_parser(
        "select_records", help="Вывод всех записей")
    select_parser.add_argument(nargs="*", dest="values", default=[])
    select_parser.set_defaults(func=DataManager.select_all_records)

    # insert
    insert_parser = subparsers.add_parser(
        "insert_record",
        help="Добавить новую запись")

    insert_parser.add_argument("--first_name", nargs="?", action="append",
                               dest="values", required=True, help="Обязательное поле")
    insert_parser.add_argument("--last_name", nargs="?", action="append",
                               dest="values", required=True, help="Обязательное поле")
    insert_parser.add_argument("--middle_name", nargs="?", action="append",
                               dest="values", required=True, help="Обязательное поле")
    insert_parser.add_argument("--company", nargs="?", action="append",
                               dest="values", required=True, help="Обязательное поле")
    insert_parser.add_argument("--phone_1", nargs="?", action="append",
                               dest="values", required=True, help="Обязательное поле")
    insert_parser.add_argument("--phone_2", nargs="?", action="append",
                               dest="values", required=True, help="Обязательное поле")

    insert_parser.set_defaults(func=DataManager().insert_record)

    # update
    update_parser = subparsers.add_parser(
        "update_record",
        help="Изменить запись")

    update_parser.add_argument("--id", nargs="?", type=int, action="append",
                               dest="values", help="Обязательное поле",
                               required=True)
    update_parser.add_argument(
        "--first_name", nargs="?", action="append", dest="values")
    update_parser.add_argument(
        "--last_name", nargs="?", action="append", dest="values")
    update_parser.add_argument(
        "--middle_name", nargs="?", action="append", dest="values")
    update_parser.add_argument(
        "--company", nargs="?", action="append", dest="values")
    update_parser.add_argument(
        "--phone_1", nargs="?", action="append", dest="values")
    update_parser.add_argument(
        "--phone_2", nargs="?", action="append", dest="values")

    update_parser.set_defaults(func=DataManager().update_record)

    # search
    update_parser = subparsers.add_parser(
        "search_record",
        help="Найти запись")
    update_parser.add_argument(
        "--first_name", nargs="?", action="append", dest="values")
    update_parser.add_argument(
        "--last_name", nargs="?", action="append", dest="values")
    update_parser.add_argument(
        "--middle_name", nargs="?", action="append", dest="values")
    update_parser.add_argument(
        "--company", nargs="?", action="append", dest="values")
    update_parser.add_argument(
        "--phone_1", nargs="?", action="append", dest="values")
    update_parser.add_argument(
        "--phone_2", nargs="?", action="append", dest="values")

    update_parser.set_defaults(func=DataManager().search_record)

    args = global_parser.parse_args()
    args.func(*args.values)


if __name__ == "__main__":
    run()
