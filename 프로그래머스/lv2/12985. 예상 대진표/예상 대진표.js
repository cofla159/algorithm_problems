function solution(n,a,b)
{   
    let count = 1;
    let nextNumA = Math.ceil(a/2);
    let nextNumB = Math.ceil(b/2); 
    while(nextNumA !== nextNumB){
        count++;
        nextNumA = Math.ceil(nextNumA/2);
        nextNumB = Math.ceil(nextNumB/2); 
    }
    return count;
}