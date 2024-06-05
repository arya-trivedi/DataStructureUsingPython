'''
Name: Arya Trivedi
Date: 06/05/2024
Program: BubbleSort

Let's say our list is num = [3,10,22,4,1,5,11]
In the first iteration, number 3 will not swap till number 1 is reached
which is after 4 loops. num = [1,10,22,4,3,5,11]

Next 10 will not swap till it sees 4, which is 2 loops
num = [1,4,22,10,3,5,11]

Next 22 will swap with 10, which is 1 loop
num = [1,4,10,22,3,5,11]

Next is again 22 will swap with 3, which is 1 loop
num = [1,4,10,3,22,5,11]

Next is again 22 will swap with 5, which is 1 loop
num = [1,4,10,3,5,22,11]

Next is again 22 will swap with 11, which is 1 loop
num = [1,4,10,3,5,11,22]

And so on and so forth.... it will take total 13 iterations to sort

O(n*n(n-1)) => because we ignore constant numbers such as 1 complexity is O(n^2), so this is not a good algorithm

'''

def BubbleSort(num):
    countLoops = 0
    for i in range(len(num)): #loop of n
        for j in range(len(num) -1): # loop of n(n-1)
            if num[i] < num[j]: # num at i less than num at j, swap
                temp = num[i] #step 1 of swap
                num[i] = num[j] # step 2 of swap
                num[j] = temp # step 3 of swap
                countLoops+=1

    print("The bubble sort worked in", countLoops, "iterations when the size of the list was", len(num))
    return num

num = [3,10,22,4,1,5,11]
print("Before Bubble Sort", num)
num = BubbleSort(num)
print("After Bubble Sort", num)