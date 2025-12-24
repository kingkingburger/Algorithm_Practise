#include <bits/stdc++.h>

#include <vector>
using namespace std;

class Solution {
 public:
  bool getZero(int number) {
    while (number > 0) {
      if (number % 10 == 0) return true;
      number = number / 10;
    }
    return false;
  }
  vector<int> getNoZeroIntegers(int n) {
    for (int i = 2; i < n; i++) {
      int target = n - i;
      if (!getZero(target) && !getZero(i)) {
        return {i, target};
      }
    }
    return {1, 1};
  }
};

int main() {
  Solution sol;
  //   vector<int> result = sol.getNoZeroIntegers(2);
  //   cout << result[0] << result[1] << endl;
  //   vector<int> result = sol.getNoZeroIntegers(1010);  // [11, 999]
  //   cout << result[0] << endl << result[1] << endl;
  vector<int> result = sol.getNoZeroIntegers(4102);  // [111,3991]
  cout << result[0] << endl << result[1] << endl;
}