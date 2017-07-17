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


if __name__ == '__main__':  # pragma no cover
    import datetime
    from functools import reduce
    times = []
    num_runs = 500
    string_length = 5
    for i in range(num_runs):
        data = [i for i in range(string_length)]
        timeA = datetime.datetime.now()
        insertion_sort(data)
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('Best Case: pre sorted')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
    string_length = 100
    for i in range(num_runs):
        data = [i for i in range(string_length)]
        timeA = datetime.datetime.now()
        insertion_sort(data)
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('Best Case: pre sorted')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
    string_length = 5
    for i in range(num_runs):
        data = [i for i in range(string_length)][::-1]
        timeA = datetime.datetime.now()
        insertion_sort(data)
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('Worst Case: reverse order.')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
    string_length = 100
    for i in range(num_runs):
        data = [i for i in range(string_length)][::-1]
        timeA = datetime.datetime.now()
        insertion_sort(data)
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('Worst Case: reverse order.')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')

