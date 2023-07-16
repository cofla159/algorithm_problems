function solution(n) {
    const oneCount = n.toString(2).match(/1/g).length;
    while(n++){
        if (n.toString(2).match(/1/g).length === oneCount) break;
    }
    return n;
}