## Longest Common Prefix

```js
var longestCommonPrefix = function (strs) {
    let result = '';
    const standard = strs[0];

    if(strs.length === 1){
        return standard;
    }

    for (let i = 0; i < standard.length; i++) {
        for (let j = 1; j < strs.length; j++) {
            const word = strs[j][0];

            if (word === standard[i]) {
                strs[j] = strs[j].substring(1);
                if (j === strs.length - 1) {
                    result += word;
                }
            } else {
                return result;
            }

        }
    }
    return result;
};
```

처음에 푼 코드 입니다.



strs 문자들이 들어온것중 1번째 꺼를 기준으로 삼습니다.

그리고 strs 배열을 돕니다. 다른 단어들을 찾는 것이죠

단어들의 맨 앞이 같으면 result에 맨앞 문자를 더하고 아니면 지금까지 더해온 값을 return 합니다.

주의할 점은 단어들을 모두 돌기 전까지는 result에 맨앞 문자를 더하지 않는 것입니다. 그래서 if문으로 2 번째 for문의 마지막에 단어를 더합니다. 



#### 다른사람의 코드 

```js
var longestCommonPrefix = function (strs) {
    let prefix = strs[0];

    for (let i = 0; i < strs.length; i++) {
        while(strs[i].indexOf(prefix) != 0){
            prefix = prefix.substring(0, prefix.length - 1);
            if(prefix === '') return "";
        }
    }
    return prefix;
};
```

훨씬더 깔끔한 코드가 있었습니다. 

![Finding the longest common prefix](https://leetcode.com/media/original_images/14_basic.png)



제가 생각한 계념이랑 비슷한 부분이 있습니다.

그런데 여기는 문자열을 통째로 가져와서 문자열이 같은 부분의 index를 찾습니다. 만약에 있다면 그건 0보다 큰값일 태니 while문이 계속 동작하게 됩니다. 

while문안에서는 문자열 끝부분은 1칸씩 자릅니다. 

즉, 문자열을 비교해서 indexOf()가 0으로 나온다면 그 문장열은 접두사가 되는것입니다. 
비교해서 indexOf()가 0이 아닌값은 -1입니다. 같은 곳이 없으니깐요