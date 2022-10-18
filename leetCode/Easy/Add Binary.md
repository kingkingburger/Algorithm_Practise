## Add Binary

```js
var addBinary = function(a, b) {
    const alength = a.length;
    const blength = b.length;
    if(alength > blength){
        b = b.padStart(alength,'0');
    }else{
        a = a.padStart(blength,'0')
    }

    let splita = a.split('');
    let splitb = b.split('');
    let carry = 0;
    let result = "";
    
    for (let i = a.length - 1; i >= 0 ; i--) {
        if(splita[i] === "1" && splitb[i] === "1"){ // 1 + 1
            carry ? (result = "1" + result ): (result = "0" + result);
            carry = 1;
        }else if(splita[i] === "0" && splitb[i] === "0") { // 0 + 0
            carry ? (result = "1" + result) : (result = "0" + result);
            carry = 0;
        } else{ // 1 + 0
            if(carry){
                result = "0" + result;
                carry = 1;
            }else{
                result = "1" + result;
                carry = 0;
            }
        }
    }
    
    if(carry){
        result = "1" + result;
    }
    return result;
};
```

진짜 비트연산하듯이 for문 돌려가지고 계산했습니다.

(1+1), (0+0), (1+0) 의 경우를 3가지를 나눠가지고 carry를 결정했습니다.



좀더 빠른 로직이 없을까 다른분의 코드를 보았습니다.

```js
var addBinary = function(a, b) {
  const aBin = `0b${a}`
  const bBin = `0b${b}`
  const sum = BigInt(aBin) + BigInt(bBin)
  return sum.toString(2)
};
```

~~여기서 궁금했던게 백틱(`)안에서 변수를 쓰면 그 변수가 int형으로 바뀌는거같습니다. 원래 a는 문자열인데 아무런 조작없이 백틱안에 넣어서 int형처럼 쓰이고 있습니다.~~

```js
let a = BigInt("0b"+"111");
```

이건 `7n`으로 출력됩니다. 문자열 앞에 0b가 있고 **convert**를 하면 접두사를 적용시키는거 같습니다. 무작정 다른 진수로 바뀌는건 아니였습니다.



a,b 문자열을 Binary로 만들고 BigInt로 감싸서 다시 Binary로 만드는 형태였습니다.

처음에 문자열을 Binary로 만들 때 0b라는 접두사를 썻습니다.



#### 자바스크립트에서 2진수, 8진수, 16진수를 입력하는 방법에 대해서 알아보겠습니다.

2진수(**b**inary): **0b** (숫자 0과 알파벳 b)

8진수(**o**ctal):   **0o** (숫자 0과 알파벳 o)

16진수(he**x**adeciaml): **0x** (숫자 0과 알파벳 x)



숫자 11을 2진법, 8진법, 10진법, 16진법으로 입력하고 그 결과를 확인해보겠습니다.

```js
var aa = 0b11;   // 2진법(binary) # (1*2) + (1*1) = 3 
console.log(aa); // 출력: 3
```

```js
var bb = 0o11;   // 8진법(octal)  # (1*8) + (1*1) = 9
console.log(bb); // 출력: 9
```

```js
var cc = 11;     // 10진법(decimal) # (1*10) + (1*1) = 11
console.log(cc); // 출력: 11
```

```js
var dd = 0x11;   // 16진법(hexadecimal) # (1*16) + (1*1) = 17
console.log(dd); // 출력: 17
```

참고로 dd변수에 입력된 숫자 17(16진수 11)을 toString을 이용해서 16진법 문자열로 출력해보겠습니다. 

```js
console.log(dd.toString(16)); // 출력: 11
```

