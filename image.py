def reverse_image(image):
    result = []
    for matrix in image :
        new_matrix = []
        for row in matrix :
            new_row = []
            for number in row : 
                new_row.append(1-number)
            new_matrix.append(new_row)
        result.append(new_matrix)
    return result

def reverse_image_recursive(image):
    if len(image) == 0:
        return []
    else:
        first = image[0]
        if isinstance(first, list):
            # Если элемент - список, обрабатываем рекурсивно
            processed_first = reverse_image_recursive(first)
        else:
            # Если элемент - число, преобразуем в негатив
            processed_first = 1 - first
        
        # Рекурсивно обрабатываем остальную часть
        rest = reverse_image_recursive(image[1:])
        
        return [processed_first] + rest

# Пример входных данных
big_list = [
    [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
    ],
    [
    [1, 1, 1],
    [0, 0, 0]
    ],
    [
    [1, 0, 0],
    [1, 0, 0]
    ]
]

# Исправленный вывод результатов
print("Обычный метод:", reverse_image(big_list))
print("Рекурсивный метод:", reverse_image_recursive(big_list))