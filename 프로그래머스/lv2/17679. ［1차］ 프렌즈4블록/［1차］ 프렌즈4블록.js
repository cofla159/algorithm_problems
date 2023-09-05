function solution(m, n, board) {
    let count = 0;
    let rotated=[];
    board = board.map(line => line.split(""));
    for (let i = 0; i < n; i++){
        let tempArr = [];
        for (let j = m-1; j >= 0; j--){
            tempArr.push(board[j][i]);
        }
        rotated.push(tempArr);
    }
    let newBoard = rotated.map(arr => [...arr]);
    let flag = false;
    
    do{
        const del = new Set();
        flag = false;
        for (let i = 0; i < rotated.length-1; i++){
            for (let j = 0; j < rotated[i].length-1; j++){
                const r = rotated[i][j+1];
                const d = rotated[i+1][j];
                const rd = rotated[i+1][j+1];
                if (rotated[i][j] === r && rotated[i][j] === d && rotated[i][j] === rd){
                    flag = true;
                    del.add([i,j].join());
                    del.add([i+1,j].join());
                    del.add([i,j+1].join());
                    del.add([i+1,j+1].join());
                    newBoard[i][j] = 0;
                    newBoard[i+1][j] = 0;
                    newBoard[i][j+1] = 0;
                    newBoard[i+1][j+1] = 0;
                }
            }
        }
        newBoard = newBoard.map(arr => arr.filter(el => el !== 0));
        rotated = newBoard.map(arr=> [...arr]);
        count += del.size;
    } while(flag);
    
    return count;
}

