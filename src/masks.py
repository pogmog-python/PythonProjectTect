import logging

# Настройка логирования для модуля masks
logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)  # Установим уровень логирования не ниже DEBUG

# Создание обработчика
file_handler = logging.FileHandler('../logs/masks.log', mode='a', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)  # Записываем все сообщения от DEBUG и выше

# Создание форматировщика
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(card_num: str) -> str:
    """Функция маскировки номера банковской карты"""
    if not card_num:  # Проверка на пустую строку
        logger.warning('Попытка маскировки пустого номера карты.')
        return "  ** ****  "

    total_card_num = str(card_num)
    masked_card_num = f"{total_card_num[:4]} {total_card_num[4:6]}** **** {total_card_num[-4:]}"
    logger.info(f'Маскированный номер карты: {masked_card_num}')
    return masked_card_num


def get_mask_account(acc_num: str) -> str:
    """Функция маскировки номера банковского счета"""
    if not acc_num:  # Проверка на пустую строку
        logger.warning('Попытка маскировки пустого номера счета.')
        return "**"

    total_acc_num = str(acc_num)
    masked_acc_num = f"**{total_acc_num[-4:]}"
    logger.info(f'Маскированный номер счета: {masked_acc_num}')
    return masked_acc_num


# Пример использования
if __name__ == "__main__":
    print(get_mask_card_number("1234567812345678"))  # Пример успешного вызова
    print(get_mask_account("12345678901234567890"))  # Пример успешного вызова
    print(get_mask_card_number(""))  # Пример вызова с пустым номером карты
    print(get_mask_account(""))  # Пример вызова с пустым номером счета
