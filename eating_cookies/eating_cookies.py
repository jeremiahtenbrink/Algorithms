#!/usr/bin/python

import sys


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache = None):
    if n == 0:
        return 1
    cache = [1, 2, 4]
    if n < 3:
        return cache[n - 1]
    for i in range(3, n):
        cache.append(cache[i - 1] + cache[i - 2] + cache[i - 3])
    return cache[n - 1]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print(
            "There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
                ways = eating_cookies(num_cookies), n = num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
