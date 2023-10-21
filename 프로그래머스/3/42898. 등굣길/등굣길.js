function solution(m, n, puddles) {
    var answer = 0;
    const dp = Array(n+1).fill(0).map(el => Array(m+1).fill(0));
    const pud = Array(n+1).fill(0).map(el => Array(m+1).fill(0));
    puddles.forEach(el => {
        if (el.length == 0) return;
        pud[el[1]][el[0]] = 1;
    })
    
    for (let i = 1; i < n+1; i++){
        for (let j = 1; j < m+1; j++){
            if (i === 1 && j === 1) {
                dp[i][j] = 1;
                continue;
            }
            if (pud[i][j]) {
                dp[i][j] = 0;
                continue;
            }
            const up = dp[i-1][j];
            const left = dp[i][j-1];
            dp[i][j] = (up+left) % 1000000007;
        }
    }
    return dp[n][m];
}