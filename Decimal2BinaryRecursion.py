'''
Name: Arya Trivedi
Date: 06/03/2024
Program: Decimal 2 Binary using Recursion

'''

# Function implements number to binary.
# It uses recursion, method calling self function

# The big-0 runtime for a recursive function is
# equivalent to the number to recursive function calls.
# This value varies depending on the complexity of the
# algorithm of the recursive function.
# For example,a recursive function of input N that
# is called N times will have a runtime of O(N)

def Dec2Bin(num):
    if num >= 1:
        # Floor division and call method again till num>= 1
        Dec2Bin(num // 2)
    # Modulus, add remainder and spacer, recursively
    print(num % 2, end = '')

# making sure input is an integer
try:
    num = int(input('Enter an integer to convert to binary: '))
    Dec2Bin(num) # call the recursive method
except:
    print("Integer expected, Please try again")