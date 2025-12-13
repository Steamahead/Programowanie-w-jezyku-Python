x = [1, 2, 3, 4, 5]


def grinder(number):
    step_1 = [item * 2 for item in number]
    return step_1


print(grinder(x))
