n, a, b = map(int, input().split())
x1 = [0 for i in range(n)]
y1 = [0 for i in range(n)]
x2 = [0 for i in range(n)]
y2 = [0 for i in range(n)]
for i in range(n):
    x1[i], y1[i], x2[i], y2[i] = map(int, input().split())
sum = 0
for i in range(n):
    width = min(a,x2[i]) - max(0,x1[i])
    height = min(b,y2[i]) - max(0,y1[i])
    if width > 0 and height > 0:
        sum += width * height
print(sum)
