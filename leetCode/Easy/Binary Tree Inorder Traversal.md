## Binary Tree Inorder Traversal

```js
var inorderTraversal = function(root) {
    let result = []
    
    inorder(result, root);
    
    return result;
};


var inorder = (result, node) => {
    if(!node) return null;
    if(node.left) inorder(result, node.left);
    result.push(node.val);
    if(node.right) inorder(result, node.right);
}
```

처음에 inorderTraversal() 매서드에 함수 로직을 쌓아두고 result를 **전역변수**로 선언했었습니다. 

#### ❎처음에 만들었던 코드

```js
let result = []
var inorderTraversal = function(root) {
    if(root && root.left) inorderTraversal(root.left);
    result.push(root.val);
    if(root && root.right) inorderTraversal(root.right);

    return result;
};
```

그러다 보니 여러개의 답을 제출 할 때 이전의 답이 겹쳐서 제출됬습니다. result를 지역함수로 놓고 로직을 다른 함수로 만들었습니다.



result의 값을 저장하고 result를 초기화하는 과정은 하나의 함수로는 부족합니다. 로직만 다른 함수로 빼는 방법을 생각할 수 있습니다.