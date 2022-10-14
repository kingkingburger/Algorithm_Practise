## Search Insert Position

처음에 한 생각입니다.

```js
for (let i = 0, length = nums.length; i < length; i++) {
    if (nums[i] >= target) {
        return i;
    }
}
return nums.length;
```

다들 이걸 먼저 떠올리셨을 것입니다. O(n)으로 동작합니다.

이분탐색으로 코드를 사용할 수 있습니다.

```js
var searchInsert = function (nums, target) {

    // 배열의 첫번째 인덱스를 정한다.
    let start = 0
    // 배열의 마지막 인덱스을 정한다.
    let end = nums.length - 1;
    // 배열의 가운대를 기준값으로 잡는다.
    let mid = Math.round((start + end) / 2);
    // 배열을 돈다.
    while (start <= end) {
        if (nums[mid] === target) {
            return mid;
        } else if (nums[mid] <= target) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
        mid = Math.round((start + end) / 2);
        // 이걸 반복해서 배열의 최적 인덱스를 찾는다.
    }
    //left의 값이 배열의 insert할 인덱스이다.
    return start;
};

```

이렇게 이분탐색을 사용해봤습니다. 

이분탐색을 사용할 때 주의해야할 점은 start와 end가 언제끝나냐를 정하는 것입니다.

저는 start와 end가 같거나 start가 더 작은때를 정했습니다. 이러면 start는 mid의 +1에 가있을것입니다. 

그리고 그 start 인덱스가 insert할 배열의 자리가 됩니다.