function solution(n, k) {
    let count = 0;
    const newN = n.toString(k);
    newN.split(/0+/).forEach(el => {
        if (el && isPrime(parseInt(el))){
            count++;
        }})
    return count;
}

function isPrime(n){
    if (n===1) return false;
    for (let i = 2; i <= Math.sqrt(n); i++){
        if (n%i === 0) return false;
    }
    return true;
}