### 2진수를 10진수로 변환해서 처리하기

문자열을 2진수로 바꾸고 또 10진수로 바꾸었어요.

```
#include <bits/stdc++.h>

using namespace std;

class Solution {
 public:
  int convertTo10(string& str) {
    int base10 = 0;
    int num = stoi(str);

    int size = 0;
    while (num != 0) {
      // 1의자리 구하기
      int main = num % 10;

      // 10진법 변환
      if (main == 1) {
        base10 += pow(2, size);
      }

      // 1의자리수 제외 한 값
      num /= 10;

      // 2진수 증가
      size += 1;
    }
    return base10;
  }

 public:
  vector<bool> prefixesDivBy5(vector<int>& nums) {
    vector<bool> answer;
    string mainString = "";
    for (int num : nums) {
      mainString += to_string(num);
      int target = convertTo10(mainString);

      if (target % 5 == 0) {
        answer.push_back(true);
      } else {
        answer.push_back(false);
      }
    }

    return answer;
  }
};

int main() {
  Solution sol;
  // vector<int> input1 = {0, 1, 1};
  // sol.prefixesDivBy5(input1);
  vector<int> input1 = {0, 1, 1, 1, 1, 1};  // [1,0,0,0,1,0]
  sol.prefixesDivBy5(input1);
}
```
이렇게 하면 stoi(num)에서 out of range가 걸려요. 

```
class Solution {
 public:
  long long convertTo10(string& str) {
    long long base10 = 0;

    for (char c : str) {
      base10 = (base10 * 2) % 5;  // 왼쪽으로 미룸
      if (c == '1') {
        base10 += 1;
      }
    }
    return base10;
  }

 public:
  vector<bool> prefixesDivBy5(vector<int>& nums) {
    vector<bool> answer;
    string mainString = "";
    for (int num : nums) {
      mainString += to_string(num);
      long long target = convertTo10(mainString);

      if (target % 5 == 0) {
        answer.push_back(true);
      } else {
        answer.push_back(false);
      }
    }

    return answer;
  }
};
```

long long 타입으로 해도 타임 에러가 나더라고요. gemini의 도움을 받아 처리했어요ㅕ.
10진수를 구하는 방법이 특이한데요. 호너의 방법이라고 불리는 방법이레요. 10진수 읽는 법과 비교해볼게요.


숫자 123을 한 글자씩 읽어볼게요 

1. 처음 1을 읽습니다
2. 다음 2가 들어옵니다
  - 기존의 1은 '십의 자리'가 되어야 합니다. 그래서 10을 곱해줍니다.
  - 그리고 새 숫자 2를 더합니다.
  - 1 x 10 + 2 = 12(현재 값: 12)
3. 다음에 3이 들어옵니다.
  - 기존에 있던 12는 이제 '백의 자리, 십의 자리'로 밀려나야 합니다. 그래서 전체에 10을 곱해줍니다.
  - 그리고 새 숫자 3을 더합니다.
  - 12 x 10 + 3 = 123(현재 값: 123)

이와 같은 방법으로 처리하면 2진수도 똑같이 할 수 있어요. 

숫자 110을 이진수로 한 글자씩 읽어볼게요 

1. 처음 1을 읽습니다
2. 다음 1이 들어옵니다
  - 기존의 1은 '십의 자리'가 되어야 합니다. 그래서 2을 곱해줍니다.
  - 그리고 새 숫자 1를 더합니다.
  - 1 x 2 + 1 = 3(현재 값: 3)
3. 다음에 0이 들어옵니다.
  - 기존에 있던 11는 이제 '백의 자리, 십의 자리'로 밀려나야 합니다. 그래서 전체에 2을 곱해줍니다.
  - 그리고 새 숫자 0을 더합니다.
  - 3 x 2 + 0 = 6(현재 값: 6)

이런식으로 2진수를 10진수로 변환할 수 있습니다.