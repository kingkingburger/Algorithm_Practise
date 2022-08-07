## 3 x n 타일링

```java
    static int solution(int n) {
        int mod = 1000000007;
        int[] dp = new int[n + 1];

        dp[1] = 2;
        dp[2] = 3;

        for (int i = 3; i <= n; i++) {
            if (i % 2 == 0) { //짝수
                dp[i] = dp[i - 1] % mod + dp[i - 2] % mod;
            } else { // 홀수
                dp[i] = (dp[i - 1] * 2) % mod + dp[i - 2] % mod;
            }
            dp[i] = dp[i] % mod;
        }

        return dp[n];
    }
```

2  x n 타일링 문제처럼 dp로 풀 수 있는 문제였습니다. 

도처히 패턴을 파악할 수 가 없어 다른분의 풀이를 참고했습니다.



#### **N = 1일 때,** 

물론 N이 1일 때 완전하게 모든 공간에 타일 배치를 하는 것은 불가능 하다. (세로 길이가 3이기 때문에)

그럼에도 불구하고 1*3 이라는 공간에 타일을 배치하는 방법을 그려보았다. 



![img](https://blog.kakaocdn.net/dn/707xT/btrmkq5xKGb/oAPmERtbvho4XLgpoOj9h0/img.png)



위, 아래로 2가지 경우의 수가 있다.

#### **N = 2일 때,** 



![img](https://blog.kakaocdn.net/dn/AvBiY/btrmtWaLYHc/metSNCHDhpFkwDs94wqhI0/img.png)



3가지 경우의 수가 있다. 

#### **N = 3일 때,** 

**N이 홀수일때는 완전하게 모든 공간을 가득 채우는건 불가능**하다. 

다만 패턴을 찾기 위해 아래와 같이 경우의 수를 도출해보았다. 

N이 홀수일 때: dp[N] = dp[N-1]*2 + dp[N-2];

- N이 2일 때의 패턴에다가 세로 타일을 위 아래로 하나씩 붙임
- N이 1일 때의 패턴에다가 가로 타일을 세 개 연달아 붙임



![img](https://blog.kakaocdn.net/dn/ZJp09/btrmhum2ZOJ/YkK9kV3XcJCjBUhHEe90ek/img.png)



#### **N = 4일 때,**

그려놓고 보니, N이 3일 때와 N이 2일 때의 패턴에다가 타일을 붙인 것을 알 수 있었다.

따라서 아래와 같이 식을 도출할 수 있었다.

N이 짝수일 때: dp[N] = dp[N-1] + dp[N-2];



![img](https://blog.kakaocdn.net/dn/JV7Fy/btrmjIEGoZD/P0kzXzFdGwiondck67rrf0/img.png)



 

### **점화식**

N이 홀수일 때: dp[N] = dp[N-1]*2 + dp[N-2];

N이 짝수일 때: dp[N] = dp[N-1] + dp[N-2];

 

### **전체 패턴**



![img](https://blog.kakaocdn.net/dn/lhiOz/btrmrm1Qbo5/Wqx9sxuXoa2RC9MmnDzVmK/img.png)



####  참고

https://gom20.tistory.com/180