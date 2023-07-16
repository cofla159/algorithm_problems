function solution(n) {
    const memo = [0];
    for (let i = 1; i <= n; i++){
        if (i === 1 || i === 2) {
            memo[i] = 1;
        }else{
            memo[i] = (memo[i-1] + memo[i-2]) % 1234567;
        }
    }
    return memo[n];
}