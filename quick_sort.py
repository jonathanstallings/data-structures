"""Doc string to end all doc strings"""


def quick_srt(un_list, low=0, high=-1):
    if high == -1:
        high = len(un_list) - 1
    if high > low:
        pivot = partition(un_list, low, high)

        if pivot > 0:
            quick_srt(un_list, low, pivot-1)
        if pivot > -1:
            quick_srt(un_list, pivot+1, high)


def partition(un_list, low=0, high=-1):
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
    temp = un_list[x]
    un_list[x] = un_list[y]
    un_list[y] = temp


def _choose_pivot(un_list, low=0, high=-1):
    if high == -1:
        high = len(un_list) - 1
    mid = low + int(high - low) // 2

    if un_list[low] == un_list[mid] and un_list[mid] == un_list[high]:
        return mid

    if (
        un_list[low] < un_list[mid] and
        un_list[low] < un_list[high] and
        un_list[mid] < un_list[high]
    ):
        return mid

    elif (
        un_list[mid] < un_list[low] and
        un_list[mid] < un_list[high] and
        un_list[low] < un_list[high]
    ):
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
