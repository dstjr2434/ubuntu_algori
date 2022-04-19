# # 1-2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접노드를 스택에 넣고 방문처리를 한다.
# # 1-3. 방문하지 않은 인접노드가 없으면 스택에서 최상단노드를 꺼낸다.
# # 1-4. 2번과 3번과정이 반복되지 않을때까지 수행한다.
# # 1-0. dfs는 탐색을 해야하는 공간과 탐색을 끝마친 공간이 있어야한다.
# # 1-0. 따라서 탐색을 끝마친공간을 노드의 수만큼 만들어준다.
# # 1-1. 탐색시작노드를 스택에 삽입하고 방문처리를 한다.

# def solution(numbers, target):
#     # 1-0. dfs는 탐색을 해야하는 공간과 탐색을 끝마친 공간이 있어야한다.
#     # 1-0. 따라서 탐색을 끝마친공간을 노드의 수만큼 만들어준다.
#     visited=[]
#     visited=[False for _ in range(len(numbers))]
#     answer=0

#     탈출조건->
#     (방문을 해야하는 리스트)첫번째 숫자가 들어가면 해당숫자의 인덱스 값을 넘겨주고 (???,해당숫자 인덱스,방문한기록)
#     첫번째 숫자의 +,-의 값이 들어가게 되는거지 그걸 dfs로 실행시켜준다.
#     숫자가 배열의 길이만큼들어왓을때 탈출 할 것인지
#     if len(numbers)
#     숫자가 target의 넘버만큼 들어왔을때 탈출할것인지 or return할 것 인지
#     if len(visited) == len(numbers):

#     return answer


def solution(numbers, target):
    answer=0
    visited=[0]
    # need_visit==numbers

    while numbers:
        tmp=[]
        
        
        for i in visited:
            value=numbers.pop(0)
            tmp.append(i+(value+1))
            tmp.append(i+(value-1))
        visited=tmp
    return answer

print(solution([1, 1, 1, 1, 1],	3))