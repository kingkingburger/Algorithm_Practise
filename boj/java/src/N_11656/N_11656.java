package N_11656;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class N_11656 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String input_text = br.readLine();
        String[] words = new String[input_text.length()];

        for(int i = 0 ; i < input_text.length(); i++){
            words[i] = input_text.substring(i);
        }
        Arrays.sort(words);

        for(String j : words){
            System.out.println(j);
        }
    }
}
