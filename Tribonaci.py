def tribonacci(n):
    # Проверка входных данных
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Первые три числа Трибоначчи
    trib = [0, 1, 1]
    if n < 3:
        return trib[n]
    
    # Основной цикл для n >= 3
    a, b, c = trib
    for i in range(3, n + 1):
        a, b, c = b, c, a + b + c  # обновление трёх последних чисел
    
    return c

# Пример использования с input
try:
    n = int(input("Введите номер числа Трибоначчи: "))
    result = tribonacci(n)
    print(f"T({n}) = {result}")
except (TypeError, ValueError) as e:
    print(e)
