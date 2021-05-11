# Task 1 ========================

# class Restaurant:

#     def __init__(self, restaurant_name, cuisine_type):
#         self.name =  restaurant_name
#         self.cuisine_type = cuisine_type    
    

#     def describe_restaurant(self):
#         print(f'Restaurant Name: {res1.name}, \nCuisine Type: {res1.cuisine_type}')
    
#     def open_restaurant(self):
#         print('Restaurant now open')

# res1 = Restaurant('Norma', 'Greek')

# print(res1.name)
# print(res1.cuisine_type)

# res1.describe_restaurant()

# res1.open_restaurant()

# Task 2 ========================

# class Restaurant:

#     def __init__(self, name, cuisine_type, cost):
#         self.name = name
#         self.cuisine_type = cuisine_type
#         self.cost = cost



#     def describe_restaurant(self):
#         print(f'Restaurant Name: {self.name}, \nCuisine Type: {self.cuisine_type}, \nCost: {self.cost}') 
    





# res1 = Restaurant('Norma', 'Italian', 'Low')
# res1.describe_restaurant()

# res2 = Restaurant('Villa', 'Korean', 'Mid')
# res2.describe_restaurant()

# res3 = Restaurant('Terry', 'German', 'High')
# res3.describe_restaurant()


# Task 3 ========================

class Users:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age



    def describe_user(self):
        print(f'First Name: {self.first_name}, \nLast Name: {self.last_name}, \nEmail: {self.email}, \nAge: {self.age}')

    def greet_user(self):
        print(f'Hi {self.first_name.title()} {self.last_name.title()}')

user1 = Users('Chingiz', 'Agha', 'cingiz@gmail.com', 18)

user1.describe_user()
user1.greet_user()

user2 = Users('Murad', 'Aliyev', 'murad@mail.ru', 21)

user2.describe_user()
user2.greet_user()

user3 = Users('Ali', 'Alyarov', 'ali@gmail.com', 19)

user3.describe_user()
user3.greet_user()

