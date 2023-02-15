N = int(input())
S = ''
for i in range(N):
    S+=input()

L = 0
R = N-1
result = ''
while L<=R:
    if len(result) == 80:
        print(result)
        result = ''

    if L == R:
        result += S[L]
        break
    if S[L] == S[R]:
        for j in range(1,2001):
            if L+j >= R-j:
                result += S[L]
                L += 1
                break
            elif S[L+j] > S[R-j]:
                result += S[R]
                R -= 1
                break
            elif S[L+j] < S[R-j]:
                result+= S[L]
                L += 1
                break
    elif S[L] > S[R]:
        result += S[R]
        R -= 1
    else:
        result+=S[L]
        L += 1
print(result)
