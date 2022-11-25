## Best Time to Buy and Sell Stock

```js
var maxProfit = function (prices) {
  let buy = 0; // buy를 중심으로 이동
  let seil = 1; // 배열 오른쪽으로 계속 이동
  let max_profit = 0;
  while (seil < prices.length) {
    if (prices[seil] > prices[buy]) {
      max_profit = Math.max(max_profit, prices[seil] - prices[buy]);
    } else {
      buy = seil;
    }
    seil++;
  }
  return max_profit;
};
```

배열 전체를 while문을 돕니다.

만약 최고 값이 나오면 최고값을 max_profit에 저장합니다.

아니면 배열을 한칸씩 오른쪽으로 이동합니다. 

![image](https://assets.leetcode.com/users/images/c0c86dc7-f7fa-4be7-85f9-61e629aa67ae_1643686591.6894035.jpeg)
