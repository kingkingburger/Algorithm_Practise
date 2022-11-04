## Maximum Depth of Binary Tree

```js
var maxDepth = function(root) {
    if(!root) return 0;
    return Math.max(maxDepth(root.left), maxDepth(root.right)) +1
};
```

트리의 왼쪽, 오른쪽으로 움직이면 +1을 해주는 형태 입니다. return 을 숫자로 하는것이 중요해보입니다.





## 처음에 생각한 코드

```js
let res = [];
var maxDepth = function(root) {
    if(!root) return 0;
    into(root, 1);
    res.sort()
    return res.pop();
};

var into = (root, result) => {
    res.push(result);
    if(root.left === null && root.right === null) return ;
    if(root.left) into(root.left, result+1);
    if(root.right) into(root.right, result+1);
}
```

처음에 함수 안에다가 result를 넣었는데 **call by reference가 안된다는걸** 알고 배열에다가 값을 집어넣습니다. 모든 트리를 탐색 후 배열을 정렬 후 마지막 값을 찾습니다.

이렇게 해서 정답이 안됐습니다.

```js
var maxDepth = function(root) {
    let res = [];
    if(!root) return 0;
    into(root, 1, res);
    return res.length ? Math.max(...res) : 1;
};

var into = (root, depth, res) => {
    if(root.left === null && root.right === null) return ;
    if(root.left) { into(root.left, depth+1, res); res.push(depth+1);}
    if(root.right) {into(root.right, depth+1, res); res.push(depth+1);};
}
```

어떻게서든 call by reference 형태로 만들었습니다. 비효율적이지만 js 공부하는 느낌으로 만들어 봤습니다.

배열에 값을 집어넣고 Math.max를 하면 됩니다. root에 1개가 들어올 때도 있으니 예외처리를 해줍니다.

결국 함수안에서 외부의 객체를 완전히 바꾸지는 못하는거 같습니다.


