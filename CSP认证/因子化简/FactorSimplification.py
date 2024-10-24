from math import sqrt

q = int(input())
c = [[0 for j in range(2)] for i in range(q)]
for i in range(q):
    s = input()
    c[i][0] = int(s.split(" ")[0])
    c[i][1] = int(s.split(" ")[1])
factor = [[] for i in range(q)]
num = [[] for i in range(q)]
for i in range(q): # 遍历q次
    cc = c[i][0]
    clen = int(sqrt(cc))+1
    for j in range(2,clen): # 遍历2到sqrt(cc)
        jlen = int(sqrt(j))+2
        for k in range(2,jlen): # 找素因子
            if j % k == 0 and j!=2: # j不是素数
                break
            elif k == jlen-1: # 找到素数j
                for l in range(clen):
                    if cc % j  == 0: # j是cc的素因子
                        cc = cc / j
                    elif l == 0: # j不是cc的素因子
                        break
                    else :
                        factor[i].append(j)
                        num[i].append(l)
                        break
for i in range(q):
    product = 1
    for j in range(len(factor[i])):
        if num[i][j] >= c[i][1]:
            product = product * factor[i][j] ** num[i][j]
    print(product)





