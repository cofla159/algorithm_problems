function solution(s){
    if (s[0] === ")") return false;
    const stack = [];
    
    for (let i = 0; i< s.length; i++){
        if ((stack[stack.length-1] === "(" && s[i] === ")") ) stack.pop();
        else stack.push(s[i]);
    }
    return stack.length === 0;
}