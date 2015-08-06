"""This module contains the radix sort method (radix_srt), which performs an
in-place sort on a passed in list. Radix sort has a best case time
complexity of O(n log n. This implementation of radix sort is stable, but not
adaptive.

References:

Radix Sort in Python
http://www.geekviewpoint.com/python/sorting/radixsort
by Isai Damier
"""


def radix_srt(un_list):
    """Sort a list in place with radix sort.

    args:
        un_list: the list to be sorted.
    """
    radix = 10
    maxLen = False
    tmp, placement = -1, 1

    while not maxLen:
        maxLen = True
        buckets = [list() for num in range(radix)]

        for i in un_list:
            tmp = i // placement
            buckets[tmp % radix].append(i)
            if maxLen and tmp > 0:
                maxLen = False

        a = 0
        for b in range(radix):
            buck = buckets[b]
            for i in buck:
                un_list[a] = i
                a += 1

        placement *= radix


if __name__ == '__main__':
    from random import randint
    WORST_CASE = [randint(9000, 10000) for x in range(1, 10001)]
    BEST_CASE = [randint(0, 9) for x in range(1, 10001)]

    from timeit import Timer

    SETUP = """from __main__ import BEST_CASE, WORST_CASE, radix_srt"""

    best = Timer('radix_srt({})'.format(BEST_CASE), SETUP).timeit(100)

    worst = Timer('radix_srt({})'.format(WORST_CASE), SETUP).timeit(100)

    print("""
        Best case represented as a list with integers between 0 and 9.
        Worst case represented as a list with large integers (here, between
        9000 and 9999).
        """)
    print('Best Case: {}'.format(best))
    print('Worst Case: {}'.format(worst))
