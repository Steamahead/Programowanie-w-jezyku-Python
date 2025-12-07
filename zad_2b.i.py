numbers = [1, 2, 3, 4, 5]
def grinder (number):
    box = []
    for item in number:
        new_item = item * 2
        box.append(new_item)
    return box
print(grinder(numbers))