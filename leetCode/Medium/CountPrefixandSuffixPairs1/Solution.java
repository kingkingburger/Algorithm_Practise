package leetCode.Medium.CountPrefixandSuffixPairs1;

class Solution {
  public boolean checkPairs(String str1, String str2) {
    int targetLength = str1.length();
    if (str2.length() >= (targetLength)) {
      String part1 = str2.substring(0, targetLength);
      String part2 = str2.substring(str2.length() - (targetLength));
      return str1.equals(part1) && str1.equals(part2);
    }

    return false;
  }

  public int countPrefixSuffixPairs(String[] words) {
    int answer = 0;
    for (int i = 0; i < words.length; i++) {
      for (int j = i + 1; j < words.length; j++) {
        if (checkPairs(words[i], words[j])) {
          answer++;
        }
      }
    }
    return answer;
  }

  public static void main(String[] args) {
    Solution solution = new Solution();
    System.out.println(
        solution.countPrefixSuffixPairs(new String[] {"a", "aba", "ababa", "aa"})); // 4)
    System.out.println(
        solution.countPrefixSuffixPairs(new String[] {"pa", "papa", "ma", "mama"})); // 2)
    System.out.println(solution.countPrefixSuffixPairs(new String[] {"bb", "bb"})); // 1)
    System.out.println(solution.countPrefixSuffixPairs(new String[] {"bc", "b", "ab"})); // 0)
  }
}
