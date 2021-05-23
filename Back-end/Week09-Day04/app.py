i = 0


def my_func(list):
    result = 1
    for i in list:
        result *= i
    print(result)

my_func([1, 2, 3, 4, 5])