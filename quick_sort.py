"""Doc string to end all doc strings"""


def quick_srt(un_list):
    _helper(un_list, 0, len(un_list)-1)


def _helper(un_list, first, last):
    if first < last:
        split = _split(un_list, first, last)
        _helper(un_list, first, split-1)
        _helper(un_list, split+1, last)


def _split(un_list, first, last):
    pivot = un_list[first]
    left = first + 1
    right = last

    while True:
        while left <= right and un_list[left] <= pivot:
            left += 1
        while un_list[right] >= pivot and right >= left:
            right -= 1

        if right < left:
            break
        else:
            temp = un_list[left]
            un_list[left] = un_list[right]
            un_list[right] = temp

    temp = un_list[first]
    un_list[first] = un_list[right]
    un_list[right] = temp

    return right


if __name__ == '__main__':
    from random import shuffle
    rands = [2 for num in range(0, 1001)]
    nums = range(0, 1001)
    BEST_CASE = shuffle(nums)
    WORST_CASE = nums

    from timeit import Timer

    SETUP = """from __main__ import BEST_CASE, WORST_CASE, quick_srt"""

    best = Timer('quick_srt({})'.format(BEST_CASE), SETUP).timeit(100)

    worst = Timer('quick_srt({})'.format(WORST_CASE), SETUP).timeit(100)

    print("""
        Best case represented as a list that is 
        Worst case represented as a list that is 
        """)
    print('Best Case: {}'.format(best))
    print('Worst Case: {}'.format(worst))
