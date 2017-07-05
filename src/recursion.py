"""A code to test recursion speed and breaking point versus a while loop point of reference."""
import datetime
def recursion(x):
    """Recursively counts down from the input number."""
    print(x)
    if x > 0:
        recursion(x - 1)
    print(x)
    
def while_loop(x):
    """Uses a while loop to count down from the input number."""
    while x > 0:
        x -= 1


if __name__ == '__main__':  
    number = 10
    #run this code with increasingly high numbers.
    #10, 100, 1000, etc
    timeA = datetime.datetime.now()
    # while_loop(number)
    timeB = datetime.datetime.now()
    print('while loop took ', timeB - timeA)
    timeA = datetime.datetime.now()
    recursion(number)
    timeB = datetime.datetime.now()
    print('recursion took ', timeB - timeA)


        def print_tree(self):
        current = [self.root, 0]
        the_list = []
        depth = 0
        final = []
        temp = []
        lines = []
        while current:
            final.append([current[0].value, current[1]])
            current[0].left and the_list.append([current[0].left, current[1] + 1])
            current[0].right and the_list.append([current[0].right, current[1] + 1])
            depth = current[1]
            try:
                current = the_list.pop(0)
            except IndexError:
                tree = [[]]
                otherTree= []
                for i in range(depth):
                    tree.append([])
                for i in final:
                    tree[i[1]].append(i[0])
                longest = 0
                for i in tree:
                    print(i)
                    if len(i) > longest:
                        longest = len(i)
                string = ' ' * 2 * longest
                if longest % 2 == 0:
                    longest += 1
                midpoint = int(longest/2 + .5)
                print(midpoint)
                for i in range(longest*20):
                    otherTree.append(' ')
                curr = [self.root, 0, midpoint*8, 0]
                depth = 0
                current_level = midpoint
                the_list = []
                while curr:
                    print(curr[0].value, 'has children: ', curr[0].left and curr[0].left.value, curr[0].right and curr[0].right.value)
                    if otherTree[curr[2]].isspace():
                        curr[2] += curr[3]
                        curr[1] += 1
                    print(curr[2])
                    print('mid', midpoint)
                    if curr[2] == midpoint*8 and curr[3] < 0:
                        curr[2] += 1
                    elif curr[2] == midpoint*8 and curr[3] > 0:
                        curr[2] -= 1
                    if curr[0] == self.root:
                        otherTree[curr[2]] += '  ' * curr[1] + str(curr[0].value)
                    else:
                        otherTree[curr[2]] += '  ' * curr[1] + str(curr[0].parent.value) + '<' + str(curr[0].value)
                    if curr[0].left:
                        otherTree[curr[2] - 1] += ' ' * (len(otherTree[curr[2]]) - len(otherTree[curr[2]-1])) + '/' + (str(curr[0].left and curr[0].left.value))
                    if curr[0].right:
                        otherTree[curr[2] + 1] += ' ' * (len(otherTree[curr[2]]) - len(otherTree[curr[2]+1])) + '\\' + (str(curr[0].right and curr[0].right.value))
                    # if curr[3] == '/':
                    #     otherTree[curr[2] + 1] += ' ' * curr[1] + curr[3]
                    # else:
                    #     otherTree[curr[2] - 1] += ' ' * curr[1] + curr[3]

                    curr[0].left and the_list.append([curr[0].left, curr[1] + 1, curr[2] -2, -3])
                    curr[0].right and the_list.append([curr[0].right, curr[1] + 1, curr[2] + 2, 3])
                    try:
                        curr = the_list.pop(0)
                    except IndexError:
                        for i in otherTree:
                            print(i)
                        break
                break