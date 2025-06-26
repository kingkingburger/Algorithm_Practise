처음에 만들었던 코드입니다
```
  string convertToBaseK(int num, int k) {
    if (num == 0) return "0";
    string result;
    while (num > 0) {
      result += to_string(num % k);
      num /= k;
    }
    reverse(result.begin(), result.end());
    return result;
  }

  bool isPalindrome(int x) {
    if (x < 0) return false;
    int original = x;
    int reversed = 0;
    while (x > 0) {
      int digit = x % 10;
      reversed = reversed * 10 + digit;
      x /= 10;
    }
    return reversed == original;
  }
  
    long long kMirror(int k, int n) {
      long long sum = 0;
      // k 진수
      // mirror number의 개수 n
      int i = 1;
      int check = 0;
      while (check < n) {
        string binaryCheck = convertToBaseK(i, k);
        long long value = stoll(binaryCheck);
        //   if (isPalindrome(value) && isPalindrome(i)) {
        if (isPal(binaryCheck) && isPal(to_string(i))) {
          check++;
          sum += i;
        }
        i++;
      }
      return sum;
    }
```
k진법을 가진 수를 만드는 함수, 대칭인지 파악하는 함수 2개를 활용해서 문제를 풀 수 있었습니다만, 시간초과가 걸렸습니다. 고민해보고 답이 안나와서 gpt 한태 물어보면서 같이 답을 찾았습니다.

1부터 계속 차례대로 값을 찾았는데요 이 방법말고 대칭인 것(palindrome)만 찾으면 되요. 문제는 `일반 n값`과 `k진법이 변환된 값 n의 값`2개다 대칭인 것만 sum을 하는 걸 원해요. 즉 일반n이 대칭이 되어야 하죠.

1부터 n까지 대칭 검사를 하는게 아닌 대칭인 n을 만듭니다. 그것의 k진법 변환 값을 대칭을 찾는게 더 효율적이라고 하다고 해요.
## 실제로 검사하는 범위의 차이

- **전수조사:** 1, 2, 3, 4, ..., 9999 (전부 검사)
- **palindrome 생성:** 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, ..., 9999 (palindrome만 생성)

## **start ~ end는 prefix 범위다**

- **prefix의 범위(start~end)는 전체 숫자 범위가 아니라 "palindrome의 절반(혹은 절반+1자리)"만큼의 범위**
- 예시: 6자리 palindrome이면, prefix는 100~999(3자리)
- 100~999 = 900개 → 6자리 palindrome 900개를 한 번에 만들어냄    
- 전수조사로 하면 100000~999999(90만 개) 전부 검사하는 셈!
