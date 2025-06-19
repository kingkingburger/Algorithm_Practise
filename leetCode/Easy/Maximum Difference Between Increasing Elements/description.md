내가 만든건 2중 for문으로 하나하나 비교해서 가장 큰값과 가장 작은값을 처리하는 거였어요. 그리고 i,j의 위치도 `j - i` 인 경우에만 처리를 하게 했었어요.

- 코드
    
    ```cpp
    class Solution {
     public:
      int maximumDifference(vector<int>& nums) {
        int result = -1;
        for (int i = 0; i < nums.size() - 1; i++) {
          int diff = -1;
          for (int j = i + 1; j < nums.size(); j++) {
            diff = nums.at(j) - nums.at(i);
            if (diff > 0 && diff > result && (i < j)) {
              result = diff;
            }
          }
        }
        return result;
      }
    };
    ```
    

만약 0이 나온다면 최대값이 아니니 -1로 반환하면 되요.

더 좋은 방법이 있는지 다른 사람 코드를 보고 확인해보려고요.

- 2ms 걸리는 코드
    
    ```cpp
    class Solution {
    public:
        int maximumDifference(vector<int>& nums) {
            int n = nums.size();
            int maxi = -1;
            for(int i=0;i<n-1;i++){
                int diff = 0;
                for(int j=i+1;j<n;j++){
                    if(nums[i] < nums[j]){
                        diff = nums[j] - nums[i];
                        maxi = max(maxi,diff);
                    }
                }
            }
            return maxi;
        }
    };
    ```
    

제가 만든 거랑 비슷한거 같은데요. vector를 [] 이 형태로 접근할 수 있는거를 몰랐네요. 그리고 max 함수도 있나봐요.

- 0ms 걸리는 코드
    
    ```cpp
    class Solution {
    public:
        int maximumDifference(vector<int>& nums) {
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
    ```
    

for문을 1번만 돌아요. min으로 nums를 돌면서 최소값을 찾는다? 아, 움직이는건 nums[i]이고 최소값만 찾는거구나. 

---

여기서 c++에서 max랑 min 쓰는 법을 알았어요. int 값을 2개 넣으면 되요.