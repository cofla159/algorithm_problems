function solution(n, words) {
    turn = 0;
    used = [];
    flag = false;
    for (let i = 0; i < words.length; i++){
        turn++;
        if (i === 0) {
            used.push(words[i]);
            continue;
        }
        let lastWord = used[used.length-1];
        if (words[i][0] === lastWord[lastWord.length-1] && !used.includes(words[i])){
            used.push(words[i]);
        }else{
            flag = true;
            break;
        }
    }
    if (flag){
        if ((turn)%n){
            return [turn%n, parseInt(turn/n)+1]
        }else{
            return [n, parseInt(turn/n)]
        }
    }else{
        return [0,0];
    }
}