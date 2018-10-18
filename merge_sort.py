"""This module contains the merge_srt method, which performs an
in-place merge sort on a passed in list. Merge sort has a best case time
complexity of O(n log n) when list is nearly sorted, and also a worst case of
O(n log n). Merge sort is a very predictable and stable sort, but it is not
adaptive. See the excellent 'sortingalgorithms.com' for more information.

"""


def merge_srt(un_list):
    """Perform an in-place merge sort on list.

    args:
        un_list: the list to sort
    """
    if len(un_list) > 1:
        mid = len(un_list) // 2
        left_half = un_list[:mid]
        right_half = un_list[mid:]

        merge_srt(left_half)
        merge_srt(right_half)

        x = y = z = 0

        while x < len(left_half) and y < len(right_half):
            if left_half[x] < right_half[y]:
                un_list[z] = left_half[x]
                x += 1
            else:
                un_list[z] = right_half[y]
                y += 1
            z += 1

        while x < len(left_half):
            un_list[z] = left_half[x]
            x += 1
            z += 1

        while y < len(right_half):
            un_list[z] = right_half[y]
            y += 1
            z += 1


if __name__ == '__main__':
    even_half = range(0, 1001, 2)
    odd_half = range(1, 1000, 2)
    BEST_CASE = range(0, 1001)
    WORST_CASE = even_half + odd_half

    from timeit import Timer

    SETUP = """from __main__ import BEST_CASE, WORST_CASE, merge_srt"""

    best = Timer('merge_srt({})'.format(BEST_CASE), SETUP).timeit(1000)

    worst = Timer('merge_srt({})'.format(WORST_CASE), SETUP).timeit(1000)

    print("""Best case represented as a list that is already sorted\n
        Worst case represented as a list that is absolute reverse of sorted""")
    print('Best Case: {}'.format(best))
    print('Worst Case: {}'.format(worst))
