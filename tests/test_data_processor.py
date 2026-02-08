import pytest

from src.data_processor import (calculate_average_gdp, process_country_data,
                                read_csv_files)


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


def test_process_country_data():
    """Группировка данных по странам."""
    test_data = [
        {"country": "USA", "gdp": "1000"},
        {"country": "USA", "gdp": "2000"},
        {"country": "Canada", "gdp": "500"},
    ]

    result = process_country_data(test_data)

    assert result["USA"] == [1000.0, 2000.0]
    assert result["Canada"] == [500.0]
    assert len(result) == 2


def test_process_country_data_invalid_gdp():
    """Пропуск некорректных значений GDP."""
    test_data = [
        {"country": "USA", "gdp": "1000"},
        {"country": "USA", "gdp": "invalid"},  # Пропустится
        {"country": "Canada", "gdp": "500"},
    ]

    result = process_country_data(test_data)

    assert result["USA"] == [1000.0]
    assert result["Canada"] == [500.0]


def test_calculate_average_gdp(country_gdp_dict):
    """Расчет среднего GDP."""
    result = calculate_average_gdp(country_gdp_dict)

    # Проверяем структуру
    assert len(result) == 3
    assert isinstance(result[0], list)
    assert len(result[0]) == 3  # [номер, страна, среднее]

    # Проверяем сортировку по убыванию
    assert result[0][1] == "USA"  # Самый высокий GDP
    assert result[2][1] == "Canada"  # Самый низкий GDP

    # Проверяем расчет среднего
    usa_gdp = next(row[2] for row in result if row[1] == "USA")
    assert usa_gdp == pytest.approx(20500.0)  # (20000 + 21000) / 2


def test_calculate_average_gdp_empty():
    """Расчет для пустых данных."""
    result = calculate_average_gdp({})
    assert result == []
