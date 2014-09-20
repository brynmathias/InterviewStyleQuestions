#!/usr/bin/env python

class stack(object):
    """docstring for stack"""
    def __init__(self):
        super(stack, self).__init__()
        self.array = []
        self.top = -1
        
    def stack_empty(self):
        """docstring for stack_empty"""
        if self.top < 0:
            return True
        else:
            return False
            
    def push(self, value):
        """docstring for push"""
        if(self.top+1 == len(self.array)):
            self.array.append(value)
        else:
            self.array[self.top]=value
        self.top+=1
    
    def pop(self):
        """docstring for pop"""
        if self.stack_empty():
            raise "stack is empty"
        else:
            self.top-=1
            return self.array[self.top+1]
        
        
def main():
    """docstring for main"""
    values = [1,2,4,6,1,35,7,24,6,2,4,6,7,2,23,6,7,2,34443,2123]
    my_stack = stack()
    for v in values:
        my_stack.push(v)
    while(my_stack.stack_empty() is False):
        print my_stack.pop()
    for v in reversed(values):
        my_stack.push(v)    
    while(my_stack.stack_empty() is False):
        print my_stack.pop()
        
if __name__ == '__main__':
    main()