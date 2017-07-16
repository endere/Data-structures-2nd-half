
def insertion_sort(array):
    """."""
    for i in range(len(array)):
        print("-------------------")
        for x in range(len(array[:i])):
            # print(array[:i])
            if array[i] < array[i - x - 1]:
                # print("We made it here")
                pass
            else:
                # print("We made it here not")
                print(array[i], array[i - x - 1])
                array.insert(i - x, array.pop(i))  # (new index, remove old index)
                break
    return array


if __name__ == '__main__':
    import random
    import datetime
    from functools import reduce
    import sys
    times = []
    num_runs = 1
    string_length = 5
    for i in range(num_runs):
        # x = i / num_runs * 100
        # sys.stdout.write("\r%d%%" % x)
        # sys.stdout.flush()
        data = random.sample(range(string_length), string_length)
        timeA = datetime.datetime.now()
        print(data)
        print(insertion_sort(data))
        timeB = datetime.datetime.now()
        times.append(timeB - timeA)
    average_time = reduce(lambda x, y: x + y, times) / len(times)
    print(' ')
    print('Number of runs: ', num_runs)
    print('Length of lists to sort: ', string_length)
    print('Average time: ', str(average_time)[-8:], 'seconds')
