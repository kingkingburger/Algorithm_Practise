#include <bits/stdc++.h>
using namespace std;

class Solution {
 public:
  // string convertToBaseK(int num, int k) {
  //   if (num == 0) return "0";
  //   string result;
  //   while (num > 0) {
  //     result += to_string(num % k);
  //     num /= k;
  //   }
  //   reverse(result.begin(), result.end());
  //   return result;
  // }

  // bool isPalindrome(int x) {
  //   if (x < 0) return false;
  //   int original = x;
  //   int reversed = 0;
  //   while (x > 0) {
  //     int digit = x % 10;
  //     reversed = reversed * 10 + digit;
  //     x /= 10;
  //   }
  //   return reversed == original;
  // }

  // long long kMirror(int k, int n) {
  //   long long sum = 0;
  //   // k 진수
  //   // mirror number의 개수 n
  //   int i = 1;
  //   int check = 0;
  //   while (check < n) {
  //     string binaryCheck = convertToBaseK(i, k);
  //     long long value = stoll(binaryCheck);
  //     //   if (isPalindrome(value) && isPalindrome(i)) {
  //     if (isPal(binaryCheck) && isPal(to_string(i))) {
  //       check++;
  //       sum += i;
  //       cout << "isPalindrome: " << i << " " << binaryCheck << endl;
  //     }
  //     i++;
  //   }
  //   cout << "sum: " << sum << endl;
  //   return sum;
  // }

  string toBaseK(long long num, int k) {
    if (num == 0) return "0";
    string s;
    while (num > 0) {
      s.push_back('0' + (num % k));
      num /= k;
    }
    reverse(s.begin(), s.end());
    return s;
  }

  bool isPal(string s) {
    int i = 0, j = s.size() - 1;
    while (i < j) {
      if (s[i++] != s[j--]) return false;
    }
    return true;
  }

  long long kMirror(int k, int n) {
    long long sum = 0;
    int found = 0;
    int length = 1;

    while (found < n) {
      int halfLen = (length + 1) / 2;
      int start = (long long)pow(10, halfLen - 1);  // 1, 10, 100, ...
      int end = (long long)pow(10, halfLen) - 1;    // 9 , 99, 999, ...

      for (long long prefix = start; prefix <= end && found < n; ++prefix) {
        string left = to_string(prefix);
        string full = left;

        for (int i = halfLen - (length % 2) - 1; i >= 0; --i) {
          full.push_back(left[i]);
        }

        long long val = stoll(full);

        if (isPal(toBaseK(val, k))) {
          sum += val;
          found++;
          // cout << "#" << found << ": " << val << " (decimal pal: " << full
          //      << ", base-" << k << " pal: " << convertToBaseK(val, k) <<
          //      ")\n";
        }
      }
      length++;
    }
    cout << "sum: " << sum << endl;
    return sum;
  }
};

int main() {
  Solution sol;
  //   auto result = sol.kMirror(2, 5);
  //   auto result = sol.kMirror(3, 7);
  auto result = sol.kMirror(5, 25);  // 6849225412
  //   auto result = sol.kMirror(7, 17);
  return 0;
}