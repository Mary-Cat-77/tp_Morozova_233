n = int(input())
listik = []
x = 0
for i in range(n):
    string = input().split()
    listik.append(string)
for i in range(0, len(listik) - 1):
    for j in range(0, len(listik) - i - 1):
    
        if listik[j][1] < listik[j + 1][1]:
            x = listik[j]
            listik[j] = listik[j + 1]
            listik[j + 1] = x
        elif listik[j][1] == listik[j + 1][1]:
            if listik[j][0] > listik[j + 1][0]:
                x = listik[j]
                listik[j] = listik[j + 1]
                listik[j + 1] = x            
for i in range(len(listik)):
    print(*listik[i])