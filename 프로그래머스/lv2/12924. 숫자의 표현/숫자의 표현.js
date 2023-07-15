function solution(n) {
    if (n === 1) return 1;
    let answer = 0;
    for (let i = 1; i <= n/2; i++){
        let sum = 0;
        let start = i;
        while (sum < n){
            sum += start++;
        }
        if (sum === n) answer++;
    }
    return answer+1;
}