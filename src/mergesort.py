"""Merge sort data structure."""


def merge_sort(array):
    """Merge sort data structure function."""
    if len(array) > 1:
        if len(array) % 2 == 0:
            half = int(len(array) / 2)
        else:
            half = int(len(array) / 2 + .5)
        left_half = array[:half]
        right_half = array[half:]
        merge_sort(left_half)
        merge_sort(right_half)
        main_count = 0
        left_count = 0
        right_count = 0
        pass
        while left_count < len(left_half) and right_count < len(right_half):
            if left_half[left_count] < right_half[right_count]:
                array[main_count] = left_half[left_count]
                main_count += 1
                left_count += 1
            else:
                array[main_count] = right_half[right_count]
                main_count += 1
                right_count += 1
        while left_count < len(left_half):
            array[main_count] = left_half[left_count]
            main_count += 1
            left_count += 1
        while right_count < len(right_half):
            array[main_count] = right_half[right_count]
            main_count += 1
            right_count += 1
    else:
        if len(array) == 0:
            return array
        if not isinstance(array[0], int):
            raise TypeError('Must be an integer, please try again.')
    return array


if __name__ == '__main__':
    import random
    import datetime
    from functools import reduce
    import sys
    times = []
    num_runs = 5
    string_length = 5
    for i in range(num_runs):
        data = random.sample(range(string_length), string_length)
        timeA = datetime.datetime.now()
        print(merge_sort(data))
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
