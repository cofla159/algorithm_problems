function solution(n, wires) {
    if (n === 2 || n === 3) return n-2;
    
    const nodes = [];
    for (let i = 0; i <= n; i++){
        nodes[i] = [];
    }
    
    wires.forEach(wire => {
        nodes[wire[0]].push(wire[1]);
        nodes[wire[1]].push(wire[0]);
    });
    
    function getConnected(ns){
        let visited = Array(n).fill(0);
        let willVisit = [...ns[1]];
        visited[1] = 1;
        let count = 1;

        while (willVisit.length){
            const next = willVisit.pop();
            if (visited[next]) continue;
            willVisit.push(...ns[next]);
            visited[next] = 1;
            count++;
        }
        return Math.abs(count - (n-count));
    }
    let answer = 98;
    wires.forEach(wire => {
        if (nodes[wire[0]].length === 1 || nodes[wire[1]].length === 1) return;
        const newNodes = nodes.map((endNodes, startNode) => {
            if (startNode === wire[0]){
                return endNodes.filter(node => node !== wire[1])
            }else if(startNode === wire[1]){
                return endNodes.filter(node => node !== wire[0])
            }else{
                return endNodes;
            }
        });
        
        answer = Math.min(answer, getConnected(newNodes));
    })
    return answer;
}

