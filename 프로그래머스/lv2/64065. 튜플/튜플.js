function solution(s) {
    if (!s.includes("},{")) return [parseInt(s.slice(2, s.length-2))];
    
    let inputArr = s.slice(2,s.length-2).split("},{").map(el => el.split(","));
    
    inputArr.sort((a,b) => a.length-b.length);
    let answer = [];
    
    inputArr.forEach(arr => {
        answer.push(...arr.filter(el => !answer.includes(el)))

    })
    
    return answer.map(el => parseInt(el))
}