#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

vector<int> minOperations(string boxes) {
  vector<int> answer;
  int n = boxes.size();

  for (int i = 0; i < n; i++) {
    int result = 0;
    for (int j = 0; j < n; j++) {
      if (i != j && boxes[j] == '1') {
        result += abs(j - i);
      }
    }
    answer.push_back(result);
  }

  return answer;
}

int main() {
  vector<int> result1 = minOperations("110");
  for (int num : result1) {
    cout << num << " ";
  }
  cout << endl;

  vector<int> result2 = minOperations("001011");
  for (int num : result2) {
    cout << num << " ";
  }
  cout << endl;

  return 0;
}
