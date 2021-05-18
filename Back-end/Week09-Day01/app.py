# # Task 1 ========================================

# class Worker:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

    
#     def info_worker(self):
#         return f'Name: {self.name} \nAge: {self.age}'


# worker1 = Worker('Ali', 23)
# worker2 = Worker('Murad', 24)

# print(worker1.info_worker())


# class Customer:

#     def __init__(self, fullname, id_number):
#         self.fullname = fullname
#         self.id_number = id_number

#     def info_custo(self):
#         return f'FullName: {self.fullname} \nID Number: {self.id_number}'

# custo1 = Customer('Said Recebov', 563)
# custo2 = Customer('Rehim Orucov', 796)

# print(custo1.info_custo())

# class Product:

#     def __init__(self, pro_name, price):
#         self.pro_name = pro_name
#         self.price = price
    

#     def pro_info(self):
#         return f'Product Name: {self.pro_name} \nPrice: {self.price}'

# product1 = Product('Milk', 5)
# product2 = Product('Bread', 2)

# #### ====>>> First Class Name Value Changing
# worker1.name = 'Huseyn'

# print(worker1.name)

# #### ====>>> Second Class ID Value Changing
# custo2.id_number = 213

# print(custo2.id_number)

# #### ====>>> Seconad Class Price Value Changing
# product1.price = 6

# print(product1.price)


# # Task 2 ========================================

# class Parent:

#     def __init__(self, age, name, surname, gender):
#         self.age = age
#         self.name = name 
#         self.surname = surname
#         self.gender = gender

# parent1 = Parent(48, 'ALi', 'Muradov', 'Male')

# class Child(Parent):

#     def __init__(self, age, name, surname, gender, height, school):
#         super().__init__(age, name, surname, gender)
#         self.height = height
#         self.school = school

# child1 = Child(18, 'Murad', 'Aliyev', 'Male', '177', 11)



# Task 3 ========================================


# class Animal: 

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         return f'Name: {self.name} \nAge: {self.age}'


# cat = Animal('Erwin', 6)

# print(cat.info())

# class Bird(Animal):

#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color

#     def info(self):
#         return f'Name: {self.name} \nAge: {self.age} \nColor: {self.color}'


# owl = Bird('Larry', 8, 'Brown')

# print(owl.info())

# Task 4 ========================================

class Bicycle:

    def __init__(self, age, color):
        self.age = age
        self.color = color

    def age_info(self):
        return f'Age: {self.age}'

    def update_age(self, change_age):
        self.age = change_age


bicycle1 = Bicycle(18, 'white')

bicycle1.update_age(19)

print(bicycle1.age)