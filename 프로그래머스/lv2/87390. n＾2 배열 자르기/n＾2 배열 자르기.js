function solution(n, left, right) {
    let arr= [];
    for (let flatIdx = left; flatIdx <= right; flatIdx++){
        const i1 = Math.floor(flatIdx / n);
        const i2 = Math.floor(flatIdx % n);
        
        if (0 <= i2 && i2 <= i1){
            arr.push(i1+1);
        } else{
            arr.push(i2+1);
        }
    }
    return arr;
}