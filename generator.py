# password generator 

import random
import string

string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def main():
    #enter the lenght of the password
    input1 = int(input("How many characters should your password have: "))
    if input1 < 8:
        input1 = int(input("The number needs to be higher then 7. How many characters should your password have: "))
    elif input1 > 50:
        input1 = int(input("The number needs to be higher then 7. How many characters should your password have: "))

    #enter the amount of symbols of the password
    charsInPw = int(input("How many symbols should your password contain: "))
    if charsInPw > input1:
        charsInPw = int(input("The symbols can not be more then the lenght of your password. How many symbols should your password contain: "))

    symbol_list = []
    for i in range(0, charsInPw):
        symbol = input("Enter a symbol: ")
        symbol_list.append(symbol)
    
    #list for random numbers and letters
    list1 = []
    #loop to fill the list with random numbers from 0 to 9 and letters from a to z and A to Z
    for i in range(input1 - charsInPw):
        if input1 - charsInPw == 0: 
            n = random.randint(0,9) 
            list1.append(str(n))
        else:
            l = random.choice(string.ascii_letters)
            list1.append(str(l))


    #combine and shuffle 
    password_list = list1 + symbol_list 
    random.shuffle(password_list)
    password = ''.join(password_list)

    print("Your new password is: ", password)


main() 