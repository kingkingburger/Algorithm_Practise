## Convert Sorted Array to Binary Search Tree

```js
var sortedArrayToBST = function(nums) {
    let newNode = new TreeNode(nums[0],null,null), cur = newNode;
    
    const result = insertNode(nums, 0, nums.length-1);
    console.log(result);
    return result;
};

var insertNode = (num, left, right) =>{
    if(left > right) return null;
    let mid = Math.round((left + right) / 2);
    let Tree = new TreeNode(num[mid], null, null);
    Tree.left = insertNode(num, left, mid - 1);
    Tree.right = insertNode(num, mid + 1, right);
    return Tree;
}
```

다른분의 코드를 보고 풀었습니다.

설명이 너무 잘되어있었습니다.

Since `nums` is a sorted list, the middle element `nums[len(nums)//2]` must be the root node of `nums`.
Thus, after setting the middle element be the root, finding the middle element in the left subarry `nums[:len(nums)//2]` and right subarry `nums[len(nums)//2 + 1 : ]`

For example, `nums = [0, 1, 2, 3, 4, 5, 6, 7]`

배열의 반씩 쪼개서 배열의 가운데를 left, right로 지정하면 되는거였습니다.



![image](https://assets.leetcode.com/users/images/9b668608-b437-47d4-8816-8dfe9dbdd318_1660126464.7137046.png)