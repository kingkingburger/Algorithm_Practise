## TwoSum

```java
    public static int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int sumResult = target - nums[i];

            if(map.containsKey(sumResult)){
                return new int[]{map.get(sumResult),i};
            }
            else{
                map.put(nums[i],i);
            }
        }
        return nums;
    }
```

처음에는 2중 for문으로 돌렸습니다.

leetcode는 끝나고 내 시간복잡도가 상위 몇 인지를 알려주더군요.

그래서 더 좋은 로직이 있겠다 싶어서 다른 코드를 찾아봤습니다.

**Map형태로 DP를 진행**하는거였습니다.



key는 배열을 돌면서 현재 값, value는 인덱스를 map에 넣습니다.

그리고 target - 현재값 으로 for문을 돌면서 map에 key가 있는지 없는지를 살펴보았습니다.

이러니 시간 복잡도가 확 줄더군요



그리고 

```java
1. if(map.get(sumResult) != null
2. if(map.containsKey(sumREsult))
```

처음에 1번을 사용했는지 시간복잡도가 상위 50%였습니다.

다른 분의 코드를 보고 2번으로 바꿨더니 70%정보다 나왔습니다.

get()을이용하면 처음부터 끝까지 Key가 있는지 찾아봐서 더 느려진거 같습니다.