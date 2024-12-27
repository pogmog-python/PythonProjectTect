def get_mask_card_number(card_num: int) -> str:
    """Функция маскировки номера банковской карты"""
    total_card_num = str(card_num)
    return f"{total_card_num[:4]} {total_card_num[4:6]}** **** {total_card_num[-4:]}"


def get_mask_account(acc_num: int) -> str:
    """Функция маскировки номера банковского счета"""
    total_acc_num = str(acc_num)
    return f"**{total_acc_num[-4:]}"
