#include <bits/stdc++.h>

#include <vector>
using namespace std;

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

int main() {
  Solution sol;
  vector<string> input1 = {"--X", "X++", "X++"};
  int result = sol.finalValueAfterOperations(input1);  // 1
  cout << result << endl;
}