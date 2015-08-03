"""This module contains the insertion sort method, which performs an
in-place sort on a passed in list. Insertion sort has a best case timeit
complexity of O(n) when list is nearly sorted, and a worst case of O(n2)
when the incoming list is already reverse sorted. While this not always
the most efficient algorithm, it is still popular when the data is nearly
sorted (because it is adaptive) or when the problem size is small.
See the excellent 'sortingalgorithms.com' for more information.

"""


def insertion_sort(un_list):
    """Sort a list in place using insertion sort.

    args:
        un_list: the list to sort
    """
    if type(un_list) is not list:
        return "You must pass a valid list as argument. Do it."

    for idx in range(1, len(un_list)):
        current = un_list[idx]
        position = idx

        while position > 0 and un_list[position-1] > current:
            un_list[position] = un_list[position-1]
            position = position - 1

        un_list[position] = current

if __name__ == '__main__':
    BEST_CASE = range(1000)
    WORST_CASE = BEST_CASE[::-1]

    from timeit import Timer

    best = Timer(
        'insertion_sort({})'.format(BEST_CASE),
        'from __main__ import BEST_CASE, insertion_sort').timeit(1000)

    worst = Timer(
        'insertion_sort({})'.format(WORST_CASE),
        'from __main__ import WORST_CASE, insertion_sort').timeit(1000)

    print("""Best case represented as a list that is already sorted\n
        Worst case represented as a list that is absolute reverse of sorted""")
    print('Best Case: {}'.format(best))
    print('Worst Case: {}'.format(worst))
