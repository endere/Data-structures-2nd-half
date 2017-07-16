
def insertion_sort(array):
    """."""
    for i in range(len(array)):
        for x in range(len(array[:i])):
            if array[i] < array[i - x - 1]:
                if x == len(array[:i]) - 1:
                    array.insert(i - x - 1, array.pop(i))
            else:
                array.insert(i - x, array.pop(i))  # (new index, remove old index)
                break
    # array.insert(2, array.pop(4))
    return array


if __name__ == '__main__':
    import random
    import datetime
    from functools import reduce
    import sys
    times = []
    num_runs = 5000
    string_length = 5
    for i in range(num_runs):
        x = i / num_runs * 100
        sys.stdout.write("\r%d%%" % x)
        sys.stdout.flush()
        data = random.sample(range(string_length), string_length)
        timeA = datetime.datetime.now()
        insertion_sort(data)
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
