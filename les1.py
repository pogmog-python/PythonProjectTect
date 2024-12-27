def num_unic_list(list_1:list[int], list_2:list[int]) -> list[int]:
    # total_list =[]
    # for i in list_1:
    #     if i in list_2:
    #         total_list.append(i)
    # return total_list
    return [i for i in list_1 if i in list_2]
if __name__ == "__les1__":
    print(num_unic_list([1, 2, 3, 4], [3, 4, 5, 6]))
