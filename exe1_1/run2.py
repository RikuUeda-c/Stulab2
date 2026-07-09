import time

weight = [4,8,3,5,9,2,3,1,5,2,4,2,7,10,3,13,11,8]
value  = [6,12,4,3,7,1,3,2,7,3,4,2,10,13,5,16,14,9]

N = len(weight)
CAPACITY = 45

start = time.perf_counter()

dp = [[0]*(CAPACITY+1) for _ in range(N+1)]

for i in range(N):
    for w in range(CAPACITY+1):

        if weight[i] <= w:
            dp[i+1][w] = max(
                dp[i][w],
                dp[i][w-weight[i]] + value[i]
            )
        else:
            dp[i+1][w] = dp[i][w]

end = time.perf_counter()

print("最大価格:", dp[N][CAPACITY])
print("処理時間:", end-start,"秒")