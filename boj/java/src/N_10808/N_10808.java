package N_10808;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.Scanner;


public class N_10808 {
    public static void main(String[] args) throws IOException {

        int[] result = new int[26];

        Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String input = br.readLine();

        //String words = sc.next();
        //String.chars()를 이용해서 IntStream을 가져온 다음 boxed()에 넣어서 Integer 객체 스트림으로 만든
        //List에 넣기 위해 collect()를 사용함
        //List<Integer> word = words.chars().boxed().collect(Collectors.toList());
        for (int i = 0; i<input.length(); i++){
            result[(int)input.charAt(i)-97] += 1;
        }


        for (int j: result){
            sb.append(j);
            sb.append(" ");
        }
        System.out.println(sb);
    }
}
