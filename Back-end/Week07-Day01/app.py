# Task 1

x = "Hello World"
y = 6

print(x)
print(y)

# Task 2============================

ad = "murad "
soyad = "aliyev"

tam_ad = "Salam " + ad.capitalize() + soyad.capitalize()

print(tam_ad)

# Task 3 ===========================

num1 = 5 
num2 = 2

print(num1 ** num2)
#25

print(num2 ** num1)
#32

# Task 4 ===========================

y = "4.92"
# y is string

y_int = int(float(y))

print(y_int)
print(type(y_int))

# Task 5 ===========================

temp = int(input('Temperature: '))

if temp < 10:
    print('Cold')

elif temp == 20:
    print('Normal')

elif temp > 30:
    print('Hot')

# Task 6 ==========================

a = "Proqramlaşdırma"

print('x' in a)
#False

# Task 7 ==========================

word1 = 'Hello '
word2 = 'World'

word3 = word1 + word2
print(word3)
