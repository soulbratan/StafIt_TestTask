# Модуль для обработки CSV файлов с макроэкономическими данными.

import csv
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