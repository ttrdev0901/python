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

stack1 = Stack()
stack2 = Stack()

string = input()

for idx, ch in enumerate(string):
    if ch == "\\":
        stack1.push(idx)
    elif ch == "/":
        nidx = stack1.pop()
        d = nidx - idx
        
