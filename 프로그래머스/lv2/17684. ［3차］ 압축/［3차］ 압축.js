function solution(msg) {
    let answer = [];
    let dict = Array(27).fill().map((v,i) => {
        if (i === 0) return null;
        return String.fromCharCode(i+64);
    })

    let i = 0
    while (i < msg.length){
        let w = msg[i];
        let addIdx = i+2;
        
        while (addIdx < msg.length+1 && dict.includes(msg.slice(i, addIdx))){
            w = msg.slice(i, addIdx);
            addIdx++;
        }
        answer.push(dict.indexOf(w));
        dict.push(msg.slice(i,addIdx));
        i = addIdx-1;
    }
    return answer;
}