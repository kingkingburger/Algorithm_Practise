### 조건에 맞는 식을 찾아서 처리하기

for문 1번으로 `key` 값을 찾은 후 
문제 에서 준 공식 `|i - j| <= k` 으로 조건에 만족하는 배열을 찾은 후 마지막에 오름차순으로 `sort` 처리를 해요
=> sort 처리를 필요 없어요. j에서 값을 담을 때 0부터 차례대로 담기 때문이에요.

```
class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        vector<int> ans;
        int n = nums.size();

        int start = 0;
        for(int i=0;i<n;i++){
            if (nums[i] == key){
                int left = max(0,i-k);
                int right = min(n-1,i+k);

                while(start<=right){
                    if (start>=left) ans.push_back(start);
                    start++;
                }
            }
        }


        return ans;
    }
};
```

다른 사람의 풀이를 보면 for문 1번에 key를 찾고 그 키에 안에서 