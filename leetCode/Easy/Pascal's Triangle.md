#### Pascal's Triangle

```js
var generate = function (numRows) {
  const number = [];
  number.push([1]);

  for (let n = 1; n < numRows; n++) {
    const arr = [];
    for (let r = 0; r <= n; r++) {
      const element = factorial(n) / (factorial(n - r) * factorial(r));
      arr.push(element);
    }
    number.push(arr);
  }
    return number;
};

function factorial(n) {
  var result = 1;
  for (var i = 2; i <= n; i++) result *= i;
  return result;
}
```

처음에 보고 dp문제인가? 하고 생각해보니 어떠한 패턴이 있다고 생각했습니다.

파스칼의 삼각형은 조합을 가지고 푸는 문제였습니다.

![image](https://user-images.githubusercontent.com/65094518/202878146-9161a6d3-17d5-4179-82ed-707c6e25a6ae.png)

각 패턴을 살펴보면 2개중에 0개... 2개중에 1개... 2개중에 2개... 이런식으로 삼각형이 구성되어있었습니다.

nCr은 ((n!) / (n-r)! * r! )의 식을 가지고 있습니다. 2중 for문으로 위 식을 적용해서 factorial로 값을 채워주면 됩니다.



#### 🟩다른방법으로 풀기

dp형태로도 풀 수 있었습니다.

```js
var generate = function(numRows) {
    var i = 0;
    var j = 0;
    // Create an array list to store the output result...
    var res = [];
    // For generating each row of the triangle...
    for (i = 0; i < numRows; i++) {
        res.push(Array(i + 1));       // 2중 배열로 만들기
        for (j = 0; j <= i; j++) {
            // Primary...
            if (j === 0 || j === i) {
                res[i][j] = 1;
            }
            else {
                // Calculate the elements of a row, add each pair of adjacent elements of the previous row in each step of the inner loop.
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j];
            }
        }
    }
    return res;      // Return the output list of pascal values...
};
```

row -1 들 중에 j -1인것, j인것을 가져와서 해당 row의 j를 구할 수 있었습니다.

더 빠르고 직관적인거 같습니다. 처음부터 dp 생각을 했지만 다른 접근을 해봤던것도 도움이 되었스빈다.