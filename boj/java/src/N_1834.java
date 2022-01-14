import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class N_1834 {

    public static void swap(int num1, int num2){
        //num1이 항상 num1보다 크게
        if(num1 < num2){
            int temp;
            temp = num1;
            num1 = num2;
            num2 = temp;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testcase = Integer.parseInt(br.readLine());

        for(int i =0;i < testcase; i++){
            String[] Num = br.readLine().split(" ");

            int num1 = Integer.parseInt(Num[0]);
            int num2 = Integer.parseInt(Num[1]);

            //num1이 항상 num1보다 크게
            swap(num1, num2);

            //최대공약수
            for(int j = num1; j > 0; j--){
                if((num1 % j) == 0 && (num2 % j) == 0 ){
                    //최소공배수 = (2개 수의 곱 / 최대공약수)
                    System.out.println((num1*num2)/j);
                    break;
                }
            }

        }
    }
}
