
def insertion_sort(array):
    """."""



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
        print(insertion_sort(data))
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
