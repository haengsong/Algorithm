N,M = map(int,input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int,input().split())))

virusList = []
road = 0
for y in range(N):
    for x in range(M):
        if arr[y][x] == 2:
            virusList.append((x,y))
        elif arr[y][x] == 0:
            road += 1
result = M*N - len(virusList)

def virus():
    global result

    visit = [[0]*M for _ in range(N)]
    
    ST = []
    for i in virusList:
        ST.append(i)
        visit[i[1]][i[0]] = 1

    cnt = 0
    while ST:
        nx,ny = ST.pop(0)

        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            X = nx + dx
            Y = ny + dy
            if 0<=X<M and 0<=Y<N and arr[Y][X] ==0 and visit[Y][X] == 0:
                visit[Y][X] = 1
                cnt += 1
                if cnt > result:
                    return
                ST.append((X,Y))
    result = min(cnt,result)


def check3(level,Y,X):
    if level == 3:
        virus()
        return
    
    for y in range(N):
        for x in range(M):
            if (Y,X) > (y,x): continue
            if arr[y][x] == 0:
                arr[y][x] = 1
                check3(level+1,y,x)
                arr[y][x] = 0

check3(0,0,0)

print(road-3-result)