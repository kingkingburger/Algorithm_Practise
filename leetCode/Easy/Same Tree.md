## Same Tree

```js
var isSameTree = function(p, q) {
    let result1 = [];
    let result2 = [];
    
    inorder(p, result1);
    inorder(q, result2);
    
    if(checkSame(result1,result2)) return true;
    else return false;
};

var inorder = (node, res) =>{
    if(!node) return null;
    if(node.left) {
        res.push(null);
        inorder(node.left, res);
    }
    res.push(node.val);
    if(node.right) inorder(node.right, res);
}

const checkSame =(arr1, arr2) => {
    let arr1Length = arr1.length;
    if(arr1Length != arr2.length) return false;
    
    while(arr1Length--){
        if(arr1[arr1Length] !== arr2[arr1Length]) return false;
    }
    return true;
}
```

저는 중위순회로 트리를 돌면서 그 결과값이 같은지 안같은지 판별했습니다

inorder()는 중위순회를 하는 것입니다. 결과는 result1,result2 배열에 들어가게 됩니다.

checkSame은 2개의 배열이 같은지 다른지 판별합니다.



다른분의 코드를 보니 더 깔끔하게 할 수 있었습니다.

```js
var isSameTree = function(p, q) {
    if(p === null && q === null) return true;
    if(p === null || q === null) return false;
    if(p.val !== q.val) return false;
    return isSameTree(p.right, q.right) && isSameTree(p.left, q.left);
};
```

- 노드가 2개다 null이면 true 1개만 null이면 false로 조건문을 걸어 둡니다.
- 그리고 val가 같지 않으면 false라고 합니다.

이제 재귀를 돌게 됩니다. p, q 둘다 **오른쪽**, **왼쪽**을 확인합니다. 

오른쪽 노드로 갔다가 같은 노드인지 확인하고 , 왼쪽 노드로 갔다가 같은 노드인지 확인합니다.

