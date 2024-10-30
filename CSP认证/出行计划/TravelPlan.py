n, m, k = map(int, input().split())
t = [0 for i in range(n)]
c = [0 for i in range(n)]
for i in range(n):
    t[i], c[i] = map(int, input().split())
q = [0 for i in range(m)]
for i in range(m):
    q[i] = int(input())
for i in range(m):
    sum = 0
    for j in range(n):
        if q[i]+k <= t[j] < q[i]+k+c[j]:
            sum += 1
    print(sum)