function solution(s) {
    let count = 0;
    let zero = 0;
    while (s !== "1"){
        count++;
        let zeroNum = s.match(/0/g);
        if (zeroNum){ 
            zero += zeroNum.length;
            s = s.replaceAll("0", "");         
        }
        s = (s.length).toString(2);
    }
    
    return [count, zero];
}