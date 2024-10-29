n, rate = map(float, input().split())
change = list(map(int, input().split()))
total = change[0]
for i in range(1,int(n)+1):
    total *= (1+rate)
    total += change[i]

print(total*(1+rate)**(-n))