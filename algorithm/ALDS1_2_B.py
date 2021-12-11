n = int(input())
A = list(map(int, input().split()))

cnt = 0
for idx in range(n-1):
    minidx = idx
    for jdx in range(idx+1, n):
        if A[jdx] < A[minidx]:
            minidx = jdx
    if minidx != idx:
        A[idx], A[minidx] = A[minidx], A[idx]
        cnt += 1

print(*A)
print(cnt)