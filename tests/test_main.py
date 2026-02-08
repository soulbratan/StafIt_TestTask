import sys # noqa
from unittest.mock import patch

from main import main


def test_main_success():
    """Успешный запуск main."""

    test_args = ["script.py", "--files", "test.csv", "--report", "average-gdp"]

    with patch("sys.argv", test_args):
        with patch("main.read_csv_files") as mock_read:
            mock_read.return_value = [
                {"country": "USA", "gdp": "1000"},
                {"country": "Canada", "gdp": "500"},
            ]

            with patch("main.tabulate") as mock_tabulate:
                mock_tabulate.return_value = "Таблица"

                with patch("builtins.print") as mock_print:
                    # Должно завершиться без ошибок
                    main()

                    # Проверяем, что вывод был
                    mock_print.assert_called_once_with("Таблица")


def test_main_file_not_found():
    """Файл не найден."""

    test_args = [
        "script.py",
        "--files",
        "missing.csv",
        "--report",
        "average-gdp",
    ]

    with patch("sys.argv", test_args):
        with patch(
            "main.read_csv_files",
            side_effect=FileNotFoundError("Файл не найден"),
        ):
            with patch("sys.exit") as mock_exit:
                main()
                mock_exit.assert_called_once_with(1)


def test_main_invalid_report():
    """Неизвестный тип отчета."""

    test_args = ["script.py", "--files", "data.csv", "--report", "invalid"]

    with patch("sys.argv", test_args):
        with patch("main.read_csv_files"):
            with patch(
                "main.get_report_generator",
                side_effect=ValueError("Неизвестный отчет"),
            ):
                with patch("sys.exit") as mock_exit:
                    main()
                    mock_exit.assert_called_once_with(1)
