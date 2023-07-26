function solution(n, computers) {
    const nodes = [];
    computers.forEach((conn, i) => {
        nodes.push(conn.map((el, j) => j === i ? 0 : el))
    })
    
    let visited = Array(n).fill(0);
    let willVisit = [0];
    let count = 1;
    console.log(nodes);
    
    while (willVisit.length > 0){
        const now = willVisit.pop();
        visited[now] = 1;
        nodes[now].forEach((el,i) => {
            if (el && !visited[i]){
                willVisit.push(i);
            }
        });
        if (willVisit.length === 0 && Math.min(...visited) === 0){
            count++;
            willVisit.push(visited.indexOf(0));
        }
    }
    return count;
}