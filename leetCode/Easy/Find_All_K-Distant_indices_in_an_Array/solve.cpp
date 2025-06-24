#include <bits/stdc++.h>

#include <vector>
using namespace std;

class Solution {
 public:
  vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
    vector<int> keys;
    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] == key) {
        keys.push_back(i);
      }
    }

    vector<int> result;
    for (int j = 0; j < nums.size(); j++) {
      for (auto key : keys) {
        if (abs(j - key) <= k) {
          result.push_back(j);
          break;
        }
      }
    }

    sort(result.begin(), result.end());

    return result;
  }
};

int main() {
  Solution sol;
  vector<int> nums3 = {3, 4, 9, 1, 3, 9, 5};
  vector<int> nums1 = {2, 2, 2, 2, 2};
  //   auto result = sol.findKDistantIndices(nums3, 9, 1);
  auto result = sol.findKDistantIndices(nums1, 2, 2);
  cout << "result: ";
  for (int i : result) {
    cout << i << " ";
  }
  return 0;
}