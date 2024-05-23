'''
Name: Arya Trivedi
Date: 5/23/24
Program: Palindrome in Python

#this function takes a word or sentence and checks if 
# the input value is palindrome i.e. if read reverse, it's the same
# the program will ignore any special characters, only a-z
'''
def isPalindrome(word):
    dummy = [] # create a dummy list to append
    word = word.lower() # lower the input
    for i in range(len(word)): # iterate from 0 to len(word) - 1
        if(word[i] >= 'a' and word[i] <= 'z'): # check if char is within a-z
            dummy.append(word[i]) # if valid, append, else ignore

    end =  len(dummy)-1 # length of the dummy array, -1 to take care of index starts with 0
    start = 0 # starting point
    while start < end: # so long start is less than end
        if(dummy[start] != dummy[end]): # if char don't match, exit and return false
            return False # not a palindrome
        start += 1 # chars match increment start counter
        end -= 1 # chars match decrement end counter
    return True; # default return True

# take user input
user_input = input("What is the word or sentence in your mind? ")

# check if the input is Palindrome and output a message
if isPalindrome(user_input):
    print(user_input, "is a Palindrome")
else:
    print(user_input, "is NOT a Palindrome")