#!/usr/bin/env python
import ystockquote
import datetime
import csv
import argparse
import pprint

TODAY = datetime.date.today()

parser = argparse.ArgumentParser(description='Process some stock quotes')
parser.add_argument('-o', '--output', default=False)
parser.add_argument('-s', '--stock', required=True)
parser.add_argument('-a', '--amount', type=int, required=True)
parser.add_argument('-d', '--start_date', default='2010-01-01')
args = parser.parse_args()


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
    if args.output is False:
        pprint.pprint(values)
    else:
        f_name = args.output + '_' + args.stock + '.csv'
        my_file = open(f_name, 'wb')
        wr = csv.writer(my_file, quoting=csv.QUOTE_ALL)
        for row in values:
            wr.writerow(row)


def main():
    ''' get started'''

    write_values(get_values(args.stock, args.start_date, args.amount))


if __name__ == '__main__':
    main()
