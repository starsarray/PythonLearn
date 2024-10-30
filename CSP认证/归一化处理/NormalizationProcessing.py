n = int(input())
a = list(map(int, input().split()))
a_average = sum(a) / n
Da = 0
fa = [0 for i in range(n)]
for i in range(n):
    Da += (a[i] - a_average) ** 2
Da = Da / n
for i in range(n):
    fa[i] = (a[i] - a_average) / (Da ** 0.5)
    print(fa[i],end=' ')