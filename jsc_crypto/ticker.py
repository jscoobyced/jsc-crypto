#!/usr/bin/python

import requests

SATANG_URL = "https://api.tdax.com/api/v3/ticker/24hr?symbol="
BINANCE_URL = "https://api.binance.com/api/v3/ticker/24hr?symbol="
URLS = [SATANG_URL, BINANCE_URL]
CURRENCY = "THB"
SELF = "thb_thb"
SYMBOLS = [["DOGE", "doge_thb", 0, 1], ["ADA", "ada_thb", 0, 1],
           ["BTC", "btc_thb", 0, 1], ["TRX", "trx_thb", 0, 1],
            ["THB", "thb_thb", 0, 1], ["SHIB", "SHIBUSDT", 1, 31.25]]
INDEX_DATE = 0
INDEX_QUANTITY = 1
INDEX_VALUE = 2
INDEX_COST = 3


def get_transactions(crypto, data):
    filename = f"{data}/{crypto}.csv"
    file = open(filename, "r")
    if not file:
        return []
    lines = file.readlines()
    transactions = []
    for line in lines:
        values = line.split()
        transactions.append([values[0], float(values[1]),
                             float(values[2]), float(values[3])])
    file.close()
    return transactions


def get_latest(currency, url):
    global SELF
    if SELF == currency:
        return float(1)
    response = requests.get(f"{url}{currency}")
    if response.status_code != 200:
        return -1
    json_data = response.json()
    return float(json_data['lastPrice'])


def get_summary(currency, url, factor, data):
    global INDEX_QUANTITY, INDEX_VALUE, INDEX_COST
    transactions = get_transactions(currency, data)
    latest = get_latest(currency, url) * factor
    total_value = 0
    total_cost = 0
    total_quantity = 0
    for transaction in transactions:
        total_quantity = total_quantity + transaction[INDEX_QUANTITY]
        current_value = transaction[INDEX_QUANTITY] * latest
        total_cost = total_cost + transaction[INDEX_COST]
        total_value = total_value + current_value
    return [total_cost, total_value, latest, total_quantity]


def format_result(summary, with_coin=False):
    profit = "Profit"
    profit_loss = summary[1] - summary[0]
    if profit_loss < 0:
        profit = "Loss"
        profit_loss = -profit_loss
    total_cost = '{:.2f}'.format(summary[0])
    total_value = '{:.2f}'.format(summary[1])
    total_profit = '{:.2f}'.format(profit_loss)
    total_quantity = '{:.5f}'.format(summary[3])
    coins = ""
    if with_coin:
        coins = f"Coins: {total_quantity}, "
    return f"{coins}Cost: {total_cost}, Value: {total_value}, {profit}: {total_profit}"


def get_data(data):
    total_cost = 0
    total_value = 0
    total_quantity = 0
    result = ""

    for symbol in SYMBOLS:
        summary = get_summary(symbol[1], URLS[symbol[2]], symbol[3], data)
        result = result + f"Results for {symbol[0]}: {summary[2]}\n"
        total_cost = total_cost + summary[0]
        total_value = total_value + summary[1]
        total_quantity = total_quantity + summary[3]
        result = result + format_result(summary, True) + "\n"

    result = result + "Final summary:\n"
    result = result + \
        format_result([total_cost, total_value, 0, total_quantity])
    return result
