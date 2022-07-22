## Dfs와 Bfs

```java
public class Main {
    static int n ;
    static int m ;
    static int graph[][];
    static int visited[];
    static void dfs(int k){
        visited[k] = 1;
        System.out.print(k + " ");
        for (int i = 1; i <= n; i++) {
            if(graph[k][i] == 1 && visited[i] == 0){
                dfs(i);
            }
        }
    }

    static void bfs(int k){
        Queue<Integer> queue = new LinkedList<>();
        queue.add(k);
        visited[k] = 1;

        while (!queue.isEmpty()) {
            Integer i = queue.poll();
            System.out.print(i+ " ");
            for (int j = 1; j <= n; j++) {
                if(visited[j] == 0 && graph[i][j] == 1){
                    queue.add(j);
                    visited[j] = 1;
                }
            }

        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        int start = Integer.parseInt(st.nextToken());

        graph = new int[1001][1001];
        visited = new int[1001];

        int v1 = 0;
        int v2 = 0;

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            v1 = Integer.parseInt(st.nextToken());
            v2 = Integer.parseInt(st.nextToken());
            graph[v1][v2] = 1;
            graph[v2][v1] = 1;
        }

        dfs(start);

        for (int i = 0; i <= n; i++) {
            visited[i] = 0;
        }

        System.out.println();
        bfs(start);
    }
}

```

dfs와 bfs의 기본 계념을 물어봣습니다.

기본 계념은 그렇다 치더라도 더 어려웠던 것이 그래프의 계념이였습니다.

2차 배열(여기서 **graph**)의 `행`을 기준으로 지정합니다.

다음 열을 그 `행`과 연결된 숫자를 넣습니다.

ex) [1] [2] 는 1과 2는 붙어있다를 뜻합니다.



#### 그리고 visitied 배열의 필요성을 느꼈습니다.

visited 배열이 없다면 한번 지나간 곳에 다시 들릴 수 있습니다. 왜냐하면 graph를 초기화 할 때 [1] [4] 가 붙어있다는 건  [4] [1]이 붙어있다는 것을 뜻합니다.

그래서 대칭으로 **graph(2차 배열)**을 초기화 해줍니다. 



visited 배열     `0`이 방문 x          `1`이 방문o

graph 는 `1`이 연결되어 있는 상태 