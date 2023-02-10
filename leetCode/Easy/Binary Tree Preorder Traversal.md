## Binary Tree Preorder Traversal

#### 🟩 code

```js
function preOrder (node,result) {
    if(!node) return;
    result.push(node.val);
    preOrder(node.left, result);
    preOrder(node.right, result);
}
var preorderTraversal = function(root) {
    let result = [];
    preOrder(root,result);
    return result;
};
```

preOrder라는 함수는 재귀함수입니다.

트리를 순회하면서 트리의 왼쪽 끝까지 갔다가 오른쪽을 살피면서 root로 올라옵니다.

![img](https://leetcode.com/problems/binary-tree-preorder-traversal/solutions/2918429/Figures/144_rewrite/144-re.png)

재귀에 대한 멋진설명입니다. 1칸 아래로 들어가면 그 칸의 시점으로 함수를 처다보면 편합니다.

![img](https://leetcode.com/problems/binary-tree-preorder-traversal/solutions/2918429/Figures/144_rewrite/144-pre.png)



#### Algorithm

1.  `answer`배열을 초기화합니다..
2. ​    `root` 가 null 이아니면 `root`노드부터 시작합니다.:
   - 만난 node의 값을 answer 배열에 저장합니다.`answer`.
   -  `root`의 왼쪽 노드로가 2단계를 반복합니다.
   -  `root`의 오른쪽쪽 노드로가 2단계를 반복합니다.
3. 재귀가 끝나면 `answer` 배열을 반환합니다.