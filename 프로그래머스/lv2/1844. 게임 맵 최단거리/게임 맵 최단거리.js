function solution(maps) {
    const n = maps[0].length;
    const m = maps.length;
    
    const visit = [];
    for (let i=0; i<m; i++) {
        const M = new Array(n).fill(0)
        visit.push(M)
    }
    visit[0][0] = 1
    const ST = [[0,0,1]];
    
    let answer = 0;
    while (ST.length>0) {
        const [x,y,cnt] = ST.shift();
        if (x === n-1 && y === m-1) {
            answer = cnt
        }
        for ([dx,dy] of [[0,1],[1,0],[-1,0],[0,-1]]) {
            const X = dx+x;
            const Y = dy+y;
            if (0<=X && X<n && 0<=Y&& Y<m && maps[Y][X] === 1 && visit[Y][X] === 0) {
                visit[Y][X] = 1
                ST.push([X,Y,cnt+1])
            }
            
        }
    }
    if (answer === 0) {
        answer = -1
    }
    return answer;
}