function solution(progresses, speeds) {
    let answer = [];
    const left = progresses.map((p,i) => Math.ceil((100-p)/speeds[i]));
    left.reverse();
    
    let deploy = 0;
    let maxLeft = left[left.length-1];

    while (left.length){
        const popped = left.pop();
        if (popped > maxLeft){
            answer.push(deploy);
            deploy = 1;
            maxLeft = popped;
        }else{
            deploy++;
        }
    }
    answer.push(deploy);
    return answer;
}