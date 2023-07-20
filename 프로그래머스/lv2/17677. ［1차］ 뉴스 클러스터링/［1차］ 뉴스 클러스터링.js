function solution(str1, str2) {
    str1 = str1.toLowerCase();
    str2 = str2.toLowerCase();
    const set1 = makeSets(str1);
    let set2 = makeSets(str2);
    let interCount = 0;
    
    if (set1.length === 0 && set2.length === 0) return 65536;
    set1.forEach(el1 => {
        if (set2.includes(el1)){
            interCount++;
            const idx = set2.indexOf(el1);
            set2.splice(idx, 1);
        } 
    })
    return Math.floor(interCount/(set1.length+set2.length)*65536);
}

function makeSets(str){
    let set = [];
    for (let i = 0; i < str.length; i++){
        const el = str.slice(i, i+2);
        if (el.length == 2 && !el.match(/[^a-z]/g)) set.push(el);
    }
    return set;
}