#include <bits/stdc++.h>
using namespace std;

class Solution {
 public:
  bool isAllUnderZero(const vector<int>& nums) {
    for (int n : nums) {
      if (n >= 0) return false;
    }
    return true;
  }

  int maxSum(vector<int>& nums) {
    int answer = 0;

    sort(nums.begin(), nums.end());
    auto unique_end = unique(nums.begin(), nums.end());
    nums.erase(unique_end, nums.end());

    if (isAllUnderZero(nums) && !nums.empty()) {
      int result = nums.back();
      return result;
    }

    for (int n : nums) {
      if (n <= 0) continue;
      answer += n;
    }
    return answer;
  }
};

int main() {
  Solution solution;
  vector<int> nums1 = {1, 2, 3, 4, 5};           // 15
  vector<int> nums2 = {1, 1, 0, 1, 1};           // 1
  vector<int> nums3 = {1, 2, -1, -2, 1, 0, -1};  // 3 {-2, -1, 0, 1, 2}
  vector<int> nums4 = {-100, -99};               // -199
  vector<int> nums5 = {-17, -15};                // -15
  vector<int> nums6 = {-17, -15, 0};             // 0

  int result = solution.maxSum(nums6);
  cout << "result: " << result << endl;
  return 0;
}
