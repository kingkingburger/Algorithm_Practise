## Symmetric Tree

```js
var isSymmetric = function(root) {
    return isMirror(root.left, root.right);
};

var isMirror = (rootLeft, rootRight) =>{
    if(rootRight === null && rootLeft === null) return true;
    if(rootRight === null || rootLeft === null) return false;
    if(rootLeft.val !== rootRight.val) return false;

    return isMirror(rootLeft.left,rootRight.right) && isMirror(rootLeft.right, rootRight.left);
 
}
```

다른분의 풀이를 참조했습니다.



트리가 대칭인지 확인하는 문제였습니다.

트리의 왼쪽 오른쪽으로 나눠져서 재귀를 쭉쭉쭉 들어가면 될것입니다. 대칭이니깐 왼쪽은 왼쪽대로 오른쪽은 오른쪽 대로 들어가야 합니다.



멈추는 조건이 중요합니다.

재귀를 걸었으니 트리의 끝까지 갈것입니다. 그러면 중간에 멈춰야할 상황은

- 왼쪽 오른쪽 값이 다른경우
- 왼쪽 오른쪽 중 한쪽이 null인 경우 입니다.



그리고 재귀를 돌리는데 return 문에 쓰고 &&로 조건을 걸어서 트리의 중간을 딱 잘라버리는 것을 배웠습니다.

그리고 조그만한 케이스를 가지고 return을 예상하는게 더 쉬울 거같습니다. 처음에 깊은 트리를 예상하고 하니 더욱 어렵게 느껴집니다. 깊이를 짧게 생각하고 종료조건을 한번 더 생각하는것이 중요한거 같습니다.