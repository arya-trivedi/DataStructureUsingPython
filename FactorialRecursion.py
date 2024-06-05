'''
Name: Arya Trivedi
Date: 06/05/2024
Program: Factorial Using Recursion
Let's assume input was 5
First Recursion: 5 * 4 which is 20 and num becomes 4
Second Recursion: 20 * 3 which is 60 and num becomes 3
Third Recursion: 60 * 2 which is 120 and nu becomes 2
Fourth Recursion: 120 * 1 which is 120 and num becomes 1
Fifth Recursion: return 1
Output is 120
((((5*4)*3)*2)*1) => 120 which is n! or 5!

O(1) > O(log n) > O(n) > O(n log n) O(n^2) > O(2^n) > O(n!)
'''
# O(n) - time complexity

def Fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * Fact(num-1)

num = int(input('Enter an integer to find factorial of: '))
print(Fact(num))