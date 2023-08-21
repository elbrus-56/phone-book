import argparse


def get_all_records():
    print("Держи результат")


def run():
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('-l', '--list', dest='accumulate', action='store_const',
                        const=get_all_records,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))


if __name__ == "__main__":
    run()
