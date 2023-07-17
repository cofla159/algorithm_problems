function solution(arr) {
    arr.sort((a,b) => a-b);
    let answer = arr[arr.length-1];
    let i = 1;
    
    while(arr.reduce((acc, cur) => acc || answer % cur, 0)){
        answer = arr[arr.length-1] * i++;
    }
    return answer;
}