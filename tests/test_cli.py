import sys
from unittest.mock import patch

import pytest

from src.cli import parse_args


def test_cli_valid_args() -> None:
    """Корректные аргументы."""
    test_args = [
        "script.py",
        "--files",
        "a.csv",
        "b.csv",
        "--report",
        "average-gdp",
    ]

    with patch.object(sys, "argv", test_args):
        args = parse_args()

        assert args.files == ["a.csv", "b.csv"]
        assert args.report == "average-gdp"


def test_cli_missing_files() -> None:
    """Отсутствует обязательный аргумент --files."""
    test_args = ["script.py", "--report", "average-gdp"]

    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit):
            parse_args()


def test_cli_missing_report() -> None:
    """Отсутствует обязательный аргумент --report."""
    test_args = ["script.py", "--files", "data.csv"]

    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit):
            parse_args()
