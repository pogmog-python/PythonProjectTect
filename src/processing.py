from typing import Dict, List


def filter_by_state(last_dict: List[Dict], value_key: str = "EXECUTED") -> List[Dict]:
    """Принимает список словарей и ключ: state (по умолчанию 'EXECUTED').
    Возвращает новый список словарей, содержащий словари соответствующих ключ"""
    new_list_dict = []
    for every_dict in last_dict:
        if every_dict["state"] == value_key:
            new_list_dict.append(every_dict)
    return new_list_dict


def sort_by_date(list_dict: List[Dict], arg_for_sort: bool = True) -> List[Dict]:
    """Принимает список словарей и параметр сортировки(по умолчанию "True" — 'CANCELED').
    Функция возвращает новый список, отсортированный по дате(date)"""
    sort_list = sorted(list_dict, key=lambda every_dict: every_dict["date"], reverse=arg_for_sort)
    return sort_list
