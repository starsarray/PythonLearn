n, d = map(int,input().split())
def matrix_read(a):
    for i in range(n):
        a.append(list(map(int,input().split())))
Q = []
matrix_read(Q)
K = []
matrix_read(K)
V = []
matrix_read(V)
W = list(map(int,input().split()))
# KT = []
# for i in range(d):
#     K1 = []
#     for j in range(n):
#         K1.append(K[j][i])
# KT*V
KTV = [[0 for i in range(d)]for j in range(d)]
for i in range(d):
    for j in range(d):
        for k in range(n):
            KTV[i][j]+=(K[k][i]*V[k][j])

# WQ
WQ = [[W[i]*Q[i][j]for j in range(d)]for i in range(n)]
# WQKTV
WQKTV = [[0 for j in range(d)]for i in range(n)]
for i in range(n):
    for j in range(d):
        for k in range(d):
            WQKTV[i][j]+=(WQ[i][k]*KTV[k][j])
        print(WQKTV[i][j],end=' ')
    print()
