function solution(skill, skill_trees) {
    let count = 0;
    const skillType = skill.split("");
    skill_trees.forEach(tree => {
        const filteredTree = tree.split("").filter(sk => skillType.includes(sk));
        const tempSkill = [...skillType];
        for (let i = 0; i < filteredTree.length; i++) {
            if (filteredTree[i] === tempSkill[0]){
                tempSkill.shift();
            }else{
                count--;
                break;
            }
        }
        count++;
    })
    return count;
}