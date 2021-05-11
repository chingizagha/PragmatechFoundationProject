# Task 1 ====================

# name = input('Enter Name: ')
# age = int(input('Enter Age: '))

# year = f'Hey {name.title()} in {2021 + (100-age)} you will be 100 year old'

# print(year)


# Task 3 ====================

# number = int(input('Enter Number: '))

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# new_list = [i for i in a if i < number ]
# print(new_list)

# Task 4 ====================

# number = int(input('Enter Number: '))

# list_range = list(range(1, number+1))
# divisor_list = []

# for i in list_range:
#     if i % 2 == 0:
#         divisor_list.append(i)
# print(divisor_list)
        
# Task 5 ====================

# word = input('Enter Word: ')

# drow = word[::-1]

# if drow == word:
#     print('Its is Palindrome')
# else:
#     print(Nonea)
        
# Task 6 ====================


# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# new_list = [i for i in a if i % 2 == 0]
# print(new_list)

# Task 7 ====================
# import random

# random_number = random.randint(1, 10)

# guess = int(input("Enter guess: "))

# while guess != exit or guess != random_number:

#     if guess > random_number:
#         print('Too high')
#     elif guess < random_number:
#         print('Too low')




car = {
    "Car": 'BMW',
    "Color": 'Red',
    "Typle": 'Mini'
}

# print(car.get('price', 'Not Found'))

# print(car.items())

# print(car.values())


# car.update({"Price": '1500'})
# print(car)

car['Color'] = 'Yellow'

print(car)