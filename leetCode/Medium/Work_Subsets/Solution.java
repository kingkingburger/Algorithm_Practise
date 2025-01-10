package leetCode.Medium.Work_Subsets;

import java.util.ArrayList;
import java.util.List;

class Solution {
  public boolean check(String str1, String str2) {
    String[] strArr = str2.split("");
    int checkFlag = 0;
    for (String s : strArr) {
      if (str1.contains(s)) {
        str1 = str1.replaceFirst(s, "");
        checkFlag++;
      }
    }
    return checkFlag == strArr.length;
  }

  public List<String> wordSubsets(String[] words1, String[] words2) {
    List<String> answer = new ArrayList<>();
    for (String s : words1) {
      int checkNumber = 0;
      for (String string : words2) {
        if (check(s, string)) {
          checkNumber++;
        }
      }
      if (checkNumber == words2.length) {
        answer.add(s);
      }
    }

    return answer;
  }

  public static void main(String[] args) {
    Solution solution = new Solution();

    // [facebook, google, leetcode]
    System.out.println(
        solution.wordSubsets(
            new String[] {"amazon", "apple", "facebook", "google", "leetcode"},
            new String[] {"e", "o"}));

    // ["google","leetcode"]
    System.out.println(
        solution.wordSubsets(
            new String[] {"amazon", "apple", "facebook", "google", "leetcode"},
            new String[] {"lo", "eo"}));

    // ["facebook","google"]
    System.out.println(
        solution.wordSubsets(
            new String[] {"amazon", "apple", "facebook", "google", "leetcode"},
            new String[] {"e", "oo"}));
  }
}
