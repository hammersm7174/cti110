# CTI-110
# M6HW2 - Random Number
# Mark Hammers
# 09 Nov 2017
#

import random

def generate_random_num():
   random_num = random.randInt(1, 100)
   return random_num

def ask_user_num(message = 'Can you guess the random number?'):
    user_num = int(input(message))
    return user_num

def check_num_right(user_num, random_num):
    if user_num > random_num:
        return 'Too high.'
    elif user_num < random_num:
        return 'Too low.'
    else:
        return 'Congrats! You got it right!'

def main():
    user_congrats = False
    ready_go = True
    
    while user_congrats or ready_go:
       random_num = generate_random_num()
       user_num = ask_user_num()
       message = check_num_right(user_num, random_num)

    while message != 'Congrats! You got it right!':
        print(message)
        user_num = ask_user_num('Try again: ')
        message = check_num_right(user_num, random_num)

    print(message)
    user_congrats = True

main()
