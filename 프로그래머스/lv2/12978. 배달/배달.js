function solution(N, road, K) {
    let answer = 0;
    
    const R = {};
    for (let i=1; i<N+1; i++) {
        R[i] = []
    }
    for ([a,b,c] of road) {
        R[a].push([c,b])
        R[b].push([c,a])
    }
    const Q = [[0,1]];
    const ARR = new Array(N+1).fill(500001*N);
    ARR[1] = 0;
    
    while (Q.length > 0) {
        Q.sort();
        [cnt,now] = Q.shift();
        
        for ([C,next] of R[now]){
            if (ARR[next] > cnt + C) {
                ARR[next] = cnt + C
                Q.push([cnt+C,next])
            }
        }
    }
    
    for (let i=1; i<N+1; i++) {
        if (ARR[i] <= K) {
            answer += 1
        }
    }
    

    return answer;
}