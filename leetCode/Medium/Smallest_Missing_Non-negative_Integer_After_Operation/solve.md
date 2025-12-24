### 해당 숫자를 만들 수 있는 나누기가 몇 개 있는지
```

class Solution {
 public:
  int findSmallestInteger(vector<int>& nums, int value) {
    vector<int> remainderCount(value, 0);

    for (int num : nums) {
      int remainder = ((num % value) + value) % value;
      remainderCount[remainder]++;
    }

    int mex = 0;
    while (true) {
      int requiredRemainder = mex % value;

      if (remainderCount[requiredRemainder] > 0) {
        remainderCount[requiredRemainder]--;
        mex++;
      } else {
        break;
      }
    }
    return mex;
  }
};
```

참고를 보고 풀었어요. 문제의 진짜의도는 0부터 시작해서 1씩 증가하는 숫자들을 만들 수 있는지 순서대로 확인하고, 처음으로 만들 수 없는 가장 작은 수를 찾는거에요.

((nums[i] % v) + v) % v 는 음수 나머지를 양수로 바꿔주는 안전한 방법입니다.
예: -10 % 7 = -3  ->  (-3 + 7) % 7 = 4


0부터 시작하여 만들 수 없는 가장 작은 숫자를 찾습니다.
  int mex = 0; // MEX: Minimum Excluded value (만들 수 없는 최소값)
  
  while (true) {
      // 현재 확인하려는 숫자(mex)를 만들기 위해 필요한 나머지
      int requiredRemainder = mex % value;

      // 해당 나머지를 가진 숫자가 우리에게 남아있는지(재고가 있는지) 확인합니다.
      if (remainderCounts[requiredRemainder] > 0) {
          // 재고가 있다면, 하나를 사용합니다.
          remainderCounts[requiredRemainder]--;
          // 그리고 다음 숫자를 만들 수 있는지 확인하기 위해 mex를 1 증가시킵니다.
          mex++;
      } else {
          // 재고가 없다면, 현재 mex는 만들 수 없습니다.
          // 이것이 우리가 찾던 답이므로 루프를 탈출합니다.
          break;
      }
  }

  return mex;


ex)
0부터 순서대로 만들 수 있는지 확인하기

이제 0부터 시작해서 각 숫자를 만들 수 있는지 확인해 봅시다.

    0을 만들 수 있는가?

        0 % 5 = 0 입니다.

        '나머지 0' 재고가 2개 있습니다. 충분합니다. (성공)

        '나머지 0' 재고 1개 사용 (남은 재고: 1개)

    1을 만들 수 있는가?

        1 % 5 = 1 입니다.

        '나머지 1' 재고가 2개 있습니다. (성공)

        '나머지 1' 재고 1개 사용 (남은 재고: 1개)

    2를 만들 수 있는가?

        2 % 5 = 2 입니다.

        '나머지 2' 재고가 2개 있습니다. (성공)

        '나머지 2' 재고 1개 사용 (남은 재고: 1개)

    3을 만들 수 있는가?

        3 % 5 = 3 입니다.

        '나머지 3' 재고가 2개 있습니다. (성공)

        '나머지 3' 재고 1개 사용 (남은 재고: 1개)

    4를 만들 수 있는가?

        4 % 5 = 4 입니다.

        '나머지 4' 재고가 2개 있습니다. (성공)

        '나머지 4' 재고 1개 사용 (남은 재고: 1개)

    5를 만들 수 있는가?

        5 % 5 = 0 입니다.

        '나머지 0' 재고가 1개 남아있습니다. (성공)

        '나머지 0' 재고 1개 사용 (남은 재고: 0개)

    6을 만들 수 있는가?

        6 % 5 = 1 입니다.

        '나머지 1' 재고가 1개 남아있습니다. (성공)

        '나머지 1' 재고 1개 사용 (남은 재고: 0개)

    ... 이런 식으로 계속 진행하면 ...

    9를 만들 수 있는가?

        9 % 5 = 4 입니다.

        '나머지 4' 재고가 1개 남아있습니다. (성공)

        '나머지 4' 재고 1개 사용 (남은 재고: 0개)

    10을 만들 수 있는가?

        10 % 5 = 0 입니다.

        '나머지 0' 재고를 확인해 보니... 0개 입니다. 더 이상 사용할 수 있는 숫자가 없습니다. (실패)