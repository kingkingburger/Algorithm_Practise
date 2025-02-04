#include <iostream>
#include <vector>
using namespace std;

class Solution {
 public:
  vector<vector<int>> makeAscendingArray(vector<int>& nums) {
    vector<vector<int>> resultArray;
    if (nums.empty()) return resultArray;

    vector<int> tempArray;
    tempArray.push_back(nums[0]);

    for (size_t i = 1; i < nums.size(); i++) {
      if (nums[i - 1] < nums[i]) {
        tempArray.push_back(nums[i]);
      } else {
        resultArray.push_back(tempArray);
        tempArray.clear();
        tempArray.push_back(nums[i]);
      }
    }

    resultArray.push_back(tempArray);
    return resultArray;
  }

  int maxAscendingSum(vector<int>& nums) {
    vector<vector<int>> targetArray = makeAscendingArray(nums);

    int maxSum = 0;
    for (const auto& subArray : targetArray) {
      int sum = 0;
      for (int num : subArray) {
        sum += num;
      }
      if (maxSum < sum) {
        maxSum = sum;
      }
    }

    return maxSum;
  }
};

int main() {
  Solution sol;
  vector<int> nums1 = {10, 20, 30, 5, 10, 50};
  vector<int> nums2 = {10, 20, 30, 40, 50};
  vector<int> nums3 = {12, 17, 15, 13, 10, 11, 12};
  // int result = sol.maxAscendingSum(nums1);  // 65
  // cout << "result: " << result << endl;
  // int result2 = sol.maxAscendingSum(nums2);  // 150
  // cout << "result2: " << result2 << endl;
  int result3 = sol.maxAscendingSum(nums3);  // 33
  cout << "result3: " << result3 << endl;
  return 0;
}