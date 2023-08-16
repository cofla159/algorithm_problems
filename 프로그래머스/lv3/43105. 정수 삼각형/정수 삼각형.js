function solution(triangle) {
    const memoSum = [triangle[0]];
    
    for (let i = 1; i < triangle.length; i++){
        const temp = [];
        for (let j = 0; j <= i; j++){
            let leftSum = 0;
            let rightSum = 0;
            if ((j-1) >= 0){
                leftSum = memoSum[i-1][j-1] + triangle[i][j];
            }
            if (j <= i-1){
                rightSum = memoSum[i-1][j] + triangle[i][j];
            }
            temp.push(Math.max(leftSum, rightSum));
        }
        memoSum.push(temp);
    }
    return Math.max(...memoSum[triangle.length-1]);
}