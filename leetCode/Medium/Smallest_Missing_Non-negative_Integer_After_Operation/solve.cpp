#include <bits/stdc++.h>

using namespace std;

class Solution {
 public:
  int findSmallestInteger(vector<int>& nums, int value) {
    vector<int> remainderCount(value, 0);

    for (int num : nums) {
      int remainder = ((num % value) + value) % value;
      remainderCount[remainder]++;
    }

    int mex = 0;
    while (true) {
      int requiredRemainder = mex % value;

      if (remainderCount[requiredRemainder] > 0) {
        remainderCount[requiredRemainder]--;
        mex++;
      } else {
        break;
      }
    }
    return mex;
  }
};

int main() {
  Solution sol;

  // vector<int> input1 = {1, -10, 7, 13, 6, 8};
  // int result = sol.findSmallestInteger(input1, 7);  // 2
  // int result = sol.findSmallestInteger(input1, 5);  // 4

  // vector<int> input2 = {1, 3, 5, 7};
  // int result2 = sol.findSmallestInteger(input2, 2);  // 0

  vector<int> input3 = {3, 0, 3, 2, 4, 2, 1, 1, 0, 4};
  int result3 = sol.findSmallestInteger(input3, 5);  // 10
  cout << result3;
}