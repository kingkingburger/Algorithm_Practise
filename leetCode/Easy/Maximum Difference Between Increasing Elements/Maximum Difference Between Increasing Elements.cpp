#include <bits/stdc++.h>
using namespace std;

class Solution {
 public:
  int maximumDifference(vector<int>& nums) {
    int result = -1;
    for (int i = 0; i < nums.size() - 1; i++) {
      int diff = 0;
      for (int j = i + 1; j < nums.size(); j++) {
        diff = nums.at(j) - nums.at(i);
        if (diff > 0 && diff > result && (i < j)) {
          result = diff;
        }
      }
    }
    return result;
  }
  int maximumDiffrence2(vector<int>& nums) {
    int n = nums.size();
    int maxi = -1;
    for (int i = 0; i < n - 1; i++) {
      int diff = 0;
      for (int j = i + 1; j < n; j++) {
        if (nums[i] < nums[j]) {
          diff = nums[j] - nums[i];
          maxi = max(maxi, diff);
        }
      }
    }
    return maxi;
  }
  int maximumDifference3(vector<int>& nums) {
    int min_so_far = nums[0];
    int max_diff = -1;

    for (int i = 1; i < nums.size(); i++) {
      if (nums[i] > min_so_far) {
        max_diff = max(max_diff, nums[i] - min_so_far);
      }
      min_so_far = min(min_so_far, nums[i]);
    }

    return max_diff;
  }
};

int main() {
  Solution solution;
  vector<int> nums1 = {7, 1, 5, 4};
  vector<int> nums2 = {9, 4, 3, 2};
  vector<int> nums3 = {1, 5, 2, 10};
  vector<int> nums4 = {
      999, 997, 980, 976, 948, 940, 938, 928, 924, 917, 907, 907, 881, 878, 864,
      862, 859, 857, 848, 840, 824, 824, 824, 805, 802, 798, 788, 777, 775, 766,
      755, 748, 735, 732, 727, 705, 700, 697, 693, 679, 676, 644, 634, 624, 599,
      596, 588, 583, 562, 558, 553, 539, 537, 536, 509, 491, 485, 483, 454, 449,
      438, 425, 403, 368, 345, 327, 287, 285, 270, 263, 255, 248, 235, 234, 224,
      221, 201, 189, 187, 183, 179, 168, 155, 153, 150, 144, 107, 102, 102, 87,
      80,  57,  55,  49,  48,  45,  26,  26,  23,  15};
  int result = solution.maximumDifference(nums4);
  cout << "Difference of sums: " << result << endl;
  return 0;
}
