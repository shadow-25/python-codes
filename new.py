# a="shubham"
# b="thakur"
# c=3
# #print(a%b)
# def list_to_string(lst):
#     result = ''
#     for item in lst:
#         result += str(item) + '\n'
#     return result.strip()  # Remove trailing space

# my_list = ['Python', 'is', 'fun']
# my_string = list_to_string(my_list)
# print(my_string)
# a=input()
# if a=='':
#     print('enter')
# else:
#     print("other key")
# import random

# Generate a unique random number each time in a loop
# for _ in range(5):  # Change 5 to the desired number of unique random numbers
#     unique_number = random.sample(range(1, 101), 1)[0]
#     print(unique_number)

import random

def generate_unique_numbers(count):
    unique_numbers = []
    while len(unique_numbers) < count:
        num = random.randint(0, 9)
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

my_unique_numbers = generate_unique_numbers(9)
print(my_unique_numbers)
def list_of_ques(count):
    Ques_set=[]
    while len(Ques_set)<count:
        num=random.randint(0,9)
        if num not in Ques_set:
            Ques_set.append(num)
    return Ques_set
Ques_Set=list_of_ques(9)
print(Ques_Set)

# Stop=input()
# print(len(Stop))
