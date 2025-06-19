#include <bits/stdc++.h>
using namespace std;

class Solution {
 public:
  long long maximumTripletValue(vector<int>& nums) {
    long long maxValue = 0;
    for (int i = 0; i < nums.size(); i++) {
      for (int j = i + 1; j < nums.size(); j++) {
        for (int k = j + 1; k < nums.size(); k++) {
          long long sum = (long long)(nums[i] - nums[j]) * nums[k];

          if (sum > maxValue) {
            maxValue = sum;
          }
        }
      }
    }
    return maxValue;
  }

  long long maximumTripletValue2(vector<int>& nums) {
    int n = nums.size();
    vector<vector<int>> minMax(n, vector<int>(2, 0));

    long long curr = INT_MIN;
    for (int i = 0; i < n; i++) {
      curr = max(curr, (long long)nums[i]);
      minMax[i][0] = curr;  // Store the maximum value up to index i
    }

    curr = INT_MIN;
    for (int j = n - 1; j >= 0; j--) {
      curr = max(curr, (long long)nums[j]);
      minMax[j][1] = curr;  // Store the maximum value from index j to end
    }

    long long answer = 0;
    for (int i = 1; i < n - 1; i++) {
      answer = max(answer,
                   (minMax[i - 1][0] - (long long)nums[i]) * minMax[i + 1][1]);
    }
    return answer;
  }
};

int main() {
  Solution solution;
  vector<int> nums1 = {12, 6, 1, 2, 7};
  vector<int> nums2 = {1, 10, 3, 4, 19};
  vector<int> nums3 = {1, 2, 3};
  vector<int> nums4 = {1000000, 1, 1000000};

  int result = solution.maximumTripletValue2(nums1);
  cout << "result: " << result << endl;
  return 0;
}
