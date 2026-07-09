import time

# 品物の容量と値段
weight = [4,8,3,5,9,2,3,1,5,2,4,2,7,10,3,13,11,8]
value  = [6,12,4,3,7,1,3,2,7,3,4,2,10,13,5,16,14,9]

N = len(weight)
CAPACITY = 45

start = time.perf_counter()

best_value = 0
best_items = []

# 2^18 通り全探索
for bit in range(1 << N):

    total_weight = 0
    total_value = 0
    items = []

    for i in range(N):
        if bit & (1 << i):
            total_weight += weight[i]
            total_value += value[i]
            items.append(i + 1)

    if total_weight <= CAPACITY and total_value > best_value:
        best_value = total_value
        best_items = items

end = time.perf_counter()

print("選んだ品物:", best_items)
print("最大価格:", best_value)
print("処理時間:", end - start, "秒")