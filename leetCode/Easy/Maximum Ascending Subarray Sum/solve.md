https://leetcode.com/problems/maximum-ascending-subarray-sum/description/?envType=daily-question&envId=2025-02-04

단순히 배열이 있고 이거에 오름차순 일 때의 총합이 가장 큰거를 구하는거에요. 중요한 것은

- 오름차순으로 배열이 있다.

이게 핵심인것 같아요. 기존 배열을 오름차순으로 쪼갤 수 있느냐? 라고 물어보는 것 같아요.


--- 

### 다른사람의 풀이
```
class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int sum = nums[0];
        int temp = nums[0];

        for(int i = 1; i < nums.size(); i++){
            if(nums[i] > nums[i-1]){
                temp += nums[i];
            }
            else{
                temp = nums[i];
            }
            sum = max(temp, sum);
        }
        return sum;
    }
};
```
역시 더 좋은 방법이 있었어요. 

내림차순 더하다가 새로운 내림차순 만나면 그거랑 비교하면 되는거였어요.