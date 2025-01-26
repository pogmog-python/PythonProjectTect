from typing import Dict, List


def filter_by_state(dictionary_list: List[Dict], value_key: str = "EXECUTED") -> List[Dict]:
    """Принимает список словарей и ключ: state (по умолчанию 'EXECUTED').
    Возвращает новый список словарей, содержащий словари соответствующих ключ"""
    new_dictionary_list = []
    for every_dict in dictionary_list:
        if every_dict["state"] == value_key:
            new_dictionary_list.append(every_dict)
    return new_dictionary_list


def sort_by_date(list_dict: List[Dict], arg_for_sort: bool = True) -> List[Dict]:
    """Принимает список словарей и параметр сортировки(по умолчанию "True" — 'CANCELED').
    Функция возвращает новый список, отсортированный по дате(date)"""
    sort_list = sorted(list_dict, key=lambda every_dict: every_dict["date"], reverse=arg_for_sort)
    return sort_list
