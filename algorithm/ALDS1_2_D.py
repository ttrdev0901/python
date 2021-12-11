def insertSort(a, gap):
    global cnt
    for i in range(gap, len(a)):
        v = a[i] # 一時保存
        j = i - gap
        while j >= 0 and a[j] > v:
            a[j+gap] = a[j]
            j = j - gap
            cnt += 1
            a[j+gap] = v

def shellsort(a):
    global cnt
    cnt = 0
    gap = []
    h = 1
    while h <= len(a):
        gap.append(h)
        h = 3*h+1
    gap.reverse()
    m = len(gap)
    print(m)
    print(*gap)
    for i in range(m):
        insertSort(a, gap[i])

n = int(input())
a = [int(input()) for _ in range(n)]
shellsort(a)
print(cnt)
for e in a:
    print(e)


        