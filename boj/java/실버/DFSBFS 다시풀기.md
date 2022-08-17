## DFSBFS 다시풀기

```java

public class DFSBFS {

    static int[][] graph;

    static boolean[] visited;

    static int n;
    static int m;
    static void dfs(int v){
        System.out.print(v + " ");
        visited[v] = true;

        for (int i = 1; i <= n; i++) {
            if(graph[v][i] == 1 && !visited[i]){
                visited[i] = true;
                dfs(i);
            }
        }
    }

    static void bfs(int v){
        Queue<Integer> queue = new LinkedList<>();
        queue.add(v);
        visited[v] = true;

        while (!queue.isEmpty()) {
            Integer poll = queue.poll();
            System.out.print(poll + " ");
            for (int i = 1; i <= n; i++) {
                if (graph[poll][i] == 1 && !visited[i]) {
                    visited[i] = true;
                    queue.add(i);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());

        graph = new int[1001][1001];
        visited = new boolean[1001];

        for (int i = 1; i <= m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a][b] = 1;
            graph[b][a] = 1;
        }

        dfs(v);
        visited = new boolean[1001];
        System.out.println();
        bfs(v);
    }
}

```

graph와 visited를 설정하는것이 중요합니다.

1차 배열에는 노드를 설정하고 2차 배열에 연결된 노드를 설정해야 합니다.

graph를 연결할 때도 1차 2차를 동시에 연결해야 양방향으로 연결된것 처럼 됩니다.