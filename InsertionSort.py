'''
Name: Arya Trivedi
Date: 06/07/2024
Progam: Insertion Sort and detailed explanantion on runtime

Unlike bubble sort, it builds the sorted list one element at a time by comparing each item with the rest of the list and inserting
it into its correct position. This "insertion" procedure gives the algorithm its name.

An excellent analogy to explain insertion sort is the way you would sort a deck of cards. Imagine that you're holding a group of cards in your
hands, and you want to arrange them in order. You'd start by comparing a single card step by step with the rest of the cards until you find its correct position
. At that point, you'd insert the card in the correct location and start over with a new card, repeating until all the cards in your hand were sorted.

Similar to bubble sort implementation, the insertion sort algorithm has a couple of nested loops that go over the list.
The inner loop is pretty efficient because it only goes through the list until it finds the correct position of an element. That said,
the algorithm still has an O(n^2) runtime complexity on the average case.

The worst case happens when the supplied array is sorted in reverse order. In this case, the inner loop has to execute every comparison
to put every element in its correct position. This still gives you an O(n^2) runtime complexity. The best case happens when the supplied
array is already sorted. Here, the inner loop is never executed, resulting in an O(n) runtime complexity, just like the best case of bubble sort

Although bubble sort and insertion sort have the same Big O runtime complexity, in practice, insertion sort is considerably more efficient than bubble sort. If you look at the implementation of both algorithms,
then you can see how insertion sort has to make fewer comparisons to sort the list.

There are more powerful algorithms, including merge sort and Quicksort, but these implementations are recursive and usually fail to beat
insertion sort when working on small lists. That said, insertion sort, is not practical for large arrays, opening the door to algorithms that can scale in more efficient ways.

Remember: O(1) constant > O(log n) logarithmic > O(n) linear > O(n^2) quadratic > O(2^n) exponential > O(n!) factorial

Any algorithm which runs in less than or equal to O(n) is better, for smaller datasets, O(n!) might work best. So algo selection is on case to case basis.
'''

# main insertion sort function

def insertion_sort(array):
    cycles = 0 # to count number of cycles to complete sorting

    # Loop from the second element of the array until
    # the last element
    for i in range(1,len(array)): # note starting from 1 NOT 0
        element = array[i] # get the value of item at index
        prevIndex = i - 1 # set the previous Index

        #Run through the list of tiems (the left portion of the array)
        # And find the correct position
        # of the element referenced by element. Do this only
        # if element is smaller than its adjacent values.
        print("Cycle is", cycles, "the list is", array, "previous index is", prevIndex, "previous value is", array[prevIndex], "the current value is", element)
        cycles += 1 # before and if enter while loop
        while prevIndex >= 0 and array[prevIndex] > element:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[prevIndex + 1] = array[prevIndex]
            prevIndex -= 1
            cycles += 1 # we are in while loop, increment again
            print("Cycle is ", cycles, "the list is", array, "previous index is", prevIndex, "previous value is", array[prevIndex], "the current value is ", element)

        # When you finish shifting the elements, you can position
        # element in its correct location
        array[prevIndex+1] = element

    return array, cycles # return modified array and cycles

nums = [3,10,22,4,1,5,11]
print("Bdfore insertion sort list was", nums)
nums, cycles = insertion_sort(nums)
print("After insertion Sort list is", nums)
print("It took", cycles, "cycles to complete the sort for a list of size",len(nums))


