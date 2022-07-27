## N-Queen

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class NQueen {

    static int cnt;
    static int n;
    static int[] board;

    static void dfs(int row){ // 행
        if (row == n) {
            cnt++;
            return;
        }

        for (int i = 0; i < n; i++) { //열 모두를 탐색
            board[row] = i; // ex) 1행에 0 , 1, 2 ...

            //해당 행에서 i 번째 col에 놓을 수 있는지 검사하는 함수
            if (Possibility(row)) {
                dfs(row + 1);
            }
        }
    }

    public static boolean Possibility(int col) {

        for (int i = 0; i < col; i++) {
            // 해당 행의 열과 i행의 열이 일치할경우 (같은 열에 존재할 경우)
            if (board[col] == board[i]) {
                return false;
            }

            /*
             * 대각선상에 놓여있는 경우
             * (열의 차와 행의 차가 같을 경우가 대각선에 놓여있는 경우다)
             */
            else if (Math.abs(col - i) == Math.abs(board[col] - board[i])) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        board = new int[n];
        dfs(0);

        System.out.println(cnt);
    }
}
```

문제 접근과 아이디어를 못찾아서 다른분의 풀이를 보고 했습니다.

[![Eight-queens-animation.gif](https://upload.wikimedia.org/wikipedia/commons/1/1f/Eight-queens-animation.gif)](https://commons.wikimedia.org/wiki/File:Eight-queens-animation.gif)

위키백과에 있는 애니메이션 입니다.

배치하는 방법은 **row**를 기준으로 한줄 씩 내려가면서 **퀸이 들어갈 수 있는가?** 를 판별합니다.

Possibility() 메서드 안에서는 이전에 놔두었던 퀸의 위치를 보고 놓을 수 있는지 없는지 계산합니다.