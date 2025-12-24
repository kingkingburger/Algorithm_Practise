#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int minimumBoxes(vector<int>& apple, vector<int>& capacity) {
      sort(capacity.begin(), capacity.end(), greater<int>()); 
      
      int n = 0;
      for(int a : apple) {
        n += a;
      }

      for(int i = 0; i < capacity.size(); ++i) {
        n -= capacity[i];
        if(n <= 0) {
          return i + 1;
        }
      }

      return 0;
    }
};

int main() {
  Solution sol;
  vector<int> apple1 = {1,3,2};
  vector<int> capacity1 = {4,3,1,5,2};
  int result = sol.minimumBoxes(apple1, capacity1);
  
  return 0;
}