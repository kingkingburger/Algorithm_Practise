def solution(cards1, cards2, goal):
    answer = "Yes"
    # 카드뭉치에서 꺼낸 위치
    idx1 = 0
    idx2 = 0

    for i, word in enumerate(goal):
        if word == cards1[idx1]:
            if idx1 != len(cards1)-1:
                idx1 += 1
        elif word == cards2[idx2]:
            if idx2 != len(cards2)-1:
                idx2 += 1
        else:
            answer = "No"
    return answer


# 다른사람의 풀이
# def solution(cards1, cards2, goal):
#     for g in goal:
#         if len(cards1) > 0 and g == cards1[0]:
#             cards1.pop(0)
#         elif len(cards2) >0 and g == cards2[0]:
#             cards2.pop(0)
#         else:
#             return "No"
#     return "Yes"

#                0      1         2       0      1       0      0      1      1        2
print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))

#                0      1         2       0      1       0      1        2      0        1
print(solution(["i", "drink", "water"], ["want", "to"], ["i", "drink", "water", "want", "to"]))

#                0      1         2        0      1       0      1      2       3        4
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))

#                0     1     2       0      1      2       0     1      2      3
print(solution(["i", "see", "to"], ["you", "now", "me"], ["i", "see", "now", "me"]))
