n ,m = map(int,input().split())
T = [0,0]
for _ in range(n):T=[a+b for a,b in zip(T,list(map(int,input().split())))]

M = []
for _ in range(m):M.append(list(map(int,input().split())))
for i in range(m):
    print(M[i][0]+T[0],M[i][1]+T[1])
