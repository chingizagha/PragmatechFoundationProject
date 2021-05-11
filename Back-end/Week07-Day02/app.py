# Task 1 ===================== 

# dia = int(input('Diameter: '))

# import math

# pi = math.pi

# area_circle = pi * dia**2/4
# print(area_circle)

# Task 2 ======================

# x = """ Sweep through the days Like children that can't stay awake """


# a = int(input('Number: '))



# if len(x) < a:
#     print('Daha Kiçik ədəd daxil edin')

# elif a < 0:
#     print('False')

# else:
#     print(x[:a])

# Task 3 ======================

# ad = input('Ad: ')
# soyad = input('Soyad: ')

# import random

# random_num = (random.randrange(10,100))


# random_gmail = f'{ad.casefold()}{soyad.casefold()}{random_num}@gmail.com'

# print(random_gmail)

# Task 4 ================== ==

# first_num = int(input('First Number: '))

# second_num = int(input('Second Number: '))

# operation = input('Math Operation: ')

# if operation == "+":
#     result = first_num + second_num
#     print(result)

# elif operation == "-":
#     result = first_num - second_num
#     print(result)

# elif operation == "*":
#     result = first_num * second_num
#     print(result)

# elif operation == "/":
#     result = first_num / second_num
#     print(result)

# else:
#     print("Wrong operator entered")


# Task 5 =====================

# n = abs(int(input('Enter Number: ')))

# if n % 2 == 0:
#     print('EVEN')
# else:
#     print('ODD')  


# Task 6 ====================

# n = abs(int(input('Enter Number: ')))

# a = int(input('Enter first divisor: '))

# b = int(input('Enter second divisor: '))

# if n % a == 0 and n % b == 0:
#     print('YES')
# else:
#     print('NO')



#Task 7 =====================

# n = int(input('Enter Number: '))

# if n > 0:
#     print('Positive')
# elif n == 0:
#     print('Zero')
# else:
#     print('Negative') 



#Task 8.1 ===================== ?????

# x = int(input('Enter Number: '))

# y = int(input('Enter Number: '))

# z = int(input('Enter Number: '))

# if x + y > z  or z + x > y or z + x > y:
#     print('YES')
# else:
#     print('NO')



#Task 8.2 =====================

# grade = 0

# while not int(grade) in range(1,13):
#     grade = int(input('Enter grade: '))

#     if 1 <= grade <= 3:
#         print('Initial')
#     elif 4 <= grade <= 6:
#         print('Average') 
#     elif  7 <= grade <= 9:
#         print('Sufficient')
#     elif 10 <= grade <= 12:
#         print('High')

#Task 9 =====================


# number = int(input('Enter Number: '))

# print(number - 1)


#Task 10 =====================

# num_1 = abs(int(input('Enter Number 1: ')))

# num_2 = abs(int(input('Enter Number 2: ')))

# result_1 = num_1 // num_2
# result_2 = num_1 % num_2

# print(f'{result_1}(Tam) {result_2}(Qalıq)')


#Task 11 =====================

# value = int(input('Enter Number: '))

# if value > 0 or value < 0:
#     print(value * -1)
# elif value == 0:
#     print('0')


#Task 12 =====================


# number = int(input('Enter Number: '))



# a  = number // 1000
# a_1 = (number - a*1000) // 100
# a_2 = (number - a*1000 - a_1*100) // 10
# a_3 = number - a*1000 - a_1*100 - a_2*10
# y = a + a_1 + a_2 + a_3
# print(y)
# print(y**2)


#Task 13 =====================

name = input('Name: ')


if len(name) < 3:
    print('Number of characters is less than 3')
elif len(name) > 11:
    print('Number of characters is more than 11')
else:
    surname = input('Surname: ')
    if len(surname) < 5:
        print('Number of characters is less than 5')
    elif len(surname) > 15:
        print('Number of characters is more than 11')
    else:
        year = input('Birth Year: ')
        if len(year) > 4 or len(year) < 4:
            print('Year of birth must consist of 4 characters')
        else:
            email = input('Email: ')
            if len(email) < 10:
                print('Number of characters is less than 10')
            elif len(email) > 22:
                print('Number of characters is more than 22')
            elif '@gmail.com' not in email:
                print('Invalid email')
            elif not email.endswith('@gmail.com'):
                print('Email is not ended with @gmail.com')
            else:
                parol = input('Password: ')
                if len(parol) < 6:
                    print('Number of characters is less than 6')
                elif len(parol) > 13:
                    print('Number of characters is more than 13')
                else:
                    parol2 = input('Confirm Password: ')
                    if parol2 != parol:
                        print('Passwords are not the same')
                    else:
                        print('Registration is complete')
                        question = input('Do you want to see the details of the registration?: ')
                        if question == 'Yes' or question == 'yes':
                            print(f'Name: {name.capitalize()} Surname: {surname.capitalize()} Age: {year} Email: {email} Password: {parol}')
                        elif question == 'No' or question == 'no':
                            print(f'{name.capitalize()}  {surname.capitalize()}  Good luck!')
                        else:
                            print('Wrong answer')






