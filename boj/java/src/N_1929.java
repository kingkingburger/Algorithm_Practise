import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class N_1929 {
    public static void NumberSieve(int number1, int number2) {

        int[] a = new int[1000000];

        //배열 초기화
        for (int i = 2; i <= number2; i++) {
            a[i] = 1;
        }

        //2부터 배수에 해당하는 수를 모두 지움
        for (int i = 2; i <= number2; i++) {
            if (a[i] == 0) { // 이미 지워진 수라면 건너뜀
                continue;
            }
            // 이미 지워진 숫자가 아니라면, 해당 숫자를 제외하고 다음 배수를 모두 0으로 만듬
            for (int j = i * 2; j <= number2; j += i) {
                a[j] = 0;
            }
        }

        //number가 배열에서 1이라면 = 소수인것
        for (int num = number1; num <= number2; num++) {
            if (a[num] != 0) {
                System.out.println(num);
            }
        }


    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] Num = br.readLine().split(" ");

        NumberSieve(Integer.parseInt(Num[0]),Integer.parseInt(Num[1]));

    }
}
