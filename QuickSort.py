# coding=utf-8
import numpy


def fast_sort(num_list):
    if len(num_list) < 2:
        return num_list

    i = 0
    j = len(num_list) - 1
    base = num_list[i]

    while i != j:

        while num_list[j] >= base and j > i:
            j -= 1

        while num_list[i] <= base and i < j:
            i += 1

        if i != j:
            temp = num_list[i]
            num_list[i] = num_list[j]
            num_list[j] = temp
        else:
            temp = num_list[i]
            num_list[i] = base
            num_list[0] = temp

    result = fast_sort(num_list[0:i])
    result.extend([num_list[i]])
    result.extend(fast_sort(num_list[i+1:]))

    return result


if __name__ == '__main__':
    nums = [0, 5, 4, 8, 9, 7, 3, 1, 2, 6]
    print fast_sort(nums)

