n, m = map(int, input().split())

base = [] # 재귀함수를 이용하여 m개의 수열을 저장하기 위한 리스트

def dfs():
    #리스트에 들어간 수열들이 m개가 되면
    #리스트에 들어있는 숫자들을 모두 출력하고 함수를 나온다.
    if(len(base) == m):                
        print(' '.join(map(str,base)))
        return

    for i in range(1, n+1):
        if i not in base:  #리스트 s 중복여부 확인
            base.append(i)
            dfs()
            base.pop()

dfs()