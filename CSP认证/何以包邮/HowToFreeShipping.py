n, x = map(int, input().split())
a = [int(input()) for i in range(n)]
# a.sort()
sum_a = sum(a)
x_a = sum_a - x # 多的金额
dp = [0 for j in range(x_a+1)] # dp[j]表示前j元钱最多可以买的商品的总价
for i in range(n): # 遍历所有商品
    for j in reversed(range(a[i],x_a+1)): # 从多的金额开始遍历前j元钱的情况 ，以a[i]结束确保j-a[i]>=0
        dp[j]= max(dp[j],dp[j-a[i]]+a[i])
print(sum_a-dp[x_a])