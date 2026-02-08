import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Анализ макроэкономических данных"
    )
    parser.add_argument(
        "--files", nargs="+", required=True, help="Пути к CSV файлам с данными"
    )
    parser.add_argument(
        "--report", required=True, help="Тип отчета (average-gdp)"
    )
    return parser.parse_args()
