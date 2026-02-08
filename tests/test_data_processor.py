import pytest
from src.data_processor import (
    read_csv_files,
)


def test_read_csv_files(sample_csv_file):
    """Чтение CSV файла работает корректно."""
    data = read_csv_files([sample_csv_file])

    assert len(data) == 6  # 6 строк данных (без заголовка)
    assert data[0]["country"] == "USA"
    assert data[0]["gdp"] == "20000"


def test_read_csv_files_not_found():
    """Ошибка при отсутствии файла."""
    with pytest.raises(FileNotFoundError):
        read_csv_files("non_existent.csv")