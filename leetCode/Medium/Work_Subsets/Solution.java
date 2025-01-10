package leetCode.Medium.Work_Subsets;

import java.util.ArrayList;
import java.util.List;

class Solution {
  // Helper method to calculate frequency of characters in a word
  private int[] getCharFrequency(String word) {
    int[] freq = new int[26]; // Assuming only lowercase letters
    for (char c : word.toCharArray()) {
      freq[c - 'a']++;
    }
    return freq;
  }

  public List<String> wordSubsets(String[] words1, String[] words2) {
    List<String> answer = new ArrayList<>();
    int[] requiredFreq = new int[26];

    // Step 1: Compute the maximum frequency for each character in words2
    for (String word : words2) {
      int[] wordFreq = getCharFrequency(word);
      for (int i = 0; i < 26; i++) {
        if (wordFreq[i] > requiredFreq[i]) {
          requiredFreq[i] = wordFreq[i];
        }
      }
    }

    // Step 2: For each word in words1, check if it satisfies the required frequencies
    for (String word : words1) {
      int[] wordFreq = getCharFrequency(word);
      boolean isUniversal = true;
      for (int i = 0; i < 26; i++) {
        if (wordFreq[i] < requiredFreq[i]) {
          isUniversal = false;
          break;
        }
      }
      if (isUniversal) {
        answer.add(word);
      }
    }

    return answer;
  }

  public static void main(String[] args) {
    Solution solution = new Solution();

    // [facebook, google, leetcode]
    //    System.out.println(
    //        solution.wordSubsets(
    //            new String[] {"amazon", "apple", "facebook", "google", "leetcode"},
    //            new String[] {"e", "o"}));

    // ["google","leetcode"]
    //    System.out.println(
    //        solution.wordSubsets(
    //            new String[] {"amazon", "apple", "facebook", "google", "leetcode"},
    //            new String[] {"lo", "eo"}));

    // ["facebook","google"]
    System.out.println(
        solution.wordSubsets(
            new String[] {"amazon", "apple", "facebook", "google", "leetcode"},
            new String[] {"e", "oo"}));
  }
}
