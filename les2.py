def num_polindromes(num_list:list[int]) -> list[int]:
    """Функция выводящая список полиндромов"""
    total_list = []
    for i in num_list:
        if str(i) == str(i)[::-1]:
            total_list.append(i)
    return total_list
print(num_polindromes([121, 123, 131, 34543]))