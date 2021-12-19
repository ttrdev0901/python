def binarySearch(A, key):
    left = 0
    right = len(A)
    while left < right:
        mid = (left+right)//2
        if A[mid] > key:
            right = mid
        elif A[mid] < key:
            left = mid + 1 # midより大きいため
        else:
            return mid
    return None

n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

cnt = 0
for char in t:
    res = binarySearch(s, char)
    if res is not None:
        cnt += 1
print(cnt)