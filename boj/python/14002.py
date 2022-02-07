test_case = int(input())
nums = list(map(int,input().split()))
dp = [1] * test_case

for i in range(1, test_case):
    for j in range(i): # 자리수 맨 왼쪽부터 들어온다.
        if(nums[i] > nums[j]): # 자리수 왼쪽부터 체크
            dp[i] = max(dp[j]+ 1 , dp[i]) # 바뀐 것, 더 큰것 체크

#수열의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
print(max(dp)) # 꼭 끝쪽에 최대 길이 배열이 없을 수 있다.

#가장 긴 증가하는 부분 수열
high_num = max(dp)
li = []
for k in range(test_case-1, -1, -1):
    if(dp[k] == high_num):
        li.append(nums[k])
        high_num -= 1 # 찾아야되는 수열을 1씩 줄인다.

li.reverse()
for q in li:
    print(q, end=' ')

