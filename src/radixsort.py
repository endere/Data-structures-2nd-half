"""Radix sort data structure."""


def radix_sort(array):
    """Radix sort data structure function."""
    if len(array) <= 1:
        return array
    buckets = {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': []}
    for i in range(len(str(max(array)))):
        for x in range(len(array)):
            if not isinstance(array[x], int):
                raise TypeError('Must be an integer, please try again.')
            try:
                buckets[str(array[x])[-i - 1]].append(array[x])
            except IndexError:
                buckets['0'].append(array[x])
        array = []
        for z in range(10):
            array += buckets[str(z)]
            buckets[str(z)] = []
    return array


if __name__ == '__main__':  # pragma no cover
    import random
    import datetime
    from functools import reduce
    times = []
    num_runs = 500
    string_length = 5
    for i in range(num_runs):
        data = [i for i in range(string_length)]
        timeA = datetime.datetime.now()
        radix_sort(data)
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('pre sorted')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
    times = []
    string_length = 100
    for i in range(num_runs):
        data = [i for i in range(string_length)]
        timeA = datetime.datetime.now()
        radix_sort(data)
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('pre sorted')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
    times = []
    string_length = 5
    for i in range(num_runs):
        data = [i for i in range(string_length)][::-1]
        timeA = datetime.datetime.now()
        radix_sort(data)
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('reverse order.')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
    times = []
    string_length = 100
    for i in range(num_runs):
        data = [i for i in range(string_length)][::-1]
        timeA = datetime.datetime.now()
        radix_sort(data)
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('reverse order.')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
    times = []
    for i in range(num_runs):
        data = random.sample(range(string_length), string_length)
        timeA = datetime.datetime.now()
        radix_sort(data)
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('random Order.')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
