## N과 M(1)

```java
public class N과M1 {

    static void dfs(int n, int m, int[] arr, boolean[] visited, int depth){
        if (depth == m) {
            for (int i : arr) {
                System.out.print(i+ " ");
            }
            System.out.println();
            return ;
        }

        for (int i = 0; i < n; i++) {
            if (visited[i] == false) {
                visited[i] = true;
                arr[depth] = i + 1;
                dfs(n, m, arr, visited, depth + 1);
                visited[i] = false;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        boolean[] visited = new boolean[n];
        int[] arr = new int[m];

        dfs(n, m, arr, visited, 0);
    }
}

```

백트래킹의 기본에 대해서 배우고 실천했습니다.

dfs의 종료조건은 **depth가 m 만큼 차면 종료**합니다.



dfs를 기본으로 하고 **visited[] 배열**을 이용해서 중복을 하지 않고 탐색 할 수 있습니다.

매개변수중 **arr**는 정답을 저장하는 공간입니다.

**depth**는 이 dfs가 재귀호출로 얼마나 스택이 쌓였는지 알 수 있습니다.



 [흐름]

- depth는 0부터 시작해서 m까지 이어집니다.
- 0 -> n까지 진행되는데 arr에 들어갈 정답은 +1를 해서 들어가게 됩니다.
- 다음 dfs 재귀에 들어가게 됩니다. 이제 visited를 보고 중복은 제외한 for문을 돕니다
- arr에 정답을 넣게 됩니다.
- depth가 m이 되면 print를 합니다.