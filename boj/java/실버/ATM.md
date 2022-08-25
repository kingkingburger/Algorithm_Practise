## ATM

```java
public class ATM {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(nums);

        int result = 0;
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j <= i; j++) {
                count += nums[j];
            }
            result += count;
        }
        System.out.println(result);
    }
}

```

nums 배열에다가 대기시간을 넣습니다.

그리고 sort를 하면 최소시간으로 정렬이 됩니다.

2중 for문으로 각 자리수 까지의 합을 모두 더합니다.

더한 값을 출력하면 됩니다.