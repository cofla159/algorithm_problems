function solution(fees, records) {
    let carRecords = {};
    const [basicTime, basicFee, unitTime, unitFee] = fees;
    records.forEach(str => {
        const [time, carNum, inOut] = str.split(" ");
        if (!carRecords.hasOwnProperty(carNum)) carRecords[carNum] = [];
        carRecords[carNum].push(time);
    })
    const accTime = {};
    for (const car in carRecords){
        const inOut = carRecords[car];
        accTime[car] = 0;
        for (let i = 0; i < inOut.length; i+=2){
            if (i+1 >= inOut.length){
                accTime[car] += (new Date('2023-07-24T'+"23:59:00").getTime() - new Date('2023-07-24T'+inOut[i]+":00").getTime()) / 1000 / 60;
            }else{
                accTime[car] += (new Date('2023-07-24T'+inOut[i+1]+":00").getTime() - new Date('2023-07-24T'+inOut[i]+":00").getTime()) / 1000 / 60;
            }
        }
    }
    let answer = [];
    for (const car in accTime){
        if (accTime[car] <= basicTime) {
            answer.push([Number(car), basicFee]);
        }else {
            answer.push([Number(car), basicFee+Math.ceil((accTime[car] - basicTime) / unitTime) * unitFee]);
        }
    }
    return answer.sort((a,b) => a[0]-b[0]).map(el => el[1]);
}