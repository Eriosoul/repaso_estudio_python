### List ###

my_original_list: list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_range = range(8)
print(list(my_range))

my_list: list = [i + 1 for i in range(8)]
print(my_list)

my_list: list = [i * 2 for i in range(8)]
print(my_list)

my_list: list = [i * i for i in range(8)]
print(my_list)


def sum_fie(number):
    return number + 5


my_list: list = [sum_fie(i) for i in range(8)]
print(my_list)
