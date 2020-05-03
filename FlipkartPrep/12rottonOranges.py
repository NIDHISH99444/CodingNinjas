from collections import deque
def update(step,i,j,queue):
    dy=[0,1,0,-1]
    dx=[-1,0,1,0]
    for s in range(len(dx)):
        if i+dx[s]<0 or i+dx[s]>=len(matrix) or j+dy[s]<0 or j+dy[s]>=len(matrix[0]) or matrix[i+dx[s]][j+dy[s]]==0 or matrix[i+dx[s]][j+dy[s]]==2:
            continue
        else:
            matrix[i+dx[s]][j+dy[s]]=2
            queue.append((step+1,i+dx[s],j+dy[s]))


def rottonOranges(matrix):
    queue=deque()
    step=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==2:
                queue.append((step,i,j))

    while queue:
        step,i,j=queue.popleft()
        update(step,i,j,queue)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==1:
                return -1
    return step


matrix=[[2,1,0,2,1],[1,0,1,2,1],[1,0,0,2,1]]
# matrix=[[2,1,1],[0,1,1],[1,0,1]]
# matrix= [[2,1,1],[1,1,0],[0,1,1]]
print(rottonOranges(matrix))