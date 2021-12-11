class Stack(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def pop(self):
        return self.items.pop(0)
    
    def push(self, item):
        return self.items.insert(0, item)


l = input().split()
operand = ('-', '+', '*')

stack = Stack()

for item in l:
    if item in "-":
        b, a = stack.pop(), stack.pop()
        stack.push(a-b)
    elif item in "+":
        b, a = stack.pop(), stack.pop()
        stack.push(a+b)
    elif item in "*":
        b, a = stack.pop(), stack.pop()
        stack.push(a*b)
    else:
        stack.push(eval(item))

print(stack.pop())

