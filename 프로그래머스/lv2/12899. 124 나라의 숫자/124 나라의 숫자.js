function solution(n) {
    let level = 0;
    let N = 0;
    let X = 0;
    for (let i=0; i<30; i++) {
        if (n<=X) {
            level = i
            N = (3**i) - (X-n)
            break
        }
        X = X+3**(i+1)
    }
    
    let A = 3**level;
    
    var answer = '';
    for (let i=0; i<level; i++) {
        const a = A/3;
        if (N > a*2) {
            answer += '4'
            N -= a*2
        } else if (N > a) {
            answer += '2'
            N -= a
        } else {
            answer += '1'
        }
        A /= 3
    }
    return answer;
}