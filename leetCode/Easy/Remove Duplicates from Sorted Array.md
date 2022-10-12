## Remove Duplicates from Sorted Array

```js
var removeDuplicates = function (nums) {

    // 기준 숫자를 정함
    let standardNum = nums[0];
    for (let i = 1; i < nums.length; i++) {
        // 기준숫자와 다르면 기준숫자 바꿈
        if (standardNum !== nums[i]) {
            standardNum = nums[i];
        } else {
            // 기준숫자가 중복되면 '_'문자로 바꿈
            nums[i] = '101';
        }
    }
    result = nums.sort((a,b) =>{
        return a - b;
    });
    console.log(result);
    //결과값에 '_'가 있다면 그 앞 인덱스로 리턴, 아니면 배열의 길이를 리턴
    console.log(result.indexOf('101') > 0 ? result.indexOf('101') : result.length);
    console.log(result);
};
```

처음에 생각한 로직입니다.

기준점인 숫자를 고르고 for문으로 배열을 모두 돈다음 다른 숫자가 나오면 '101'문자로 바꿉니다.

for문이 끝나면 유니코드의 순서대로 sort를 합니다. 

배열에 '101'의 인덱스가 있다면 그 인덱스를 리턴 합니다.

위 방식으로는 속도가 빠르게 나오진 않았습니다. 사이트의 솔루션을 보니 다른 방법이 있었습니다.

```js
var removeDuplicates = function (nums) {

    // 기준 숫자를 정함
    let insertIndex = 1;
    for (let i = 1; i < nums.length; i++) {
        // 기준숫자와 다르면 기준숫자 바꿈
        if (nums[i-1] !== nums[i]) {
            nums[insertIndex] = nums[i];
            //그 다음에 숫자받을 
            insertIndex++;
        }
    }

    return insertIndex;

};
```

nums 배열의 인덱스를 돌리는 것입니다.

inesrtIndex는 중복되는 숫자의 인덱스를 알려주는 역할을 합니다.

for문을 돌면서 만약 이전의 수와 다른 수가 있다면 그 인덱스에 값을 바꿔줍니다. 만약 중복이라면 넘어갈 것입니다.

