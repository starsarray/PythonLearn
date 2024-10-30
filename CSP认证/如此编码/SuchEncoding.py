n, m = map(int, input().split())
a = list(map(int, input().split()))
b = [0 for i in range(n+1)]
c = [1]
cb = [0 for i in range(n+1)]
for i in range(1, n+1):
    c.append(a[i-1] * c[i-1])
    if i > 1:
        cb[i] = cb[i-1] + c[i-2]*b[i-1]
    b[i] = (m%c[i] - cb[i-1])//c[i-1]
    print(b[i], end=' ')


