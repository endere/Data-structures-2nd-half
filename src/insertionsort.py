"""Insertion Sort data structure."""


def insertion_sort(array):
    """Function for our insertion sort data structure."""
    for i in range(len(array)):
        if not isinstance(array[i], int):
            raise TypeError('Must be an integer, please try again.')
        for x in range(len(array[:i])):
            if array[i] < array[i - x - 1]:
                if x == len(array[:i]) - 1:
                    array.insert(i - x - 1, array.pop(i))
            else:
                array.insert(i - x, array.pop(i))
                break

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
        print(insertion_sort(data))
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
