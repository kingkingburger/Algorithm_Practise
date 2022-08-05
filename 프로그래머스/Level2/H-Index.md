## H-Index

```java
    static int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);

        for (int j = 0; j < citations.length; j++) {
            int citation = citations[j];
            int i = citations.length - j; // 앞에 남아있는 수
            if (citation >= i) {
                answer = Math.max(answer, i);
            }
        }

        System.out.println("answer = " + answer);
        return answer;
    }
```

제가 해본 테스트 케이스들 입니다.

```java
        solution(new int[]{3, 0, 6, 1, 5});   // 3
        solution(new int[]{5, 4, 3, 8, 10});  // 4
        solution(new int[]{5, 3, 3, 8, 10});  // 3
        solution(new int[]{100, 100, 100});   // 2
        solution(new int[]{0, 1, 100, 101});  // 2
        solution(new int[]{0, 101, 101, 101});// 3
```

#### 풀이방법

먼저 배열을 sort()시켜서 오름차순으로 만듭니다.

h-index란 **인덱스의 값**이 앞에 **남아있는 수(나보다 큰 수)**보다 크거나 작은 위치에서 인덱스를 의미합니다. 

여기 부분이 이해하기 여려웠습니다.

'그러면 h-index는 h회 이상 인용된 논문의 개수 일껀데 그러면 **citation**을 넣으면 되지 않을까?' 라고 생각했습니다.

**citations**배열는 인용된 논문의 개수를 구해놓은 것입니다. h-index는 `h를 기준으로 h회 인용된 논문의 개수`에서 h를 구하는 것입니다.



#### {0,1,4,5,6}으로 예시를 들어보겠습니다

| 해당 논문 인용 횟수 = citations[i] | 해당 논문보다 인용횟수가 크거나 같은 논문 편수 = h | h회 이상 인용된 논문 편수가 h편 이상이다. (true/false)       |
| ---------------------------------- | -------------------------------------------------- | ------------------------------------------------------------ |
| 0                                  | 5                                                  | 5회 이상 인용된 논문 편수가 5편 이상이다. => false           |
| 1                                  | 4                                                  | 4회 이상 인용된 논문 편수가 4편 이상이다. => false           |
| 4                                  | 3                                                  | 3회 이상 인용된 논문 편수가 3편 이상이다. => true<br />4회 이상 인용된 논문 편수가 3편 이상도 true입니다. 하지만 'h회 이상 인용된 논문 편수가 h편 이상'이기 때문에 h의 값이 기준이 됩니다. |
| 5                                  | 2                                                  | 2회 이상 인용된 논문 편수가 2편 이상이다. => true            |
| 6                                  | 1                                                  | 1회 이상 인용된 논문 편수가 1편 이상이다. => true            |

그러면 4,5,6이 h-index의 후보가 됩니다. 이 때 h값은 3,2,1이 됩니다. 우리는 h값을 구하는 것입니다. citations[i]의 값을 구하는 것이 아닙니다.



#### 참고

https://bada744.tistory.com/94#2.-%EC%9D%B8%EC%9A%A9%ED%9A%9F%EC%88%98-%EB%B0%B0%EC%97%B4-%EC%9A%94%EC%86%8C-%EA%B0%92%EC%9D%84-%EC%B0%A8%EB%A1%80%EB%A1%9C-h%EB%A1%9C-%EC%A7%80%EC%A0%95%ED%95%98%EB%A9%B0-h-index-%EC%A1%B0%EA%B1%B4-%EC%97%AC%EB%B6%80-%ED%8C%8C%EC%95%85