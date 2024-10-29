n, m = map(int, input().split())
p = list(map(int, input().split()))
t = list(map(int, input().split()))
min_t = [0 for i in range(m)] # 记录每个课程的结束时间
day1 = [0 for i in range(m)] # 记录每个课程的开始时间
for i in range(m):
    if p[i] != 0:
        day1[i] = t[p[i]-1]+day1[p[i]-1]
        min_t[i] = day1[i]+t[i]-1
    else:
        min_t[i] = t[i]
        day1[i] = 1
    print(day1[i],end=' ')
print()
min_day = max(min_t)
if min_day <= n:
    for i in range(m):
        print(day1[i]+n-min_day,end=' ')
    print()