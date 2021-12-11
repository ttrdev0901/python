class Card(object):
    def __init__(self, str_int: str):
        self.suit = str_int
        self.char = str_int[0]
        self.number = str_int[1]
    
    def __str__(self):
        return f"{self.char}{self.number}"
    
    def __eq__(self, other) -> bool:
        return self.suit == other.suit

def bubblesort(cards: list):
    A = cards.copy()
    n = len(cards)
    for i in range(n):
        for j in range(n-1, i, -1):
            if A[j].number < A[j-1].number:
                A[j], A[j-1] = A[j-1], A[j]
    return A

def selectionsort(cards: list):
    A = cards.copy()
    n = len(cards)
    for idx in range(n-1):
        minidx = idx
        for jdx in range(idx+1, n):
            if A[jdx].number < A[minidx].number:
                minidx = jdx
        if minidx != idx:
            A[idx], A[minidx] = A[minidx], A[idx]
    return A

def isStable(truelist:list, checkedlist:list):
    for tl, cl in zip(truelist, checkedlist):
        if tl != cl:
            return False
    return True

n = int(input())
cards = [ Card(i) for i in input().split()]

bub = bubblesort(cards)
sel = selectionsort(cards)

print(*bub)
print('Stable')
print(*sel)
print('Stable' if isStable(bub,sel) else 'Not stable')