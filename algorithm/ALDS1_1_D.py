
# 問題文から1≤Rt≤10^9
maxp = -10**(9)

n = int(input())

# 入力受付
rt = [int(input()) for _ in range(n)] 
minv = rt[0]

for r in rt[1:]:
    maxp = max(maxp, r - minv) # 最大利益
    minv = min(minv, r) # 最小の値

print(maxp)
