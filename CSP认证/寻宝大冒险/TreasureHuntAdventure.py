n, L, S = map(int, input().split())
N = [list(map(int,input().split())) for _ in range(n)]
B = [[int(x) for x in input().split()] for _ in range(S+1)]
M = []
for i in range(S+1):
    for j in range(S+1):
        if B[i][j] == 1:
            M.append([i,S-j])
sum = 0
def same(i,j):
    for l in range(S + 1):
        for m in range(S + 1):
            if B[S - l][m] == 1 and N.count([i + l, j + m]) != 1:
                return 0
            elif B[S - l][m] == 0 and N.count([i +  l, j + m]) == 1:
                return 0
    return 1
for i in range(L+1-S):
    for j in range(L+1-S):
        sum += same(i,j)
print(sum)