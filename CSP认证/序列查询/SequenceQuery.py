n, N = map(int, input().split())
A = list(map(int, input().split()))

sum = 0
for i in range(1,n+1):
    if i < n:
        sum += (A[i] - A[i-1])*i
    else:
        sum += (N - A[i-1])*i
print(sum)