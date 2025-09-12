#include <bits/stdc++.h>
using namespace std;

class Solution {
 public:
  bool checkVowel(string s) {
    int find = 0;
    for (char ch : s) {
      if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
        find++;
      }
    }
    return find > 0;
  }

  bool doesAliceWin(string s) {
    bool isVowel = checkVowel(s);

    if (!isVowel) {
      return false;
    }

    return true;
  }
};

int main() {
  Solution solution;

  int result = solution.doesAliceWin("leetcoder");  // 38
  cout << "result" << result << endl;
  return 0;
}
