# Модуль для обработки CSV файлов с макроэкономическими данными.

import csv
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List


def read_csv_files(file_paths: List[Path]) -> List[Dict[str, Any]]:
    """
    Чтение данных из нескольких CSV файлов.
    Args:
        file_paths: Список путей к CSV файлам
    Returns:
        Список словарей с данными
    """
    all_data = []

    for file_path in file_paths:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            all_data.extend(list(reader))

    return all_data

def process_country_data(data: List[Dict[str, Any]]) -> Dict[str, List[float]]:
    """
    Группировка данных по странам для расчета среднего ВВП.

    Args:
        data: Список словарей с данными

    Returns:
        Словарь: страна -> список значений ВВП
    """
    country_gdp = defaultdict(list)

    for el in data:
        country = el["country"]
        try:
            gdp = float(el["gdp"])
            country_gdp[country].append(gdp)
        except (ValueError, KeyError):
            continue

    return country_gdp

def calculate_average_gdp(
    country_gdp: Dict[str, List[float]],
) -> list[list[object]]:
    """
    Расчет среднего ВВП по странам.

    Args:
        country_gdp: Словарь страна -> список значений ВВП

    Returns:
        Список списков [Страна, средний ВВП] отсортированные по ВВП
    """
    averages = {}

    for country, gdp_values in country_gdp.items():
        if gdp_values:
            averages[country] = statistics.mean(gdp_values)
        else:
            averages[country] = 0.0

    # Сортируем по убыванию ВВП
    averages = dict(
        sorted(averages.items(), key=lambda item: item[1], reverse=True)
    )

    # Преобразуем в удобный формат для tabulate и добавляем нумерацию
    table_dict = [
        [i, k, v] for i, (k, v) in enumerate(averages.items(), start=1)
    ]
    return table_dict