wallets = {
    'alice': {'currency': 'USD', 'balance': 1200.0},
    'bob': {'currency': 'USD', 'balance': 450.0},
    'carol': {'currency': 'EUR', 'balance': 900.0},
    'dave': {'currency': 'USD', 'balance': 150.0},
}

rows = [
    'TR-100|alice|bob|200',
    'TR-101|bob|dave|700',
    'TR-102|alice|carol|50',
    'TR-103|eve|bob|30',
    'TR-104|dave|dave|10',
    'TR-105|bob|alice|abc',
    'TR-106|bob|dave|100',
]


class TransferError(Exception):
    pass


class TransferFormatError(TransferError):
    pass


class AccountNotFoundError(TransferError):
    pass


class CurrencyMismatchError(TransferError):
    pass


class InsufficientFundsError(TransferError):
    pass


class TransferAmountError(TransferError):
    pass


def parse_transfer(raw):
    transfer_id,from_user,to_user,amount = raw.split('|')
    try:
        amount = int(amount) > 0
    except ValueError:
        raise TransferFormatError('format error')
    
    return {'transfer_id':transfer_id,"from_user":from_user,'to_user':to_user,'amount':amount}

    # TODO: распарсить строку и вернуть dict перевода
    # TODO: при ошибке конвертации amount использовать raise ... from ...
   


def apply_transfer(transfer, wallets):
    not_exist = []
    for el in wallets:
        if el not in rows:
            not_exist.append(el)
    
    for el in rows:
        transfer_id,from_user,to_user,amount = el.split('|')
    
    
     

    # TODO: проверить существование аккаунтов
    # TODO: запретить перевод самому себе
    # TODO: проверить совпадение валют
    # TODO: проверить баланс отправителя
    # TODO: обновить балансы и вернуть dict результата
    pass


def process_batch(rows, wallets):
    # TODO: вернуть (successes, errors)
    pass


# TODO: вызвать process_batch(rows, wallets)
# TODO: вывести успешные переводы
# TODO: вывести ошибки по типам
# TODO: вывести итоговые балансы
# TODO: найти richest_usd_user
