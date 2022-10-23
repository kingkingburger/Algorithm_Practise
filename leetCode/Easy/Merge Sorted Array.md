## Merge Sorted Array

```js
var merge = function (nums1, m, nums2, n) {
    while(nums1.length > m){
        nums1.pop();
    }
    nums1.push(...nums2);
    nums1.sort((a,b)=>a-b);
    console.log(nums1);
};
```

- 첫 번째 nums1 배열은 m보다 많이 들어오는경우가 있습니다. 그래서 m만큼 잘라줍니다.
- nums1과 nums2배열을 합칩니다.
- nums1을 sort합니다.



다른분의 코드도 봤습니다. 

```js
var merge2 = function (nums1, m, nums2, n) {
    let insertPos = m + n + 1;
    m--;
    n--;
    while (n >= 0) {
        nums1[insertPos--] = nums1[m] > nums2[n] ? nums1[m--] : nums2[n--];
    }
};
```

nums1 배열을 다시 정의하는 형태였습니다.

맨 끝부터 nums1의 끝과 nums2의 끝을 비교해가지고 nums1 배열의 끝부터 채워나가는 형태였습니다.