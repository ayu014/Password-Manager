# #Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']




# def generate():
#     nr_letters = random.randint(8, 10)
#     nr_symbols = random.randint(2, 4)
#     nr_numbers = random.randint(2, 4)

#     password_list = []

#     for char in range(nr_letters):
#         password_list.append(random.choice(letters))

#     for char in range(nr_symbols):
#         password_list += random.choice(symbols)

#     for char in range(nr_numbers):
#         password_list += random.choice(numbers)

#     random.shuffle(password_list)

#     password = ""
#     for char in password_list:
#         password += char

#     return password


import string
from random import randint,choice,shuffle

letters = string.ascii_letters
symbols = string.punctuation
digits = string.digits

def generate():

    pass_l = [choice(letters)  for i in range(randint(8,10))]
    pass_s = [choice(symbols) for i in range(randint(2,4))]
    pass_d = [choice(digits) for i in range(randint(2,4))]

    password = pass_l + pass_s + pass_d
    #Shuffling of all the characters to make it more complex
    shuffle(password)

    password = ''.join(password)
    return password