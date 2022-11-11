from functools import reduce

def sum_of_squares(sequence):
    # Your code here
    # x = 0
    # for i in sequence:
    #     x += i ** 2
    # return x
    intergers = [int(x) for x in sequence if x[0] != '#']
    squares = [x **2 for x in intergers]
    return reduce(lambda a, b: a + b, squares)

# print(sum_of_squares([0]))
# print(sum_of_squares([1]))
# print(sum_of_squares([1, 2, 3]))
# print(sum_of_squares([-1]))
# print(sum_of_squares([-1, -2, -3]))

print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))
print(sum_of_squares(['1', '2', '#100', '3']))


