N = int(input())
M = int(input())
ARR = input()


P = ''
for i in range(N+1):
    P+='I'
    if i != N:
        P+='O'
L = len(P)
pre = ''
n = 0
result = 0
for i in range(M-L+1):
    if ARR[i] == 'I' and ARR[i+1] == 'O':
        pre = ''
        for j in range(i,i+L):
            pre += ARR[j]
        if pre == P:
            result += 1


print(result)