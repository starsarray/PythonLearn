n = int(input())
T = []
T1 = []
for i in range(n):
    for j in range(8):
        T1.append(input())
    T.append(T1)
    T1 = []
T1 = [T[0]]
T1_count = [0]
for i in range(n):
    for j in range(len(T1_count)):
        if T1[j] == T[i]:
            T1_count[j] += 1
            print(T1_count[j])
            break
        elif j == len(T1)-1:
            T1.append(T[i])
            T1_count.append(1)
            print(1)

