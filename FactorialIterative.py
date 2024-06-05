'''
Name: Arya Yohan Trivedi
Date: 06/05/2024
Program: Factorial Using Iteration
Let's assume input was 5
we are doing num*count, in beginning of while loop num = 5 and count = 1
First Iteration: 5(num) * 1(count) => 5 and count = 5
Second Iteration: 4(num) * 5(count) => 20 and count = 20
Third Iteration: 3(num) * 20(count) => 60 and count = 60
Fourth Iteration: 2(num) * 60(count) => 120 and count = 120
Since num > 1 is completed, program returns 120
It will run in num - 1 loops
Since constant numbers are not taken in O(num - 1), thus we
will conclude this algorithm will run in O(n)

O(1) > O(log n) > 0(n) > O(n log n) > O(n^2) > O(2^n) > O(n!)
'''
# O(n) - time complexity
def FactIter(num):
    count = 1 # for 0 or 1, fact is 1 (0! or 1! = > 1)
    while num > 1: # loop to num
        count *= num # multiply count with num
        num -=1 # reduce num by 1
        print("in the loop")
    return count # at the end, return count

num = int(input('Enter an integer to find factorial: '))
print(FactIter(num))