### 조건에 맞는 식을 찾아서 처리하기

문자열을 vector에 저장하두고 vector와 앞에 있는것을 비교해가면서 애나그램인지 확인해요.
애나그램인지 확인하는 방법은 문자열을 sort 하고 똑같은지 비교하면 되요.

```
class Solution {
 public:
  bool compareWord(string s1, string s2) {
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());
    return s1 == s2;
  };

 public:
  vector<string> removeAnagrams(vector<string>& word) {
    vector<string> answer;
    answer.push_back(word[0]);
    for (int i = 1; i < word.size(); i++) {
      if (!compareWord(answer.back(), word[i])) {
        answer.push_back(word[i]);
      }
    }
    return answer;
  }
};
```
