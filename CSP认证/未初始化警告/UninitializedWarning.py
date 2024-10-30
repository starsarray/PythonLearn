n, k = map(int,input().split())
x = [0 for i in range(k)]
y = [0 for i in range(k)]
sum = 0
for i in range(k):
    x[i],y[i] = map(int,input().split())
    for j in range(i):
        if y[i] == 0:
            break
        elif y[i] == x[j]:
            sum += 1
            break
print(sum)