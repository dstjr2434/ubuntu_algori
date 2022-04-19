def dfs(graph,n,visited):
    # 1-1. 탐색시작노드를 스택에 삽입하고 방문처리를 한다.
    visited[n]=True
    for idx,value in enumerate(graph[n]):
        if value==1 and visited[idx]==False:
            dfs(graph,idx,visited)
    
    
def solution(n, computers):
    answer = 0
    # 1-0. dfs는 탐색을 해야하는 공간과 탐색을 끝마친 공간이 있어야한다.
    # 1-0. 따라서 탐색을 끝마친공간을 노드의 수만큼 만들어준다.
    visited=[False for _ in range(n)]
    
    #1-4. 2번과 3번과정이 반복되지 않을때까지 수행한다.
    for i in range(n):
        # 1-3. 방문하지 않은 인접노드가 없으면 스택에서 최상단노드를 꺼낸다.
        if visited[i]==False:
            dfs(computers,i,visited)
            answer+=1
    return answer

print(solution(3 ,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# 1-2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접노드를 스택에 넣고 방문처리를 한다.
