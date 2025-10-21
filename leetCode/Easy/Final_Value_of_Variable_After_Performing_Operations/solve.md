### 문자열에 '+', '-' 확인

문자열에 + 들어가있다면 + 연산, - 들어가있다면 - 연산 되게만들었어요.


```
class Solution {
 public:
  bool checkCalculate(string str) {
    if (str.find("+") != string::npos) {
      return true;
    }
    return false;
  }

 public:
  int finalValueAfterOperations(vector<string>& operations) {
    int answer = 0;
    for (string str : operations) {
      if (checkCalculate(str)) {
        answer++;
      } else {
        answer--;
      }
    }
    return answer;
  }
};
```

다른 사람의 풀이를 보니 더 하드코딩하는 식으로 만들어놨네요.
```
class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int x = 0;
        for (auto& op : operations) {
            if (op == "X++" || op == "++X") {
                x++;
            } else {
                x--;
            }
        }
        return x;
```
어처피 X++, ++X 두개중 하나만 들어오니깐 이런 로직이 가능하는 것 같아요