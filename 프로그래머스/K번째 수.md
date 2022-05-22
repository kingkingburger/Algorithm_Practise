## K번째 수

```java
import java.util.*;

class Solution {
    public List<Integer> solution(int[] array, int[][] commands) {
        List<Integer> answer = new ArrayList<>();

        for (int q = 0; q < commands.length; q++) {
            List<Integer> list = new ArrayList<>();

            int i = commands[q][0];
            int j = commands[q][1];
            int k = commands[q][2];

            for (int l = i-1; l <= j-1; l++) {
                list.add(array[l]);
            }
            Collections.sort(list);
            answer.add(list.get(k - 1));
        }
        return answer;
    }
}
```

array들 안에 들어있는 요소들을 for문에서 하나씩 빼옵니다. 그걸 i, j, k라고 정해둡니다.

그리고 list에 i-1 ~ j-1 까지 돕니다. 인덱스는 0부터 시작하기 때문입니다.

그다음 Collections.sort()로 list를 sort해줍니다.

그리고 k의 인덱스에 따라 answer 리스트에 값을 넣어서 반환합니다.



다른사람의 풀이를 보니

```java
import java.util.Arrays;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for(int i=0; i<commands.length; i++){
            int[] temp = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
            Arrays.sort(temp);
            answer[i] = temp[commands[i][2]-1];
        }

        return answer;
    }
}
```

이런식으로도 풀수 있었습니다.

Arrays에 copyofRange로 Range를 설정해주는 메서드가 있었습니다.