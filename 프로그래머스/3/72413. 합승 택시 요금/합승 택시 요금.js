function solution(n, s, a, b, fares) {
    const inf = 10 ** 9;
    const cost = Array(n+1).fill().map(el => Array(n+1).fill(inf));
    
    for (const [node1, node2, price] of fares){
        cost[node1][node2] = cost[node2][node1] = price
    }
    
    for (let k = 1; k <= n; k++){
        cost[k][k] = 0;
        for (let i = 1; i <= n; i++){
            for (let j = 1; j <= n; j++){
                cost[i][j] = Math.min(cost[i][j], cost[i][k]+cost[k][j])
            }
        }
    }
    let answer = inf;    
    for (let i = 0; i <= n; i++){
        answer = Math.min(answer, cost[s][i]+cost[i][a]+cost[i][b]);
    }
    return answer;
}