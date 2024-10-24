s = input()
n = int(s.split(" ")[0])
m = int(s.split(" ")[1])
c = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    ss = input()
    for j in range(m):
        c[i][j] = int(ss.split(" ")[j])
d = [0 for i in range(n)]
def superC(i):
    for j in range(n):
        for k in range(m):
            if c[i][k] >= c[j][k]:# 不符合条件，跳出循环
                break
            elif k==m-1:# 符合条件，更新d
                d[i]=j+1
                return
    return

for i in range(n):
    superC(i)
    print(d[i])
