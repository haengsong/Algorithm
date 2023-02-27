function solution(numbers, target) {
    let answer = 0;
    const L = numbers.length;
    
    function bt(X,level) {
        if (level === L) {
            if (X === target) {
                answer += 1
            }
            return
        }
        bt(X+numbers[level],level+1)
        bt(X-numbers[level],level+1)
    }
    bt(0,0)
    
    return answer;
}