[2873. Maximum Value of an Ordered Triplet I](https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/)

https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/description/?envType=daily-question&envId=2025-04-02

 `(nums[i] - nums[j]) * nums[k]` 이 식을 만족하는 조합중 가장 큰 값을 찾는 거에요. 저는 3중 for문을 이용했어요.

- 코드
    
    ```cpp
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
    };
    
    int main() {
      Solution solution;
      vector<int> nums1 = {12, 6, 1, 2, 7};
      vector<int> nums2 = {1, 10, 3, 4, 19};
      vector<int> nums3 = {1, 2, 3};
      vector<int> nums4 = {1000000, 1, 1000000};
    
      int result = solution.maximumTripletValue(nums4);
      cout << "result: " << result << endl;
      return 0;
    }
    
    ```
    

다른 사람을 보니 max 값을 가지고 하는 방법도 있는 것 같아요.

- 코드
    
    ```cpp
    class Solution {
    public:
        long long maximumTripletValue(vector<int>& nums) {
            int n = nums.size();
            vector<vector<int>> minMax(n, vector<int>(2, 0));
            long long curr = INT_MIN;
            for(int i = 0; i<n; i++){
                curr = max(curr, (long long)nums[i]);
                minMax[i][0] = curr;
            }
            curr = INT_MIN;
            for(int i = n-1; i>=0; i--){
                curr = max(curr, (long long)nums[i]);
                minMax[i][1] = curr;
            }
            long long ans = 0;
            for(int i = 1; i<n-1; i++){
                ans = max(ans, (minMax[i-1][0]-(long long)nums[i])*minMax[i+1][1]);
            }
            return ans;
        }
    };
    ```
    

왼쪽에서 가장 큰값, 오른쪽에서 가장 큰값 구한다음 for문 돌려서 가장 큰 값을 찾는거에요. 없다면 0이 나와요. 

minMax vector에 각 index마다 최소, 최대를 저장해요. 그리고 전체 for문을 돌면서 i < j < k에 맞게 이전 값과 이후 값의 최소, 최대를 가져와요.