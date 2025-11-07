def replace_characters(lst, old, new):
    result_list = []
    for string in lst :
        new_string=string.replace(old,new)
        result_list.append(new_string)
    return result_list

# Пример использования
test_list = ["hello", "world"]
old_char = "h"
new_char = "1"

result = replace_characters(test_list, old_char, new_char)
print("Результат:", result)