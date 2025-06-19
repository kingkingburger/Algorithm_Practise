s문자를 준다면 index i 고르고 옆에 자기와 같은게 있다면 지우는식?

i가 있을 때 자기 주변에 있는 같은 캐릭터가 있다면 그거 삭제하는 식으로 만들어라.

문자열을 dict로 만든다음 문자마다 i,j,k를 비교했을 때 1개씩 지우고 남아있는 문자 개수를 처리하면 되지 않을까요.

제가 생각한 아이디어는 글자를 dictionary로 뽑아내서 남아있는 문자가 3개 이상인데 홀수라면 +1, 짝수라면 +2 하는 방식으로 답을 구했어요.

- 코드
    
    ```cpp
    class Solution {
     public:
      int minimumLength(string s) {
        int result = 0;
        map<char, vector<int>> charIndex;
        for (int i = 0; i < s.size(); ++i) {
          charIndex[s[i]].push_back(i);
        }
    
        // 결과 출력
        for (auto& [ch, indices] : charIndex) {
          int totalSize = indices.size();
          if (totalSize >= 3) {
            if (totalSize % 2 == 0) {
              totalSize = 2;
            } else {
              totalSize = 1;
            }
            result += totalSize;
          } else {
            result += totalSize;
          }
        }
        return result;
      }
    };
    
    ```
    

- 다른분 코드
    
    ```cpp
    class Solution {
    public:
        int minimumLength(string s) {
            vector<int> charFreq(26, 0);
            for(auto &c : s){
                charFreq[c - 'a']++;
            }
            int len = 0;
            for(auto &freq : charFreq){
                if(freq % 2){
                    len += 1;
                }else if(freq > 0){
                    len += 2;
                }
            }
            return len;
        }
    };
    ```
    

저랑 비슷한 생각을 했는데 더 깔끔하네요. map을 쓰지 않고 `char : 숫자` 형태로 더 간소화했어요.

- 내 코드에서 수정한 부분
    
    ```cpp
        int result = 0;
        map<char, int> charIndex;
        for (int i = 0; i < s.size(); ++i) {
          charIndex[s[i]]++;
        }
        for (auto& [ch, count] : charIndex) {
          if (count % 2 == 0) {
            result += 2;  // 짝수인 경우
          } else {
            result += 1;  // 홀수인 경우
          }
        }
    ```
    

굳이 map에 문자를 담을 필요가 없어요. 3개 이상 확인하는 코드도 필요없어요. 홀, 짝일 때 규칙을 적용하면 됬었네요.