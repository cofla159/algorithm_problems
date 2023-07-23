function solution(n, t, m, p) {
    const needStrLen = m*t;
    let str = " ";
    let i = 0;
    while (str.length < needStrLen){
        str += (i++).toString(n);
    }
    let answer = "";
    for (let i = 1; answer.length < t; i++){
        if (i%m === p || (m===p && i % m === 0)) answer+=str[i].toUpperCase();
    }
    return answer;
}