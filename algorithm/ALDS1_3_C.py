class DoublyLinkedList:
    def __init__(self) -> None:
        self.items = []
    
    def insert(self, x):
        self.items.insert(0, x)
    
    def delete(self,x):
        idx = self.items.index(x)
        self.items.pop(idx)
    


n = int(input())

