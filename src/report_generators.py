from src.data_processor import calculate_average_gdp

REPORT_GENERATORS = {}


def report_generator(report_name: str):
    """Декоратор для регистрации генераторов отчетов."""

    def decorator(func):
        REPORT_GENERATORS[report_name] = func
        return func

    return decorator


@report_generator("average-gdp")
def generate_average_gdp_report(data):
    """Генерация отчета среднего ВВП по странам."""
    return calculate_average_gdp(data)


def get_report_generator(report_name: str):
    """Получение генератора отчета по имени."""
    if report_name not in REPORT_GENERATORS:
        raise ValueError(f"Неизвестный тип отчета: {report_name}")
    return REPORT_GENERATORS[report_name]
