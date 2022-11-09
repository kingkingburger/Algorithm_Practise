## Balanced Binary Tree

```js
var isBalanced = function(root) {
    if(!root) return true;
    const result = maxDepth(root);
    return result ? true : false ;
};

var maxDepth = function(root) {
    if(!root) return 0;// ending 조건, null 일 떄 0부터 시작해서 call stack 을 타고 올라가면서 깊이가 쌓인다. 
    
    const le = maxDepth(root.left);
    const ri = maxDepth(root.right);
    if(le === false || ri === false || Math.abs(le - ri) >1) return false;

    //만약 왼쪽과 오른쪽의 균형 차이가 1 이상이라면 
    return Math.max(maxDepth(root.left), maxDepth(root.right)) +1
};
```

트리의 깊이를 알아내는 것 까진 생각했습니다. 하지만 트리의 깊이로 비교하는건 완전 이진트리가 아니더라도 가능했습니다. 그래서 다른 경우를 생각했습니다.

트리의 깊이를 탐색하면서 그 순간 깊이 차이가 1이상이면 균형이 무너진 트리라고 생각할 수 있습니다.

깊이 차이가 1이상일 때 false를 리턴합니다. 그 때 call stack 모두가 false를 리턴하게끔 만들어야 합니다.

그래서 ` if(le === false || ri === false || Math.abs(le - ri) >1)`형태로 if문을 작성했습니다. [왼쪽, 오른쪽, 깊이차이1] 이 3개중에 하나라도 false면은 계속해서 false가 나오게 됩니다. 즉, 처음에 깊이차이1이 나면 계속해서 false가 나옵니다.

만약 `le === false || ri === false` 조건이 없다면 `Math.abs(le - ri) = 0 > 1` 조건에서  만족하지 못해서 false를 반환하지 못합니다.





다른분의 코드를 보니 이해가 더 쉬웠습니다.

```js
var isBalanced = function(root) {
    // If the tree is empty, we can say it’s balanced...
    if (root == null)  return true;
    // Height Function will return -1, when it’s an unbalanced tree...
	if (Height(root) == -1)  return false;
	return true;
}
// Create a function to return the “height” of a current subtree using recursion...
var Height = function(root) {
    // Base case...
	if (root == null)  return 0;
    // Height of left subtree...
	let leftHeight = Height(root.left);
    // Height of height subtree...
	let rightHight = Height(root.right);
    // In case of left subtree or right subtree unbalanced, return -1...
	if (leftHeight == -1 || rightHight == -1)  return -1;
    // If their heights differ by more than ‘1’, return -1...
    if (Math.abs(leftHeight - rightHight) > 1)  return -1;
    // Otherwise, return the height of this subtree as max(leftHeight, rightHight) + 1...
	return Math.max(leftHeight, rightHight) + 1;
};
```

