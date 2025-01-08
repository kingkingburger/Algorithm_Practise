package leetCode.Medium.Minumum_Number_of_Operations_to_move_all_balls_to_each_box;

import java.util.Objects;

class Solution {
  public int[] minOperations(String boxes) {
    int[] answer = new int[boxes.length()];
    String[] boxList = boxes.split("");

    for (int i = 0; i < boxList.length; i++) {
      int sum = 0;

      for (int j = 0; j < boxList.length; j++) {
        if (i != j && Objects.equals(boxList[j], "1")) {
          sum += Math.abs(j - i);
        }
      }

      answer[i] = sum;
    }

    return answer;
  }

  public static void main(String[] args) {
    Solution solution = new Solution();
    solution.minOperations("110");
  }
}
