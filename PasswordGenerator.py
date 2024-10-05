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