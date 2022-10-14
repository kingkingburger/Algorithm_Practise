## Length Of Last Word

```js
var lengthOfLastWord = function(s) {
    s = s.trimEnd();
    let result = 0;
    for (let i = s.length-1; i > 0; i--) {
        result++;
        if(s[i-1] === ' '){ // 글자 왼쪽에 ' '있다면 그대로 끝넴
            return result;
        }
    }
    return s.length;
};
```

- 먼저 trimEnd()로 오른쪽 문자열 공백을 모두 없에줍니다.
- for문을 도는데 문자열의 거꾸로 돕니다.
- 거꾸로 돌다가 앞에 공백(' ')이 있다면 그동안 걸어온 길의 값을  return 합니다.