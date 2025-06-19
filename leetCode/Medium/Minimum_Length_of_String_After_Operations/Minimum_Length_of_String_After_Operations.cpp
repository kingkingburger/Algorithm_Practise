#include <bits/stdc++.h>
using namespace std;

class Solution {
 public:
  int minimumLength(string s) {
    int result = 0;
    map<char, int> charIndex;
    for (int i = 0; i < s.size(); ++i) {
      charIndex[s[i]]++;
    }
    for (auto& [ch, count] : charIndex) {
      if (count % 2 == 0) {
        result += 2;  // 짝수인 경우
      } else {
        result += 1;  // 홀수인 경우
      }
    }

    // 결과 출력
    // for (auto& [ch, indices] : charIndex) {
    //   int totalSize = indices;
    //   if (totalSize >= 3) {
    //     if (totalSize % 2 == 0) {
    //       totalSize = 2;
    //     } else {
    //       totalSize = 1;
    //     }
    //     result += totalSize;
    //   } else {
    //     result += totalSize;
    //   }
    //   //   cout << ch << " → ";
    //   //   for (int idx : indices) cout << idx << ' ';
    //   //   cout << '\n';
    //   //   cout << result << endl;
    // }
    return result;
  }
};

int main() {
  Solution solution;

  //   int result = solution.minimumLength("abaacbcbb");  // 5
  // int result = solution.minimumLength("aa");  // 2
  int result = solution.minimumLength(
      "ucvbutgkohgbcobqeyqwppbxqoynxeuuzouyvmydfhrprdbuzwqebwuiejoxsxdhbmuaisca"
      "lnteocghnlisxxawxgcjloevrdcj");  // 38
  cout << "result" << result << endl;
  return 0;
}
