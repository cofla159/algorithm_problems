function solution(dirs) {
    const move = {
        U: [0, 1],
        D: [0, -1],
        R: [1, 0],
        L: [-1, 0],
    };
    const visited = new Set();
    let now = [0, 0];
    let count = 0;

    dirs.split("").forEach(dir => {
        const [dx, dy] = move[dir];
        const newX = now[0] + dx;
        const newY = now[1] + dy;

        if (-5 <= newX && newX <= 5 && -5 <= newY && newY <= 5) {
            const road = `${now[0]}${now[1]}${newX}${newY}`;
            const reverseRoad = `${newX}${newY}${now[0]}${now[1]}`;
            if (!visited.has(road)) {
                visited.add(road);
                visited.add(reverseRoad);
                count++;
            }
            now = [newX, newY];
        }
    });

    return count;
}
