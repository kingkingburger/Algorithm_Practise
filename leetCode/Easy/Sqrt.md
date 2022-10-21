## Sqrt

```js
var mySqrt = function(x) {
    let res = Math.pow(x,0.5);
    console.log(Math.floor(res));
};
```

첫 번째 답입니다. Math.pow를 쓰지 말라고했지만 이게 제일 빨랐습니다.



```js
let result = 1;
while(result*result <= x) result++;
return result - 1;
```

두 번째 답입니다. 제곱을 계속 늘려 원하는 수보다 커지면 그 수의 -1 한 값이 제곱근이 됩니다.

브루드포스 형태로 해결합니다.



```js
var mySqrt3 = function(x) {
    let left = 1;
    let right = Math.floor(x / 2) + 1;
    let mid;

    while(left <= right){
        mid = Math.floor((left + right) / 2);
        //제곱값 찾기
        if(mid*mid > x){
            right = mid - 1;
        }else if(mid*mid < x){
            left = mid + 1;
        }else{
            return mid;
        }
    }
    return right;
};
```

다른 분의 답을 보니 이분탐색으로 찾을 수도 있습니다.

x의 제곱근은 무조건 [1,n/2+1] 사이에 있습니다. 그래서 이 범위를 이분탐색해서 x근처의 제곱근 값을 찾을 수 있습니다. 만약 못찾는다면 (n/2+1) 값을 리턴합니다.