numbers = list(range(1, 11))
def grinder(number):
    box = []
    for item in number:
        if item % 2 == 0:
            box.append(item)
    return box
print(grinder(numbers))




