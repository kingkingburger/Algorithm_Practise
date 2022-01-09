package N_2743;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class N_2743 {
    public static void main(String[] args) throws IOException {

        int result = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        //단어입력
        String input = br.readLine();

        //단어 개수 세기
        for (int i = 0; i<input.length(); i++){
            result++;
        }

        System.out.println(result);
    }
}
