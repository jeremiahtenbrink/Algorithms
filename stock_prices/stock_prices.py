#!/usr/bin/python

import argparse


def find_max_profit(prices):
    min = None
    max_profit = None
    for i, price in enumerate(prices):
        if i > 0 and (max_profit is None or max_profit < price - min):
            max_profit = price - min

        if min is None or min > price:
            min = price

    if max_profit is not None:
        return max_profit

    return 0


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description = 'Find max profit from prices.')
    parser.add_argument('integers', metavar = 'N', type = int, nargs = '+',
                        help = 'an integer price')
    args = parser.parse_args()

    print(
        "A profit of ${profit} can be made from the stock prices {prices}.".format(
            profit = find_max_profit(args.integers), prices = args.integers))
