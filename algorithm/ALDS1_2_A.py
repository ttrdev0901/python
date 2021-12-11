n = int(input())
A = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(n-1, i, -1):
        if A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            cnt += 1
print(*A)
print(cnt)


# # 00:02 sec    5608 KB     236 bytes    
# n = int(input())
# a = list(map(int, input().split()))
# cnt = 0
# for i in range(n):
#   for j in range(1, n-i):
#     if a[n-j] < a[n-j-1]:
#       cnt += 1
#       a[n-j], a[n-j-1] = a[n-j-1], a[n-j]
# print(" ".join([str(i) for i in a]))
# print(cnt)