def my_func (list_1: list, list_2: list) -> list:
    return [item ** 3 for item in set(list_1 + list_2)]
var = my_func([1, 3, 5, 6], [2, 4, 6])


print(var)