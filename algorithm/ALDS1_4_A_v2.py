n = int(input())
s = set(map(int, input().split()))
q = int(input())
t = set(map(int, input().split()))

print(len(s&t))