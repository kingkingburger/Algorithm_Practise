package N_10809;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class N_10809 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        //알파벳 위치
        int[] alphabet = new int[26];

        //배열을 -1로 채우기
        Arrays.fill(alphabet, -1);

        //문자열 받기
        String words = br.readLine();

        //문자열 하나하나의 순서를 배열에 넣는다.
        //int로 변환해서 'a'의 아스키코드에 뺀값은 알파벳의 'a'로 부터 떨어진 위치이다.
        for (int i = 0; i<words.length(); i++){
            if(alphabet[(int)words.charAt(i)-97] < 0){
                alphabet[(int)words.charAt(i)-97] = i;
            }
        }

        //StringBuilder에 배열에 있는 모든 것을 넣는다.
        for(int word : alphabet){
            sb.append(word + " ");
        }

        System.out.println(sb);

    }
}
