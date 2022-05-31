## N개의 최소공배수

```java
public static int min(int a , int b) {
        int sum = a * b;
        while(!(a % b == 0)){
            int temp = b;
            b = (a % b);
            a = temp;
        }

        return (sum / b);
    }
    public static int solution(int[] arr) {
        int result = 0;

        for (int i = 0; i < arr.length - 1; i++) {
            int a = arr[i];
            int b = arr[i+1];
            result = result > 0 ? min(result, b) : min(a, b);
        }

        return result;
    }

    public static void main(String[] args) {
        solution(new int[] {2,6,8,14});
    }
```

`유클리드 호제법`을 사용했습니다.

삼항 연산자를 이용해 좀더 깔끔하게 쓸 수 있었습니다. 처음에 시작하면 첫 번째 수, 두 번째 수로 시작을 하고 그 이후로는 앞의 두수의 결과값의 최소공배수를 구합니다.

```java
//최대공약수 - 유클리드 호제법(num2의 나머지가 0보다 크면 나머지를 나누기)
//1. a = 10, b = 8, 나머지 2 => a = 8, b = 2
//2. a = 8, b = 2, 나머지 0 => a = 2, b = 0
while(!(num1 % num2 == 0)){
    int temp = num2;
    num2 = (num1 % num2);
    num1 = temp;
}
System.out.println(num2);

//최소공배수 - 두 수의곱 / 최대공약수
System.out.println(result / num2);
```

예전에 풀었던 논리가 생각나서 최대공약수를 구하고 -> 두수의 곱 / 최대공약수를 해서 최소공배수를 구했습니다. 