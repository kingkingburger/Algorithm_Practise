## Remove Element

```js
var removeElement = function (nums, val) {

    //제거할 인덱스
    let removeIndex = nums.length - 1;
    let result = 0;
    for (let i = 0, length = nums.length; i < length; i++) {
        //이전 값이 제거되야할 값이라면
        if (nums[i] === val) {
            while(nums[removeIndex] === val){
                removeIndex--;
            }
            nums[i] = nums[removeIndex];
            removeIndex--; // 바꿔야할 인덱스 거꾸로
            result++;
        }
    }
    console.log(nums.length - result);
};
```

이렇게 로직을 짜봤습니다.

nums를 for문을 돌다가 제거할 인덱스가 나타나면 nums배열의 거꾸로 있는 값을 넣어줍니다.

거꾸로 있는것이 val 값과 같다면 인덱스를 거꾸로 돌려서 val이 아닌 값의 인덱스를 얻어옵니다.



다른분들의 코드를 보았습니다.

```js
var removeElement2 = function (nums, val) {

    //제거할 인덱스
    let removeIndex = 0;
    for (let i = 0, length = nums.length; i < length; i++) {
        //이전 값이 제거되야할 값이라면
        if (nums[i] !== val) {
            nums[removeIndex] = nums[i];
            removeIndex++;
        }
    }
};
```

for문에다가 배열을 돌립니다. 만약 val값이 아니면 지정해둔 인덱스와 바꿉니다.

만약 val값이면 그것의 인덱스가 저장이 됩니다. 그리고 val값이 아닌걸 만나면 배열의 차례대로 인덱스를 증가시키면서 val이 아닌 값으로 바꾸게 됩니다.



