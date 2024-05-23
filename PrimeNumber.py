'''
Name: Arya Trivedi
Date: 5/23/24
Program: Prime Number Finder
'''

'''
The function takes integer as a prime number. A prime number starts with 
2 to infinity. Prime divides by itself ONLY.
2,3,5,7,11,13,17,19,23,29 as examples between 1-30
'''

def isPrime(num):
    for i in range(2,num): # from 2 to end of input number
        if(num % i == 0): # if no remainder, cannot be prime
            return False
    return True # default is True

# Continuous loop to take user input, enter 0 to exit
while True:
    try:
        num = int(input("Input a valid integer 2 or more, 0 to exit: "))
        if(num < 2 and num != 0): # number should be at least 2 or more
            print("Please enter a number 2 or larger")
        elif(num == 0): # this is exit role
            print("Goodbye! ")
            break
        elif(isPrime(num)): # false or true
            print(num, "is a Prime number")
        else:
            print(num, "is NOT a Prime number")
    except ValueError:
        print("Not a valid number, try again")