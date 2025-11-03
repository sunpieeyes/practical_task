def how_many_times(message):
    if not isinstance(message, str):  # проверка типа
        raise TypeError("Input must be a string")
    
    total = 0
    for char in message:
        if char == ' ':  # пропускаем пробелы
            continue
        if not ('a' <= char <= 'z'):  # проверка символов
            raise ValueError("String must contain only lowercase a-z letters or spaces")
        total += ord(char) - ord('a') + 1
    return total

# Пример использования с вводом от пользователя
try:
    user_input = input("Введите строку (только строчные буквы a-z и пробелы): ")
    result = how_many_times(user_input)
    print(f"Сумма порядковых номеров букв: {result}")
except (TypeError, ValueError) as e:
    print("Ошибка:", e)
