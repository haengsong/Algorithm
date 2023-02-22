N = int(input())
M = int(input())
ARR = input()


P = ''
for i in range(N+1):
    P+='I'
    if i != N:
        P+='O'
L = len(P)
n = 0
result = 0
while n <= M-L:
    if ARR[n] == 'I':
        pre = ''
        for i in range(n,n+L):
            pre += ARR[i]
        if pre == P:
            result += 1
            n += 1
    n += 1

print(result)