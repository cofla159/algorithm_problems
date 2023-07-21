function solution(priorities, location) {
    let count = 0;
    while(1){
        // for (let i = 0; i <5 ;i++){
        const now = priorities.shift();
        if (now >= Math.max(...priorities)){ 
            count++;
            if (!location) break;
        }else {
            priorities.push(now);
        }
        if (!location){
            location = priorities.length-1;
        }else{
            location--;
        }
    }
    return count;
}