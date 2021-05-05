# Task 1 ==================== Done

# i = 0
# result = 0
# list1 = [1, 2, 3, 4, 5, 83]

# while i < len(list1):   
#     result = result + list1[i]
#     i += 1 
    
# print(result)

# Task 2 ====================

  # With Sort()

# list1 = [1, 11, 3, 4, 8, 6]

# list1.sort()

# print(list1[-1])

 # Without Sort()

# max_num = 0
# list1 = [1, 11, 3, 4, 8, 13]

# for i in list1:
#     if i > max_num:
#         max_num = i
# print(max_num)     

# Task 3 ====================


# list1 = [1, 11, 3, 4, 8, 13]

# min_num = list1[0]

# for i in list1:
#     if i < min_num:
#         min_num = i

# print(min_num) 

# Task 4 ==================== ??????

# list1 = ['abc', 'xyz', 'aba', '1221']
# i = 0
# while i < len(list1):
#     if len(i) >= 2 and i[0] == i[-1]:
#         i += 1
#         print(i)      

    

# Task 5 ==================== Done

# list1 = ['1', 5, 6]

# if not list1:
#     print('List is Empty')    
# else:
#     print('List is not Empty')


# Task 6 ====================


# store_food = ("apple", "banana", "lemon", "kiwi", "grape")  

# for i in store_food:
#     print('Menu: ' + i)

# #store_food[1] = "cherry " 

# print(store_food) # Python rejects the change.

# store_food = list(store_food)
# store_food[1] = "watermelon"
# store_food[3] = "cherry"
# store_food = tuple(store_food)


# for a in store_food:
#     print('Revised Menu: ' + a)


# Task 7 ====================

# user_name = input('Enter Username: ')

# usernames = ['admin', 'Emil', 'Murad', 'Ali', 'Chingiz', 'Rustem', 'Niyaz']


# if user_name in usernames:
#     if user_name == 'admin':
#         print("Hello admin, would you like to see a status report?")
#     else:
#         print(f"Hello  {user_name}, thank you for logging in again!") 

# else:
#     print('Invalid Username')


# Task 8 ====================

# aris = {"name": "Plato","country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}



# word = input('Enter Word: ')

# if word == "name" or word == "title":
#     question1 = input("Maybe did you mean 'What was the name of this philosopher'?: ")
#     if question1 == 'yes' or question1 == 'Yes':
#         print(f'{word.title()} of this philosopher was {aris["name"]}')
#     elif question1 == 'no' or question1 == 'No':
#         word = input('Enter Word: ')
#         if word == "name" or word == "title":
#             print("You entered this before!")
#             word = input('Enter Word: ')
# elif word == "country" or word == "where":
#     question2 = input("Maybe did you mean 'Where was Plato born?': ")
#     if question2 == 'yes' or question2 == 'Yes':
#         print(f'{aris["name"].title()} was born in {aris["country"].title()}')
#     elif question2 == 'no' or question2 == 'No':
#          word = input('Enter Word: ')
#          if word == "where" or word == "country":
#             print("You entered this before!")
#             word = input('Enter Word: ')
# elif word == "born" or word == 'when':
#     question3 = input("Maybe did you mean 'When was Plato born?': ")
#     if question3 == 'yes' or question3 == 'Yes':
#         print(f'{aris["name"].title()} was born in {aris["born"]}')
#     elif question3 == 'no' or question1 == 'No':
#         word = input('Enter Word: ')
#         if word == "name" or word == "title":
#             print("You entered this before!")
#             word = input('Enter Word: ')
# elif word == "teacher" or word == "master":
#     question4 = input("Maybe did you mean 'Who was a teacher of Plato?': ")
#     if question4 == 'yes' or question4 == 'Yes':
#         print(f'{word.title()} of {aris["name"].title()} was {aris["teacher"]}')
#     elif question4 == 'no' or question4 == 'No':  
#         word = input('Enter Word: ')
#         if word == "name" or word == "title":
#             print("You entered this before!")
#             word = input('Enter Word: ')
# elif word == "student" or word == "learner":
#     question5 = input("Maybe did you mean 'Who was a student of Plato?': ")
#     if question5 == 'yes' or question5 == 'Yes':
#         print(f'{word.title()} of {aris["name"].title()} was {aris["student"].title()}')
#     elif question5 == 'no' or question5 == 'No':  
#         if word == "student" or word == "learner":
#             print("You entered this before!")
# else:
#     print("Not found!")




    





    
