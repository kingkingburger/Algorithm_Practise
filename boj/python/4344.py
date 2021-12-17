case_num=int(input())
sum=0
count=0
for _ in range(case_num):
    student_num = list(map(int,input().split()))
    for i in range(1,student_num[0]+1):
        sum += student_num[i]
    avg = sum/student_num[0]


    for k in range(1, student_num[0]+1):
        if(avg < student_num[k]):
            count +=1


    print("{0:.3f}%".format((count/student_num[0])*100))
    sum, avg, count=0,0,0


# case_num=int(input())

# for _ in range(case_num):
#     student_num = list(map(int,input().split()))
#     avg = sum(student_num[1:])/student_num[0]
#     count=0

#     for k in student_num[1:]:
#         if(avg < k):
#             count +=1

#     rate = (count/student_num[0])*100
#     print("{0:.3f}%".format(rate))
