function solution(n) {
    let arr = [];
    for (let i = 1; i <= n; i++){
        arr.push(Array(i).fill(0));
    }
    const end = n*(n+1)/2;
    let count = 0;
    let [i,j] = [-1,0];
    let mode = 'left';
        
    while (count < end){
        if (mode === 'left'){
            if (++i <= n-1 && !arr[i][j]){
                arr[i][j] = ++count;
            }else{
                i--;
                mode = 'bottom';
            }
        }else if (mode === 'bottom'){
            if (++j <= i && !arr[i][j]){
                arr[i][j] = ++count;
            }else{
                j--;
                mode = 'right';
            }
        }else if (mode === 'right'){
            if (--i >= 0 && --j >= 0 && !arr[i][j]){
                arr[i][j] = ++count;
            }else{
                i++;
                j++;
                mode = 'left';
            }
        }
    }
    
    return arr.flat();
}
