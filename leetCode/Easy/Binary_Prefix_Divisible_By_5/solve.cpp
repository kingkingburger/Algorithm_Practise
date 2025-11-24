#include <bits/stdc++.h>

using namespace std;

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

int main() {
  Solution sol;
  // vector<int> input1 = {0, 1, 1};
  // sol.prefixesDivBy5(input1);
  // vector<int> input1 = {0, 1, 1, 1, 1, 1};  // [1,0,0,0,1,0]
  // sol.prefixesDivBy5(input1);
  vector<int> input1 = {1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0,
                        0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0,
                        1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1,
                        0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0};
  sol.prefixesDivBy5(input1);
}