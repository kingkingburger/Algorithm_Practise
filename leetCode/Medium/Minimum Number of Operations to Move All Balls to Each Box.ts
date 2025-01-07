function minOperations(boxes: string): number[] {
    const answer: number[] = [];
    const boxList = boxes.split("");

    for (let i = 0; i < boxList.length; i++) {
        let result = 0;

        for (let j = 0; j < boxList.length; j++) {
            if (i != j && boxList[j] === "1") {
                result += Math.abs(j - i);
            }
        }

        answer.push(result);
    }

    return answer;
}

console.log(minOperations("110")); //[1,1,3]
console.log(minOperations("001011")); //[11,8,5,4,3,4]