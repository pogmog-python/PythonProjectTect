from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_info: str) -> str:
    """ Функция маскировки карт и счетов"""
    if 'Счет' in user_info:
        return f"Счет {get_mask_account(user_info)}"
    elif len(user_info) >= 16 and user_info[-16:].isdigit():
        card_num = get_mask_card_number(user_info[-16:])
        card_mask = user_info.replace(user_info[-16:], card_num)
        return card_mask
    else:
        return user_info


def get_date(date: str) -> str:
    """ Функция возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    return f'{date[8:10]}.{date[5:7]}.{date[0:4]}'
