package N_10842;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class N_10842 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] Num = br.readLine().split(" ");

        //int형으로 하면 에러가 난다. 그릇이 작음
        Long result_ab = Long.parseLong(Num[0] + Num[1]);
        Long result_cd = Long.parseLong(Num[2] + Num[3]);
        System.out.print(result_ab + result_cd);
    }
}
