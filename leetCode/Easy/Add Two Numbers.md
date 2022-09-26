## Add Two Numbers

```java
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode node = new ListNode(0);
        ListNode answer = node;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int x = (l1 == null) ? 0 : l1.val; 
            int y = (l2 == null) ? 0 : l2.val;
            int num = x + y + carry;
            carry = num / 10;
            node.next = new ListNode(num % 10);
            node = node.next;
            if(l1 != null) l1 = l1.next;
            if(l2 != null) l2 = l2.next;
        }
        if(carry == 1){
            answer.next = new ListNode(carry);
        }
        
        return answer.next;
    }
}
```

leetCode에 ListNode가 어떤것인지 알려줍니다.



처음에 생각했던 로직을 구사했는데 반대로 하는게 어려워서 다른사람의 코드를 봤습니다.

l1, l2가 null일 때 를 처리해야하고 carry가 나오는 것을 처리해야 합니다.



carry가 있는데 남아 있는 수가 있다면 +1를 하고 수가 끝났다면 1를 앞에다가 붙여줄 것입니다.

10으로 나눈 나머지로 자리 수를 채워줍니다.