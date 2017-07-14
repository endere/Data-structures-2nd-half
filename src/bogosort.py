import random

def bogo_sort(to_sort):
    while not is_sorted(to_sort):
        random.shuffle(to_sort)
    return to_sort


def is_sorted(to_sort):
    # for i in to_sort:
    #     try:
    #         if to_sort[i] > to_sort[i + 1]:
    #             return False
    #     except IndexError:
    #         pass
    # return True
    return all(a <= b for a, b in zip(to_sort[:-1], to_sort[1:]))

if __name__ == '__main__':
    import datetime
    from functools import reduce
    import sys
    times = []
    num_runs = 5
    string_length = 5
    for i in range(num_runs):
        x = i / num_runs * 100
        sys.stdout.write("\r%d%%" % x)
        sys.stdout.flush()
        data = random.sample(range(string_length), string_length)
        timeA = datetime.datetime.now()
        print(bogo_sort(data))
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    print(' ')
    print('highest: ', max(times))
    print('lowest: ', min(times))
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
    print(bogo_sort([5, 1, 2, 3, 3, 4]))