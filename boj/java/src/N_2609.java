import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class N_2609 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] Num = br.readLine().split(" ");
        int num1 = Integer.parseInt(Num[0]);
        int num2 = Integer.parseInt(Num[1]);

        //num1이 항상 num1보다 크게
        if(num1 < num2){
            int temp;
            temp = num1;
            num1 = num2;
            num2 = temp;
        }

        //최대공약수
        for(int i = num1; i > 0; i--){
            if((num1 % i) == 0 && (num2 % i) == 0 ){
                System.out.println(i);
                break;
            }
        }

        //최소공배수
        int bigger = num1;
        while(true){
            if((bigger % num1 == 0) && (bigger % num2 == 0)){
                System.out.println(bigger);
                return;
            }
            bigger++;
        }

    }
}
