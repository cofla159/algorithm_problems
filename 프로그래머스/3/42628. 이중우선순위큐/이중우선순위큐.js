function solution(operations) {
    const queue = [];
    const insert = (num) => {
        let idx = 0;
        for (const el of queue){
            if (el > num) break;
            idx++;
        }
        if (!idx){
            queue.unshift(num);
        }else if (idx >= queue.length){
            queue.push(num);
        }else{
            queue.splice(idx, 0,num);
        }
        console.log(queue);
    }
    
    const delMin = () => {
        queue.shift();
    }
    
    const delMax = () => {
        queue.pop();
    }
    
    for (const op of operations){
        if (op[0] === "I"){
            insert(parseInt(op.split(" ")[1]));
        }else if (op[2] === "1"){
            delMax();
        }else{
            delMin();
        }
    }
    return queue.length ? [queue[queue.length-1], queue[0]] : [0,0];
}