package N_10820;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class N_10820 {
    //아스키코드
    //숫자 48 ~ 57
    //소문자 97 ~ 122
    //대문자 65 ~ 90

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String words = "";
        //문자열 받기
        while((words = br.readLine()) != null) {
            //숫자 개수
            int count = 0;
            //소문자 개수
            int lower = 0;
            //대문자 개수
            int upper = 0;
            //공백 개수
            int space = 0;

            //문자열 하나하나 검사한다.
            for (int i = 0; i<words.length(); i++){
                int str =(int)words.charAt(i);
                if(48 <= str  && str <= 57) {
                    count++;
                }
                else if(65 <= str && str <= 90){
                    upper++;
                }
                else if(97 <= str && str <= 122){
                    lower++;
                }
                else{
                    space++;
                }
            }

            //StringBuilder에 소문자, 대문자, 숫자, 공백을 순서대로 넣는다.
            sb.append(lower + " " + upper + " "+ count + " "+ space + " ");
            
            System.out.println(sb);
            //StringBuilder를 초기화
            sb.setLength(0);
        }
    }
}
