import pytest

from src.report_generators import (generate_average_gdp_report,
                                   get_report_generator)


def test_get_report_generator_exists():
    """Получение существующего генератора."""
    generator = get_report_generator("average-gdp")
    assert generator is generate_average_gdp_report


def test_get_report_generator_not_exists():
    """Ошибка при получении несуществующего генератора."""
    with pytest.raises(ValueError, match="Неизвестный тип отчета"):
        get_report_generator("non-existent")


def test_generate_average_gdp_report(country_gdp_dict):
    """Генератор отчета возвращает корректные данные."""
    result = generate_average_gdp_report(country_gdp_dict)

    assert len(result) == 3
    assert result[0][1] == "USA"
    assert result[0][2] == pytest.approx(20500.0)
