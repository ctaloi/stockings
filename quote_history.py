import ystockquote
import datetime
import csv

TODAY = datetime.date.today()


def get_values(stock, start, shares):
    ''' iterate through historical pricing and multiply by amount of shares '''

    quotes = ystockquote.get_historical_prices(stock, start, str(TODAY))

    del quotes[0]  # remove headers
    for line in quotes:
        del line[2:]
        d = float(line[1]) * shares
        line.append(d)
        del line[1]
    return(quotes)


def write_values(values):
    my_file = open('results.csv', 'wb')
    wr = csv.writer(my_file, quoting=csv.QUOTE_ALL)
    wr.writerow(values)


def main():
    ''' get started'''

    write_values(get_values('AAPL', '2011-01-01', 1000))


if __name__ == '__main__':
    main()
