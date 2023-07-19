function solution(cacheSize, cities) {
    if (!cacheSize) return cities.length*5;
    let queue = new Array(cacheSize);
    let time = 0;
    
    cities.forEach(city => {
        city = city.toLowerCase();
        if (queue.includes(city)){
            time += 1;
            queue = queue.filter(cache => cache !== city); 
            queue.push(city);
        }else {
            time += 5;
            if (queue.length === cacheSize) queue.shift(); 
            queue.push(city);
        }
    })
    return time;
}