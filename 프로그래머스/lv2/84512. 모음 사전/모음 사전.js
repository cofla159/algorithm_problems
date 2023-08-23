function solution(word) {
    let char = ['A', 'E', 'I', 'O', 'U'];
    
    const getPermutations = function (arr, selectNumber) {
        const results = [];
        if (selectNumber === 1) return arr.map((el) => [el]); 
        arr.forEach((fixed, index, origin) => {
            const combinations = getPermutations(origin, selectNumber - 1); 
            const attached = combinations.map((el) => [fixed, ...el]); 
            results.push(...attached); 
        });
        return results;
    }
    
    const dictionary = [...getPermutations(char, 1),...getPermutations(char, 2),...getPermutations(char, 3),...getPermutations(char, 4),...getPermutations(char, 5)].sort();
    return dictionary.findIndex(el => el.join("") === word)+1;
}

