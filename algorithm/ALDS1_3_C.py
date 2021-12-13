class DoublyLinkedList:
    def __init__(self) -> None:
        self.items = []
    
    def insert(self, x):
        self.items.insert(0, x)
    
    def delete(self,x):
        if x in self.items:
            idx = self.items.index(x)
            self.items.pop(idx)
        else:
            pass
    
    def deleteFirst(self):
        self.items.pop(0)
    
    def deleteLast(self):
        self.items.pop(-1)
    
    def __str__(self):
        return " ".join(self.items)

n = int(input())
dll = DoublyLinkedList()

for _ in range(n):
    input_cmd = input()
    
    if input_cmd == "deleteFirst":
        dll.deleteFirst()
    elif input_cmd == "deleteLast":
        dll.deleteLast()
    else:
        cmd, val = input_cmd.split()
        if cmd == "insert":
            dll.insert(val)
        else:
            dll.delete(val)

print(dll)