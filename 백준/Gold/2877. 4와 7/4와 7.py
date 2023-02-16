def en(level,X):
    global E,N
    if K <= X:
        E = level
        N = (2**level)-(X-K)
        return

    en(level+1, X+2**(level+1))

K = int(input())
E = 0
N = 0
en(0,0)
result = [4]*E
A = 2**E
for i in range(E):
    if A//2 < N:
        result[i] = 7
        N -= A//2
    A /= 2

ans = ''
for i in result:
    ans += str(i)
print(ans)