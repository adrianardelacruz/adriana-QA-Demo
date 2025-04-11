EXCHANGE_RATE = 56.0  # 1 USD = 56 PHP


def php_to_usd(php_amount):
    return round(php_amount / EXCHANGE_RATE, 2)


def usd_to_php(usd_amount):
    return round(usd_amount * EXCHANGE_RATE, 2)
