n = int(input())
d = set()
ans = []
for i in range(n):
    order, string = input().split()
    if order == "insert":
        d.add(string)
    elif order == "find":
        if string in d:
            ans.append('yes')
        else:
            ans.append('no')
print('\n'.join(ans))
