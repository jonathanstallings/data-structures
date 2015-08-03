def insertion_sort(un_list):
    for idx in range(1, len(un_list)):
        current = un_list[idx]
        position = idx

        while position > 0 and un_list[position-1] > current:
            un_list[position] = un_list[position-1]
            position = position - 1

        un_list[position] = current

if __name__ == '__main__':
    pass
