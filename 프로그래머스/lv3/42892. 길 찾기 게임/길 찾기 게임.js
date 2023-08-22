function solution(nodeinfo) {
    const nodeNumInfo = nodeinfo.map((el,i) => [i+1, ...el]);
    nodeNumInfo.sort((a,b) => a[1]-b[1]);
    nodeNumInfo.sort((a,b) => b[2]-a[2]);
    
    let pre = [];
    let post = [];
    function order(sorted){
        const [num,x,y] = sorted[0];
        let left = [];
        let right = [];
        
        for (let i = 1; i < sorted.length; i++){
            if (sorted[i][1] < x) left.push(sorted[i]);
            else right.push(sorted[i]);
        }
        
        pre.push(num);
        if (left.length) order(left);
        if (right.length) order(right);
        post.push(num);
    }
    order(nodeNumInfo);
    
    return [pre, post];
}