from masks import get_mask_card_number, get_mask_account


def mask_account_card(user_info: str) -> str:
    """ Функция маскировки карт и счетов"""
    if 'Счет' in user_info:
        return f"Счет {get_mask_account(user_info)}"
    else:
        card_num = get_mask_card_number(user_info[-16:])
        card_mask = user_info.replace(user_info[-16:], card_num)
        return card_mask


