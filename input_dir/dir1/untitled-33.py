def dfs(start):
    global flag
    flag = 0
   
    visited[start] = 1
    for i in range(n):
        print(listik[start][i])
        if listik[start][i]:
            if visited[i] == 1:
                flag = 1
            elif visited[i] == 0:
                dfs(i)
    visited[start] == 2
    

n = int(input())
listik = []
flag = 0
visited = [0] * n
for i in range(n):
    string = list(map(int, input().split()))
    listik.append(string)
for i in range(n):
    if visited[i] == 0:
        dfs(i)
print(flag)