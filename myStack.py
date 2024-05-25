'''
Name: Arya Trivedi
Date: 4/30/2024
Program: My implementation of ADT, stack using container approach
'''

'''
A stack is a container (linear collection) in which dynamic set operations are carried out as per the last-in first-out (LIFO) principle
. There is only one pinter - top, which is used to perform these operations
'''

class myStack:
    #constructor
    def __init__(self):
        self.container = []

    # appending to the *container*,
    def push(self, item):
        self.container.append(item)
    
    # pop from the container
    def pop(self):
        return self.container.pop()
    
    # view element at the top of the stack
    def peek(self):
        if self.isEmpty():
            raise Exception('Stack Empty!')
        return self.container[-1]
    # see if empty
    def isEmpty(self):
        return self.size() == 0
    # return length of container
    def size(self):
        return len(self.container) #length of container
    
    # show container
    def show(self):
        return self.container #display the entire stack as list
    
    # clear or reset
    def clear(self):
        self.container = []

def main():

        stack = myStack()
        stack.push(1)
        stack.push(10)
        stack.push(21)
        stack.push(31)
        stack.push(41)
        print("Size of my stack is: ", stack.size())
        print("is Empty?", stack.isEmpty())
        print("Display All: ", stack.show())
        stack.pop()
        print("Display All after pop: ", stack.show())
        stack.clear()
        print("Display All after pop-all:", stack.show())
    
if __name__ == '__main__':
    main()