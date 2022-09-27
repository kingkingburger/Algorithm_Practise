Palindrome Number

```java
    public boolean isPalindrome(int x) {
        String[] split = String.valueOf(x).split("");
        for (int i = 0; i < split.length; i++) {
            int last = split.length - 1;
            if(split[i].equals(split[last - i])){
                continue;
            }else{
                return false;
            }
        }
        return true;
    }
```

이렇게 string[]로 만들어서 첫 번째와 마지막을 차례대로 비교합니다. 중간에 다른 값이 있다면 false를 리턴했습니다.

거꾸로 읽어도 제대로 읽는 것과 같은 문장을 어떻게 찾아야 하나..

```java
    public boolean isPalindrome(int x) {
        if(x < 0){
            return false;
        }
        
        int reverse = 0;
        int temp = x;
        
        while(temp != 0){
            reverse = reverse * 10 + temp % 10;
            temp /= 10;
        }
        
        return reverse == x;
        
    }
```

다른분의 로직을 참고 했습니다. 무조건 int형 안에서 끝낼 수 있을거 같았습니다.

int형을 뒤집는 방법이 있었습니다.

원본의 복사(temp)를 가지고 reverse된 객체를 만듭니다.

reverse 객체는 이전의 reverse 값의 x10을 합니다. 그리고 temp를 1자리씩 가져옵니다.

그러면 reverse는 x10로 1자리씩 왼쪽으로 갑니다. 그리고 오른쪽에서는 x의 1의 자리수가 들어옵니다.

그러면 원래값(x)를 1의 자리씩 왼쪽으로 땡기는 것입니다.

