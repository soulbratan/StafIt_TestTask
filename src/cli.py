import argparse


def parse_args() -> argparse.Namespace:
    """
    Функция для работы с аргументами из коммандной строки.
    --files: путь к файлам;
    --report: название отчёта.
    """
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
