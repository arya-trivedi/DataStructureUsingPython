'''
Name: Arya Trivedi
Date: 06/03/2024
Program: Decimal 2 Binary using iteration

# Funciton implements number to binary.
# it uses iteration technique, using 0(n) approach
# as there is ONLY 1 while loop
'''

def Dec2Bin(num):
    binary = ''
    while num > 0:
        # build string by adding remainder to spacer
        binary = str(num % 2) + binary
        num = num // 2 #get the floor value
    print(binary) # finally, print

# making sure input is an integer
try:
    num = int(input('Enter an integer to convert to Binary: '))
    Dec2Bin(num) # call the recursive method
except:
    print("Integer expected, try again")