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


if __name__ == '__main__':  # pragma no cover
    import datetime
    from functools import reduce
    times = []
    num_runs = 500
    string_length = 5
    for i in range(num_runs):
        data = [i for i in range(string_length)]
        timeA = datetime.datetime.now()
        bubble_sort(data)
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('Best Case: pre sorted')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
    times = []
    string_length = 100
    for i in range(num_runs):
        data = [i for i in range(string_length)]
        timeA = datetime.datetime.now()
        bubble_sort(data)
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('Best Case: pre sorted')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
    times = []
    string_length = 5
    for i in range(num_runs):
        data = [i for i in range(string_length)][::-1]
        timeA = datetime.datetime.now()
        bubble_sort(data)
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('Worst Case: reverse order.')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
    times = []
    string_length = 100
    for i in range(num_runs):
        data = [i for i in range(string_length)][::-1]
        timeA = datetime.datetime.now()
        bubble_sort(data)
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('Worst Case: reverse order.')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
