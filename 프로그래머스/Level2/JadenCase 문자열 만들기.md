## JadenCase 문자열 만들기

```java
    static String solution(String s) {
        StringBuilder sb = new StringBuilder();
        StringBuilder answer = new StringBuilder();

        char[] chars = s.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == ' ') {
                distinguish(sb, answer);// 문자를 Jaden형식으로 바꾸기
                answer.append(' ');
            }else { // 문자인거 판별
                sb.append(chars[i]);
                if(i == chars.length - 1){
                    distinguish(sb,answer);
                }
            }
        }
        return answer.toString();
    }

    private static void distinguish(StringBuilder sb, StringBuilder answer) {
        if(sb.length() > 0){
            String first = sb.substring(0,1).toUpperCase();
            String other = sb.substring(1).toLowerCase();
            answer.append(first + other);
            sb.setLength(0);
        }
    }
```

문자열을 받아서 공백까지 같이 구현해야 합니다. 처음에 **StringTokenizer**로 공백을 모두 줄이는 방법을 썻더니 답이 아니였습니다.

String을 char형태로 자르고 공백이 나타나면 이전에 **StringBuilder**에 모아둔 문자를 **Jaden 형식**으로 바꿉니다.(distinguish() 메서드에서 바꿉니다.) 공백이 안나타나면 계속해서 문자를 모아둡니다. 



#### 다른사람의 풀이

```java
class Solution {
  public String solution(String s) {
        String answer = "";
        String[] sp = s.toLowerCase().split("");
        boolean flag = true;

        for(String ss : sp) {
            answer += flag ? ss.toUpperCase() : ss;
            flag = ss.equals(" ") ? true : false;
        }

        return answer;
  }
}
```

너무 깔금합니다.

모든 공백이 올 때 `공백 or 첫 번째 문자`를 대문자로 바꾸고 answer 변수에 집어넣는 형태입니다.

처음에 flag가 true이니 공백 다음은 무조건 대문자가 들어갈 것 입니다.