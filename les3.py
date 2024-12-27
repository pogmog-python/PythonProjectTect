def unic_value(list_num_1: list[int], list_num_2: list[int]) -> list[int]:
    """Функция возвращающая уникальные значения из двух списков"""
    # total_list = []
    # for i in list_num_1:
    #     if i != list_num_2:
    #         total_list.append(i)
    return list(set(list_num_1) - set(list_num_2)) + list(set(list_num_2) - set(list_num_1))

print(unic_value([1, 2, 3, 4], [3, 4, 5, 6]))