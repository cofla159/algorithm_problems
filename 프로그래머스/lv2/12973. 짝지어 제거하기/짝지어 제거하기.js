function solution(s)
{
    let stack = [];
    for (char of s){
        if (stack[stack.length-1] === char) {
            stack.pop();
        }
        else {
            stack.push(char);
        }
    }
    return stack.length === 0 ? 1 : 0;
}