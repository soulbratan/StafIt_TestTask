import sys

from tabulate import tabulate

from src.cli import parse_args
from src.data_processor import process_country_data, read_csv_files
from src.report_generators import get_report_generator


def main() -> None:
    try:
        args = parse_args()

        # Чтение данных
        data = read_csv_files(args.files)
        group_data = process_country_data(data)

        # Получение генератора отчета
        generator = get_report_generator(args.report)

        # Генерация отчета
        report_data = generator(group_data)

        # Вывод в консоль
        headers = ["Страна", "Средний ВВП"]
        print(
            tabulate(
                report_data, headers=headers, tablefmt="grid", floatfmt=".2f"
            )
        )

    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден - {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except SystemExit:
        # argparse выведет сообщение сам, если не будут введены аргументы
        sys.exit(2)


if __name__ == "__main__":
    main()
