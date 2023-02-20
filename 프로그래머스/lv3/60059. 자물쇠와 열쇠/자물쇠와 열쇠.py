def solution(key, lock):
    answer = False
    N = len(lock)
    M = len(key)
    
    newlock = []
    for i in range(M-1):
        newlock.append([1]*(N+(M-1)*2))
    for i in range(N):
        newlock.append([1]*(M-1) + lock[i] + [1]*(M-1))
    for i in range(M-1):
        newlock.append([1]*(N+(M-1)*2))
    
    
    for t in range(4):
                
        for y in range((N+M-1)):
            for x in range((N+M-1)):

                visit = [[1]*(N+(M-1)*2) for _ in range((N+(M-1)*2))]
                for y2 in range(N):
                    for x2 in range(N):
                        if lock[y2][x2] == 0:
                            visit[y2+(M-1)][x2+M-1] = 0

                for ky in range(M):
                    for kx in range(M):
                        if newlock[y+ky][x+kx] == 0 and key[ky][kx] == 1:
                            visit[y+ky][x+kx] = 1
                        elif newlock[y+ky][x+kx] == 1 and key[ky][kx] == 1:
                            visit[y+ky][x+kx] = 0
                s = 1
                for y2 in range(N):
                    for x2 in range(N):
                        if visit[y2+(M-1)][x2+M-1] == 0:
                            s = 0
                if s:
                    answer = True
        if t<3:
            newkey = []
            for x in range(M):
                arr = []
                for y in reversed(range(M)):
                    arr.append(key[y][x])
                
                newkey.append(arr)
            
            key = newkey
            
    return answer