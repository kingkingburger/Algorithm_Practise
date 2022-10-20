## Plus One

```js
var plusOne = function(digits) {
    let num = BigInt(Number(0));
    for (let i = 0; i < digits.length; i++) {
        let ditisNum = BigInt(digits[(digits.length - 1) - i]); //BigInt형
        let positioning = (10n ** BigInt(Number(i)));//BigInt형
        num += ditisNum * positioning;
    }
    num = num + 1n;
    return String(num).split("");
};
```

js에서 Number는 최대 2^53-1 까지 안전하게 다룰 수 있다고 합니다. 

그래서 2^53보다 큰값을 원하면 에러가 납니다. 그러니 더 큰 메모리 타입인 `BinInt`를 사용했습니다.

BigInt는 BigInt 끼리만 비교, 연산이 가능합니다.



#### 선언방법

```js
let a = 9007199254740996n; // 리터럴 뒤에 n을 붙여 선언
let b = BigInt(Number.MAX_SAFE_INTEGER + 6); // 혹은 BigInt로 선언

console.log(a, b); // 9007199254740996n, 9007199254740996n
```

`6145390195186705544`란 어마어마한 수도 계산할 수 있게됩니다.

그래서 변수인 num, i 에는 Bigint()로 감쌌고 자리수를 정해주는 10은 뒤에다가 n을 붙혔습니다.



#### 다른 풀이 방법

```js
var plusOne2 = function(digits) {
    for (let i = digits.length - 1 ; i >= 0 ; i--) {
        digits[i]++;
        if(digits[i] > 9){
            digits[i] = 0;
        }else{
            return digits;
        }
    }
    digits.unshift(1);
    return digits;
};
```

BigInt로 하는건 너무 느렸습니다. 배열을 한번에 돌면서 +1을 하는 다른 방법을 찾아봤습니다.

digits 배열을 거꾸로 돌면서 +1식 합니다. 만약에 10이 된다면 for문을 또 돕니다. 아니라면 +1한 상태로 digits 배열을 반환합니다. 

마지막까지가서 for문이 끝난다면 배열을 모두 0으로 가득차있을것입니다. 그러면 맨 왼쪽에서 숫자를 붙여주는 unshift()를 사용합니다.

이 방법이 휠씬더 빠릅니다. 보다 수학적으로 사고해야겠습니다.
