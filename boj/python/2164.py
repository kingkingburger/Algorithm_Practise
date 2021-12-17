from collections import deque

input_num = int(input())

#deque 만들기
def make_deq(num):
    deq = deque()
    for i in range(1, num+1):
        deq.append(i)
    
    return deq

#카드 하나를 버리고 하나는 뒤로 넣기
def mix_card(deq):
    for _ in range(len(deq)):
        result = deq.popleft()
        deq.rotate(-1)
    return result

deq = make_deq(input_num)
print(mix_card(deq))