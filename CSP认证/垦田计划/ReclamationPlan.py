n, m, k = map(int,input().split())
T = []
C = []
for i in range(n):
    t, c = map(int,input().split())
    T.append(t)
    C.append(c)
target = min(T)
mm = m
while mm>=0 and target>= k:
    mm = m
    target -= 1
    for i in range(n):
        if T[i]>target:
         mm += (target-T[i])*C[i]
print(target+1)