def ff(X):

    visit = [0]*(N+1)
    visit[X] = 1
    Q = [(X,0)]
    C = 0
    while visit != [0]+[1]*N:
        now,cnt = Q.pop(0)
        for k in F[now]:
            if visit[k] == 0:
                C += cnt+1
                visit[k] = 1
                Q.append((k,cnt+1))
    return C

N, M = map(int,input().split())
F = { i:[] for i in range(1,N+1)}
for j in range(M):
    a,b = map(int,input().split())
    F[a].append(b)
    F[b].append(a)

m = 5001*N
result = 0
for l in range(1,N+1):
    a = ff(l)
    if a < m:
        m = a
        result = l

print(result)