import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class N_1978 {

    public static int NumberSieve(int number){
        int[] a = new int[10000];
        int sosu_count = 0;
        //배열 초기화
        for(int i= 2; i <= number; i++){
            a[i] = 1;
        }

        //2부터 배수에 해당하는 수를 모두 지움
        for(int i=2; i<= number;i++){
            if(a[i] == 0){ // 이미 지워진 수라면 건너뜀
                continue;
            }
            // 이미 지워진 숫자가 아니라면, 해당 숫자를 제외하고 다음 배수를 모두 0으로 만듬
            for(int j = i*2; j<= number; j += i){
                a[j] = 0;
            }
        }

        //number가 배열에서 1이라면 = 소수인것
        if(a[number] != 0){
            sosu_count++;
        }

        return sosu_count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int test_case = Integer.parseInt(br.readLine());
        int result =0;
        String[] Num = br.readLine().split(" ");

        for(int count = 0; count < test_case; count++){
            result += NumberSieve(Integer.parseInt(Num[count]));
        }

        System.out.println(result);
    }
}
