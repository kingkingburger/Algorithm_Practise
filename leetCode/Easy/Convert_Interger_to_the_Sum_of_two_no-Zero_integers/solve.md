### 숫자에 0이 들어가있는지 확인

0이 들어가있는지 확인하는 방법은 1의 자리 숫자부터 검사하는거에요.
10으로 mod 한 결과가 0이라면 0을 포함한 숫자가 있는거죠.


```
class Solution {
public:
  bool getZero(int number) {
    while (number > 0) {
      if (number % 10 == 0) return true;
      number = number / 10;
    }
    return false;
  }
  vector<int> getNoZeroIntegers(int n) {
    for (int i = 2; i < n; i++) {
      int target = n - i;
      if (!getZero(target) && !getZero(i)) {
        return {i, target};
      }
    }
    return {1, 1};
  }
};
```

다른 사람의 풀이를 보면 for문 1번에 key를 찾고 그 키에 안에서 