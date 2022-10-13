## Merge Two Sorted Lists

```js
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

var mergeTwoLists = function (list1, list2) {

    if(!list1) return list2;
    if(!list2) return list1;

    if(list1.val < list2.val){
        list1.next = mergeTwoLists(list1.next, list2);
        return list1;
    }else{
        list2.next = mergeTwoLists(list1, list2.next);
        return list2;
    }
};

let Node3 = new ListNode(4);
let Node2 = new ListNode(2, Node3);
let Node1 = new ListNode(1, Node2);
let Node6 = new ListNode(4,);
let Node5 = new ListNode(3, Node6);
let Node4 = new ListNode(1, Node5);

mergeTwoLists(Node1, Node4);
```

Merge sort의 기본개념은 Divide and conquer입니다.
따라서 Quick sort와 마찬가지로 재귀를 구현할 수 있습니다.



1. 이미 정렬된 두 파티션들이 있다면,
2. 두 파티션의 첫요소를 검사하여 더 작은 요소를 찾습니다.
3. Linked List 와 연결하여서 푸는 문제이기때문에 더 작은 요소를 가지고 있는 **링크드리스트를 헤드**로 삼고, 
4. **헤드로 삼은 링크드리스트의 다음 노드**와, 헤드가 되지못한 링크드리스트 두가지를 다시 함수에 넣습니다.





링크리스트 문제를 풀 때는 재귀를 활용하면 편하구나 라는 깨달음을 얻었습니다. 

---

```js
var mergeTwoLists = function(l1, l2) {
    var mergedHead = { val : -1, next : null },
        crt = mergedHead;
    while(l1 && l2) {
        if(l1.val > l2.val) {
            crt.next = l2;
            l2 = l2.next;
        } else {
            crt.next = l1;
            l1 = l1.next;
        }
        crt = crt.next;
    }
    crt.next = l1 || l2;
    
    return mergedHead.next;
};
```

더 쉬운 솔루션을 발견했습니다. 원래 이런 로직흐름을 생각했었습니다.

헤드의 값을 비교하고 정답 Node에 다 넣는 방식을 생각했습니다.

1. 헤드의 값을 비교하고
2. 정답 노드의 next에 더 작은 링크드리스트를 넣습니다.
3. 그리고 작은 리스트는 1칸 옮깁니다.
4. 그리고 정답 노드도 헤드를 옮겨야합니다.
5. 이 과정을 반복하고 나면 하나의 리스트는 비어있을 것입니다.
6. 마지막에 모두다 넣어줍니다.

그리고 정답 노드를 반환합니다.