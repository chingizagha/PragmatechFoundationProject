# Task 1 ====================

# def myfunc(list1):
    
#     sum1 = 0

#     for i in list1:
#         sum1 += i
#     print(sum1)
    
# myfunc([8, 2, 13, 0, 7])


# Task 2 ====================

# def multiply(list1):
    
#     sum1 = 1

#     for i in list1:
#         sum1 *= i
#     print(sum1)
    
# multiply ([8, 2, 3, -1, 7])

# Task 3 ====================


# def returnDay(weekDay):

    
#     if weekDay == 1:
#         print('Sunday')
#     elif weekDay == 2:
#         print('Monday')
#     elif weekDay == 3:
#         print('Tuesday')
#     elif weekDay == 4:
#         print('Wednesday')
#     elif weekDay == 5:
#         print('Thursday')
#     elif weekDay == 6:
#         print('Friday')
#     elif weekDay == 7:
#         print('Saturday')
#     else:
#         print('None')



# num_week = int(input('Enter a number: '))

# returnDay(num_week)

# Task 4 ====================

# def lastElement(list1):
    
#     if not list1:
#         print('None')
#     else:
#         print(list1[-1]) 


# lastElement([1, 2, 3, 4, 5])

# Task 5 ====================


# def evenNumbers(list1):
    
#     for i in list1:
#         if i % 2 != 0:
#             list1.remove(i)
    
#     print(list1)
        


# evenNumbers([1, 2, 3, 4, 5, 6, 7, 8, 10])

# Task 6 ==================== 

# def showEmployee(**kwargs):

#     print("Name: " + kwargs.values())


# name = input('Enter name: ')

#salary = int(input("Enter salary: "))

#showEmployee(name1 = name)

# Task 7 ==================== ????


# def multiplyNumber(list1):

    
    
#     while 1 > 0:
#         num1 = int(input('Enter a number: '))

#         if num1 % 1 == 0:
#             list2.append(num1)
#         elif num1 == 'no':
#             print(list1)
#         else:
#             print('Invalid number')
    
    
#     sum1 = 0

#     for i in list1:
#        sum1 += i
#     print(sum1)

# list2 = []
# multiplyNumber(list2)
        


# Task 7 ====================

# def my_func(*numbers):
#     cem = 0
#     for i in numbers:
#         cem += i 
#     return cem


# print(my_func(1, 2, 3, 4, 5, 6, 7, 8))


def my_func(func):

    def decorate():
        print('Decorate is running')
        func()
        print('Decorator stopped')
    
    return decorate()
def main():
    print('Main is running')

my_func(main)