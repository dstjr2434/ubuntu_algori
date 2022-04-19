# def solution(people, limit):
#     answer = 0
#     sum=0
#     people.sort()

#      # 사람들이 다빠져나갈때까지
#     while people:
#         # 리스트의 요소들 중에서 가장큰수와 큰
#         sum+=people.pop(-1)
#         # limit를 넘지않으면서 작은수들중에서 가장 큰수를 더한다
#         flag=-1
#         for idx,_ in enumerate(people):
#             if sum+people[idx]>limit:
#                 break
#             elif sum+people[idx]==limit:
#                 flag=idx
#             else:
#                 flag=idx
#         if flag !=-1:
#             people.pop(flag)
#         answer+=1
#         sum=0
            
#     return answer

# # print(solution([70, 50, 80, 50,40,20,25,43],100))
# # print(solution([70, 80, 50], 100))
# print(solution([40,50,150,160],200))


def solution(people,limit):
    answer = 0
    people.sort()

    start,end=0, len(people)-1

    while start<=end:
        answer+=1
        if people[start]+people[end]<=limit:
            start+=1
        end-=1
    return answer

# print(solution([70, 50, 80, 50,40,20,25,43],100))
# print(solution([70, 80, 50], 100))
print(solution([40,50,150,160],200))