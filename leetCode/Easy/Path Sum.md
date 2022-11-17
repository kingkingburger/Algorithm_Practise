## Path Sum

```js
var hasPathSum = function(root, targetSum) {
    if(!root) return false;
    
    if(root.left === null && root.right === null && targetSum - root.val === 0) return true;
    
    return hasPathSum(root.left, targetSum - root.val) || hasPathSum(root.right, targetSum - root.val)
};
```

- 리프노드인지 판단합니다. 
- 만약 현재 targetSum과 현재 값이 0이 된다면 true를 return 합니다.
- 결과값이 하나라도 true가 나오면 true가 되게끔 합니다.