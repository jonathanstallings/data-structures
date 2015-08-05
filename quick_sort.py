"""This module contains the quick sort method (quick_srt), which performs an
in-place sort on a passed in list. Quick sort has a best case time
complexity of O(n log n) when all elements are equal, and a worst case of
O(n2). Quick sort is not stable or adaptive, but it is robust and has low
overhead.

See the excellent 'sortingalgorithms.com' for more information.
"""


def quick_srt(un_list):
    """Sort a list in place with quick sort.

    args:
        un_list: the list to be sorted
    """
    _quick_srt(un_list, low=0, high=-1)


def _quick_srt(un_list, low=0, high=-1):
    """Sort a list in place with quick sort.

    args:
        un_list: the list to be sorted
        low: index lower bound
        high: the index upper bound
    """
    if high == -1:
        high = len(un_list) - 1
    if high > low:
        pivot = _partition(un_list, low, high)

        if pivot > 0:
            _quick_srt(un_list, low, pivot-1)
        if pivot > -1:
            _quick_srt(un_list, pivot+1, high)


def _partition(un_list, low=0, high=-1):
    """Partition the list into values less than and greater than pivot.

    If the the partitioned sublist contains at least two uniqe values,
    the pivot index is returned. Else, a value of -1 is returned, which
    will end any further recursive calls to _quick_srt.

    args:
        un_list: the list to be sorted
        low: index lower bound
        high: the index upper bound

    returns: the pivot index or -1
    """
    if high == -1:
        high = len(un_list) - 1
    pivot = _choose_pivot(un_list, low, high)
    _swap(un_list, pivot, high)
    j = low
    for i in range(low, high+1):
        if un_list[i] < un_list[high]:
            _swap(un_list, i, j)
            j += 1

    _swap(un_list, high, j)
    for i in range(low, high):
        if un_list[i] != un_list[i+1]:
            return j

    return -1


def _swap(un_list, x, y):
    """Swap the values at two index positions in list.

    args:
        un_list: the list to act upon
        x: index to first element
        y: index to second element
    """
    temp = un_list[x]
    un_list[x] = un_list[y]
    un_list[y] = temp


def _choose_pivot(un_list, low=0, high=-1):
    """Choose a pivot for quick sort.

    args:
        un_list: the list to be sorted
        low: index lower bound
        high: the index upper bound

    returns: the pivot index
    """
    if high == -1:
        high = len(un_list) - 1
    mid = low + (high - low) // 2

    if un_list[low] == un_list[mid] and un_list[mid] == un_list[high]:
        return mid

    if (un_list[low] < un_list[mid]
            and un_list[low] < un_list[high]
            and un_list[mid] < un_list[high]):
        return mid

    elif (un_list[mid] < un_list[low]
            and un_list[mid] < un_list[high]
            and un_list[low] < un_list[high]):
        return low

    else:
        return high


if __name__ == '__main__':
    from random import randint
    rands = [randint(1, 10001) for x in range(1, 10001)]
    dupes = [1 for x in range(1, 10001)]
    nums = range(0, 10001)
    BEST_CASE = dupes
    WORST_CASE = rands

    from timeit import Timer

    SETUP = """from __main__ import BEST_CASE, WORST_CASE, quick_srt"""

    best = Timer('quick_srt({})'.format(BEST_CASE), SETUP).timeit(100)

    worst = Timer('quick_srt({})'.format(WORST_CASE), SETUP).timeit(100)

    print("""
        Best case represented as a list that being a list of the same values.
        Worst case represented as a list that is random numbers.
        """)
    print('Best Case: {}'.format(best))
    print('Worst Case: {}'.format(worst))
