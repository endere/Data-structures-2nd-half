"""Implement the bubble sort algorithm."""


def bubble_sort(array):
    """Iterate through list of numbers and continuously swap values until list is sorted."""
    while True:
        flag = True
        for i in range(len(array)):
            if not isinstance(array[i], int):
                raise TypeError('Invalid input.')
            try:
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    flag = False
            except IndexError:
                pass
        if flag is True:
            return array


if __name__ == '__main__':
    import random
    import datetime
    from functools import reduce
    import sys
    times = []
    num_runs = 1
    string_length = 10000
    for i in range(num_runs):
        x = i / num_runs * 100
        sys.stdout.write("\r%d%%" % x)
        sys.stdout.flush()
        data = random.sample(range(string_length), string_length)
        timeA = datetime.datetime.now()
        bubble_sort(data)
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
