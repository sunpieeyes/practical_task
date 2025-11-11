def is_palindrome(string):
    cleaned_string = string.lower().replace(" ","")
    reversed_string = cleaned_string[::-1]
    return cleaned_string == reversed_string
    

def is_palindrome_recursive(string):
    cleaned = string.lower().replace(" ","")
    if len(cleaned) <=1 :
        return True
    elif cleaned[0] == cleaned[-1]:
        return is_palindrome_recursive(cleaned[1:-1])
    else:
        return False
    


# Получение ввода от пользователя
string_input = input("введите строку: ")

# Вывод результатов
print("Обычный метод:", is_palindrome(string_input))
print("Рекурсивный метод:", is_palindrome_recursive(string_input))