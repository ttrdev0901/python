n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

def linear_search(A: list, target: int):
    """番兵法による線形探索

    Args:
        A (list): 探索されるリスト
        target (int): 探索したいキー

    Returns:
        int or NOT FOUND: targetの出現回数, 存在しない場合はNOT FOUND
    """
    A.append(target)
    n = len(A) - 1
    i = 0 
    while A[i] != target:
        i += 1
    if i == n:
        return "NOT FOUND"
    return i

cnt = 0
for i in s:
    for j in t:
        if i == j:
            cnt += 1
print(cnt)