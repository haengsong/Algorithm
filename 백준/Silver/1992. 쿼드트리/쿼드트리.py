N = int(input())
ARR =[]
for _ in range(N):
    ARR.append(input())

def ff(x1,x2,y1,y2):
    global result
    if x2-x1 == 1:
        if ARR[y1][x1]=='1':
            result += '1'
        else:
            result += '0'
        return

    cnt = [0,0]
    for i in range(y1,y2):
        for j in range(x1,x2):
            cnt[int(ARR[i][j])] += 1

    if cnt[0] and cnt[1] == 0:
        result += '0'
    elif cnt[0] == 0 and cnt[1]:
        result += '1'

    else:
        R = (x2-x1)//2
        result += '('
        ff(x1, x1+R, y1, y1+R)
        ff(x1+R, x2, y1, y1+R)
        ff(x1, x1+R, y1+R, y2)
        ff(x1+R, x2, y1+R, y2)
        result += ')'

result=''
ff(0,N,0,N)
print(result)