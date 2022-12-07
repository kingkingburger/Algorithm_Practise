## ✅ Linked List Cycle

```js
var hasCycle = function(head) {
    let array = [];
    while(head){
        const inArray = array.indexOf(head.val);
        
       if(inArray > -1){
        return true;
       }
        const random = Math.random();
       array.push(head.val + random);
       head.val = head.val + random
       head = head.next;
    } 
    return false;
};
```

처음에 만든 코드입니다.

노드들을 지나가면서 배열에 값을 넣어둡니다. 배열에 같은 값이 있다면 사이클이 있다고 판단하고 **true**를 반환합니다.

array에다가 랜덤한 값을 넣어주지 않으면 노드들 가운데 같은 노드가 **true**로 반환됩니다.
ex) 5, 12 ,6 , 12, 8 면 12의 다음값이 8인데도 이전에 12값이 들어있기 때문에 **true**가 됩니다.

이러한 문제를 해결하려고 random한 값을 넣어서 고유한 값으로 만들어줬습니다. array에는 고유한 값만 있기때문에 같은 값이더라도 이전의 값이랑 다른 값을 가지게 됩니다.



#### ✅ 다른사람의 코드

```js
var hasCycle = (head) => {
    if (!head) return false;

    while (head) {
        if (head.val === 'checked') return true
        head.val = 'checked'
        head = head.next
    }
    return false
}
```

정말 간단하고 알기 쉽게쓰였습니다.

한번 지나가면 node의 값을 **checked**로 만들고 다음으로 넘어갑니다. 만약 다음에 값이 **checked**면 Cycle이 있다는 뜻이니깐 true를 반환합니다.