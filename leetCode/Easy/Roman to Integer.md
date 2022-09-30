## Roman to Integer

```js
const alpha = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

var romanToInt = function(s) {
  let result = 0;
  let splitwords = s.split("");
  for(let i = 0, length = splitwords.length; i < length ; i++){
      let word = splitwords[i];
      let rightword = splitwords[i+1];
      if(alpha[word] < alpha[rightword]){
          result -= alpha[word];
      }else{
          result += alpha[word];
      }
  }
    return result;
};
```

alpha라는 기준 딕셔너리를 만듭니다.

for문을 돌면서 글자를 오른쪽 글자와 비교합니다. 만약 현재 for문에서 도는 글자보다 오른쪽 글자가 크다면 단위가 바뀐것이니 전체 결과값에 현재 값은 빼줍니다.

전체적으로 봤을 때 결과값의 크기를 재는것입니다. 중간중간에 단어들의 크기를 잴 필요가 없었던것입니다.

for문을 돌다보면 마지막 원소까지 가게됩니다. 그럼 오른쪽에 아무것도 없으니 `undefine` 된 객체가 와서 무조건 else문으로 들어가게 됩니다.

그래서 무조건 마지막 문자는 전체값에 더하게 되었습니다. 마지막까지 더해야 하니깐요

