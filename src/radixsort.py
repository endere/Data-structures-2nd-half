"""Merge sort data structure."""


def radix_sort(array):
    """Merge sort data structure function."""


if __name__ == '__main__':
    import random
    import datetime
    from functools import reduce
    times = []
    num_runs = 5
    string_length = 5
    for i in range(num_runs):
        data = random.sample(range(string_length), string_length)
        timeA = datetime.datetime.now()
        print(radix_sort(data))
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
