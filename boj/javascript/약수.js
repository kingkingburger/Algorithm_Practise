const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const nums = input[1].split(" ").map((num) => +num);

function solution(testcase) {
  console.log(Math.max(...testcase) * Math.min(...testcase));
}

solution(nums);
