const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((num) => +num);

input.shift();
function solution(testcase) {
  testcase = testcase.sort((a, b) => a - b);
  for (let num of testcase) {
    console.log(num);
  }
}

solution(input);
