import argparse

from service import DataManager


def func_hello():
    return "Hello-world"


def run():
    global_parser = argparse.ArgumentParser(
        prog="phone_book")

    subparsers = global_parser.add_subparsers(
        title="subcommands", help="Телефонный справочник")

    # select
    select_parser = subparsers.add_parser(
        "select_records", help="Вывод всех записей")
    select_parser.add_argument(nargs="*", dest="values", default=[])
    select_parser.set_defaults(func=DataManager.select_all_records)

    # insert
    insert_parser = subparsers.add_parser(
        "insert_record",
        help="Добавить новую запись: Фамилия, Имя, Отчество, Компания, Рабочий тлф, Личный тлф")
    insert_parser.add_argument(nargs=6, dest="values")
    insert_parser.set_defaults(func=DataManager().insert_record)

    # update
    update_parser = subparsers.add_parser(
        "update_record",
        help="Изменить запись: id, Фамилия, Имя, Отчество, Компания, Рабочий тлф, Личный тлф")
    update_parser.add_argument(
        "--id", type=int, action="append", dest="values")
    update_parser.add_argument("--first_name", action="append", dest="values")
    update_parser.add_argument("--last_name", action="append", dest="values")
    update_parser.set_defaults(func=DataManager().update_record)

    args = global_parser.parse_args()
    print(args)
    args.func(*args.values)


if __name__ == "__main__":
    run()
