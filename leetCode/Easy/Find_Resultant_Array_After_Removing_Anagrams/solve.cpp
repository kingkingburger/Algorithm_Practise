#include <bits/stdc++.h>

#include <algorithm>
#include <string>
using namespace std;

class Solution {
 public:
  bool compareWord(string s1, string s2) {
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());
    return s1 == s2;
  };

 public:
  vector<string> removeAnagrams(vector<string>& word) {
    vector<string> answer;
    answer.push_back(word[0]);
    for (int i = 1; i < word.size(); i++) {
      if (!compareWord(answer.back(), word[i])) {
        answer.push_back(word[i]);
      }
    }
    return answer;
  }
};

int main() {
  Solution sol;
  vector<string> input1 = {"abba", "baba", "bbaa", "cd", "cd"};
  auto result1 = sol.removeAnagrams(input1);
  for (auto result : result1) {
    cout << result << endl;
  }
}