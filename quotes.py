#!/usr/bin/env python
import ystockquote
import locale

locale.setlocale(locale.LC_ALL, '')

def get_quote(symbol):
    ''' Return quote '''

    quote = float(ystockquote.get_price(symbol))
    return(quote)

def get_change(symbol):
    ''' Return change '''

    change = float(ystockquote.get_change(symbol))
    return(change)

def my_stocks():
    ''' Setup stock holding information '''

    apple = {'name': 'Apple', 'symbol': 'AAPL', 'cost': 427.50, 'shares': 25}
    sonus = {'name': 'Sonus', 'symbol': 'SONS', 'cost': 2.99, 'shares': 100}
    alteva = {'name': 'Alteva', 'symbol': 'ALTV', 'cost': 0, 'shares': 26}

    my_stocks = (apple, sonus, alteva)

    return(my_stocks)

def todays_quotes():

    print ''
    for stock in my_stocks():
        stock_cost = int(stock['cost']*stock['shares'])
        stock_value = int(get_quote(stock['symbol'])*stock['shares'])
        stock_status = stock_value - stock_cost
        print stock['name'], locale.currency(stock_status), get_change(stock['symbol'])
    print ''

def main():
    ''' get started'''

    todays_quotes()

if __name__ == '__main__':
    main()