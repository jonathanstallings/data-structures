"""Jonny Five's Docstrings are alive!"""


def radix_srt(un_list):
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
    pass
