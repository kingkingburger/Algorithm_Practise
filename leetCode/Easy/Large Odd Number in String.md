# Large Odd Number in String

```py
import sys

sys.set_int_max_str_digits(100000)


class Solution:
    def largestOddNumber(self, num: str) -> str:

        # for i in range(len(num), 0, -1):
        #     converted_num = int(num)
        #
        #     if converted_num % 2 != 0:
        #         return str(converted_num)
        #
        #     target_index = i - 1
        #     target = int(num[target_index])
        #
        #     if target % 2 == 0:
        #         num = num[:target_index] + num[target_index + 1:]

        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ''

```

#### 🟩 내 생각

제가 처음에 생각한 로직이 주석된 부분 입니다.

string이 홀수인지 검사합니다.

문자열의 오른쪽 부터 1개씩 지우는데요. 이 때 짝수만 지우면 된다고 생각했습니다. 이렇게 해서 O(n)이 되었다고 생각했습니다.

문자열의 길이가 10^5라 python의 max_str_digits를 조정해주어야 했습니다.

마지막에 10^5의 문자열을 넣었을 때 시간초과가 나왔습니다. 그래서 gpt한태 물어보았더니 더 효율적이 코드가 나왔습니다.



#### 결론

`1의 자리수가 홀수면 홀수다` 라는 계념을 인지했어야 했습니다.

문자열을 오른쪽부터 왼쪽으로 돌면서 홀수인지 판별하고 아니면 한칸식 자르는 형식이 좋은거 같스빈다.

그것도 python의 문자열 자르기(슬라이싱) 하는 문법도 다시 리마인드 했습니다.

