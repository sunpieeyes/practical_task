def count_char(lst, char):
    result = []
    for string in lst:
        count = string.count(char)
        result.append(count)
    return result

# Пример использования
test_list = ["helloo", "world"]
char_to_count = "w"

result = count_char(test_list, char_to_count)
print("Результат:", result)