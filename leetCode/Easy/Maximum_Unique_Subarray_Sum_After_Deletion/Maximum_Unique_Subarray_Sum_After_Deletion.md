```
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

```

- 배열의 중복을 제거하고 오름차순으로 정렬해요.
- 음수랑 0이 섞여있는 배열은 가장 오른쪽 값이 최대 값이에요.
- 나머지는 0보다 큰 값들의 합을 더해줘요.

leetCode에 있는 다른 답이에요.
```
class Solution {
public:
    int maxSum(vector<int>& nums) {
        unordered_map<int, int> freq;
        sort(nums.begin(), nums.end(), greater<int> ());
        if (nums[0] < 0) return nums[0];
        for (int num : nums) {
            freq[num]++;
        }
        int sum = 0;
        for (const auto &pair : freq) {
            if (pair.first >= 0) sum += pair.first;
        }
        return sum;

    }
};
```
더 깔끔한것 같아요. 내림차순으로 정렬하는 것과, key, value 형태로 값을 처리해요.