n,m=map(int,input().split())
T = []
from math import cos,sin
kp = [1.0]
kb = [1.0]
kidx = 0
knidx = [0] # 记录第i个点的坐标变换前有几个k
rp = [0.0]
rb = [0.0]
ridx = 0
rnidx = [0] # 记录第i个点的坐标变换前有几个r
for i in range(n):
    T.append(list(map(float,input().split())))
    if T[i][0] == 1:
        kp.append(kp[kidx]*T[i][1])
        kidx += 1
    elif T[i][0] == 2:
        rp.append(rp[ridx]+T[i][1])
        ridx += 1
    knidx.append(kidx)
    rnidx.append(ridx)
M = []
for i in range(m):
    M.append(list(map(int,input().split())))
for i in range(m):
    a,b = M[i][0]-1,M[i][1]
    x, y = M[i][2], M[i][3]
    x *= kp[knidx[b]]/kp[knidx[a]]
    y *= kp[knidx[b]]/kp[knidx[a]]
    r = rp[rnidx[b]]-rp[rnidx[a]]
    x, y = x*cos(r)-y*sin(r), x*sin(r)+y*cos(r)
    print(x,y)


