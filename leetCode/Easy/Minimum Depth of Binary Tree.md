## Minimum Depth of Binary Tree

```js
var minDepth = function(root) {
    if(!root) return 0;
    let left = minDepth(root.left);
    let right = minDepth(root.right);
    return (left === 0 || right === 0) ? left + right + 1 : Math.min(left, right) + 1;
};
```

트리의 최대 길이 구하는 방법에서 아이디어를 얻었습니다.

처음에 양쪽 트리의 최대길이를 구하고 비교하면 되지 않을까 생각했습니다.

```js
var minDepth = function(root) {
    if(!root) return 0;
    let result = 0;
    const left = maxDepth(root.left);
    const right = maxDepth(root.right);
    
    if(left === 0) result = right + 1;
    else if(right === 0) result = left + 1;
    else result = Math.min(left, right) + 1;
    

    return result;
};

var maxDepth = function(root){
    if(!root) return 0;
    return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
}
```

그래서 최대길이 가져오는 코드를 가져와서 해본결과 트리의 최대길이보다 짧은 것이 있는경우 문제가 되었습니다.

![image](https://user-images.githubusercontent.com/65094518/201349209-2ee9a8ee-3d9f-4cee-9e40-d986689f9910.png)



다른분의 코드를 보고 힌트를 얻었습니다.

```js
return (left === 0 || right === 0) ? left + right + 1 : Math.min(left, right) + 1;
```

왼쪽과 오른쪽이 둘중에 하나가 0이면 (=한쪽이 비어있다면) 다른 한쪽의 경우만 생각하면 되었습니다.

둘다 꽉꽉차있다면 왼쪽오른쪽을 비교하는 Math.min()을 사용하면 되었습니다.