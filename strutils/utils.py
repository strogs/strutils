def str_valid_int(data, to_int=False):
    """
    Проверяет входные данные на наличие типа Integer.
    При условии приводит к типу Integer.
    При указании числа с плавающей точкой, убирает дробную часть и оставляет только целое.

    Args:
        data (any): Любое значение
        to_int (bool): Указывает, возвращать число или логическое значение
    
    Returns:
        bool, int: Значение в зависимости от аргументов
    """
    if data is None or (isinstance(data, str) and data.strip() == ""):
        return 0

    # Проверка int
    if isinstance(data, int):
        return int(data) if to_int else True

    # Проверка float
    if isinstance(data, float):
        return int(data) if to_int else False

    # Проверка строки
    if isinstance(data, str):
        # Проверка на целое число
        if data.isdigit():
            return int(data) if to_int else True
        # Проверка на дробное число
        try:
            float_value = float(data)
            return int(float_value) if to_int else False
        except ValueError:
            return False

    return False
