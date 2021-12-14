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
    
    def last(self):
        return self.items[-1]

stack1 = []
stack2 = []

string = input()

# _はifで拾わない。自動的にidxに1足されるので。
amount = 0
for idx, ch in enumerate(string):
    if ch == "\\":
        stack1.append(idx) # stackに格納
    elif ch == "/" and len(stack1) != 0:
        j = stack1.pop() # stackから取り出し
        d = idx - j
        amount += d
        while len(stack2) != 0 and stack2[-1][0] > j:
            d += stack2.pop()[1]
        stack2.append((j, d))

print(amount)
print(len(stack2), *[i[1] for i in stack2])


