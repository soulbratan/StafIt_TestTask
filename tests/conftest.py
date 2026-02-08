from typing import Generator

import pytest
import tempfile
import csv
from pathlib import Path


@pytest.fixture
def sample_csv_file() -> Generator:
    """Создает временный CSV файл с тестовыми данными."""
    data = [
        ["country", "gdp", "year"],
        ["USA", "20000", "2020"],
        ["USA", "21000", "2021"],
        ["Canada", "1800", "2020"],
        ["Canada", "1900", "2021"],
        ["Germany", "3800", "2020"],
        ["Germany", "3900", "2021"],
    ]

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".csv", delete=False, encoding="utf-8"
    ) as f:
        writer = csv.writer(f)
        writer.writerows(data)

    file_path = Path(f.name)
    yield file_path

    # Удаляем после теста
    if file_path.exists():
        file_path.unlink()