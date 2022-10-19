## Climbing Stairs

```js
var climbStairs = function(n) {
    let numCount = [1,2,3];
    for (let i = 3; i < n; i++) {
        numCount[i] = numCount[i-1] + numCount[i-2];
    }
    console.log(numCount[n-1]);
};

climbStairs(1);
```

문제를 처음보자마자 dp문제라는걸 직감했습니다.

`1, 2`로 만들 수 있는 최대수들을 dp형태로 더하면 되었습니다.

1,2,3은 `1,2`로 더할 수 있는 `숫자의 개수`가 1,2,3으로 정해져있습니다. 

만약 4의 `1,2`로 더할 수 있는 `숫자의 개수`는 
2의 `1,2`로 더할 수 있는 `숫자의 개수` + 3의 `1,2`로 더할 수 있는 `숫자의 개수`입니다.