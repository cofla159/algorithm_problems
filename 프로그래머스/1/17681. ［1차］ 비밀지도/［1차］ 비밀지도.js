function solution(n, arr1, arr2) {
    const answer = Array(n).fill().map(el => Array(n).fill(' '));
    for (let i = 0; i < n; i++){
        const str1 = numTo2Num(arr1[i], n);
        const str2 = numTo2Num(arr2[i], n);
        for (let j = 0; j < n; j++){
            if (str1[j] === '1' || str2[j] === '1'){
                answer[i][j] = '#'
            }
        }
    }
    return answer.map(line => line.join(''));
}

const numTo2Num = (num, maxLen) => {
    let answer = '';
    for (let i = maxLen-1; i >= 0; i--){
        if (num - Math.pow(2, i) >= 0){
            answer += '1';
            num -= Math.pow(2, i)
        }else {
            answer += '0'
        }
    }
    return answer
}