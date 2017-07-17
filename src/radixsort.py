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


if __name__ == '__main__':
    import random
    import datetime
    from functools import reduce
    times = []
    num_runs = 5
    string_length = 1000
    for i in range(num_runs):
        data = random.sample(range(string_length), 10)
        timeA = datetime.datetime.now()
        print(radix_sort(data))
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
