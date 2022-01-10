package N_11655;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class N_11655 {
    public static void main(String[] args) throws IOException {


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        //단어입력
        String input = br.readLine();
        for (int i = 0; i < input.length(); i++) {
            int word = (int) input.charAt(i);

            //소문자 일 때
            if (65 <= word && word <= 90) {
                if(word >= 78){ // N을 기준으로 크면 +13 작으면 -13
                    word = word - 13;
                }else{
                    word = word + 13;
                }
                sb.append((char)word); // char타입으로 바꿔서 AsCii 코드를 문자로
            }

            //대문자 일 때
            else if (97 <= word && word <= 122) {
                if( word >= 110){
                    word = word - 13;
                }else{
                    word = word + 13;

                }
                sb.append((char)word);
            }

            else if (word == 32){
                sb.append(" ");
            }
            else{
                sb.append((char)word);
            }
        }

        System.out.println(sb);
    }
}
