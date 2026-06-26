# 容量と価格のデータ
weights = [4, 8, 3, 5, 9, 2, 3, 1, 5, 2, 4, 2, 7, 10, 3, 13]
values = [6,12, 4, 3, 7, 1, 3, 2, 7, 3, 4, 2,10, 13, 5, 16]
N = len(weights)
CAPACITY = 45
max_value = 0
best_set = []
# 総当り

for mask in range(1 << N):
    total_w = 0
    total_v = 0
    selected = []
for i in range(N):
    if mask & (1 << i):
       total_w += weights[i]
       total_v += values[i]
       selected.append(i + 1)
    if total_w <= CAPACITY and total_v > max_value:
       max_value = total_v
       best_set = selected
print("最大価格:", max_value)
print("選ばれた品物:", best_set)