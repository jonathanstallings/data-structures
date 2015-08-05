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
        while right >= left and un_list[right] >= pivot:
            right += 1

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
    pass
