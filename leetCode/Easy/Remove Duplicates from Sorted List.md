## Remove Duplicates from Sorted List

```js
var deleteDuplicates = function(head) {
    let removeHead = { val : -1, next : null },
        crt = removeHead;
    
    while(head){
        let num = head.val;
        let nextNode = head.next;

        if(head.next && (num === nextNode.val)){
            head = head.next;
            continue;
        }
        
        crt.next = head;
        crt = crt.next;
        head = head.next;
    }

    return removeHead.next;
};
```

중복된 링크드 리스트 지우는 문제였습니다.



처음에 더미데이터를 생성하고 또 다른 변수를 선언해서 그 더미 데이터를 가리키게 합니다.

변수 포인터는 다음 값을 입력받는 포인터이고 더미데이터 다음부터 데이터가 쌓이게 됩니다.



같은 수가 있을 때는 head 포인터를 next로 옮긴다음에 다음 수를 찾습니다.



다른분의 코드를 봤습니다.

```js
var deleteDuplicates = function(head) {
  let current = head;
  
  while (current) {
    if (current.next && current.val === current.next.val) {
      current.next = current.next.next;
    } else {
      current = current.next;
    }
  }
  
  return head;
};
```

현재 next값이 다음꺼랑 같으면 다다음 노드로 포인터를 옮깁니다.



----

포인터에 대한 계념을 다시 복습하니 좋았습니다.