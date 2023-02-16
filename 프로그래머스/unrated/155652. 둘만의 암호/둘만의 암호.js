function solution(s, skip, index) {
    const S = [];
    for (let i=0; i<skip.length; i++) {
        S.push(skip.charCodeAt(i))
    }
    var answer = '';
    
    for (let i=0; i<s.length; i++) {
        let A = s.charCodeAt(i)
        let n = 0;
        while (n<index) {
            A ++;
            if (A>122) {
                A -= 26;
            }
            if (S.includes(A)) {
                continue
            } else {
                n++;
            }
        }
        answer += String.fromCharCode(A)
    }
    
    console.log(answer)
    return answer;
}