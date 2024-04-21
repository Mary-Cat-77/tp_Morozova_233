n = int(input())
string = input().split()
count = 0
x = 0
s = 'YES'
listik = []
for i in range(len(string) - 1):
    for j in range(len(string) - i - 1):
        if int(string[j]) > int(string[j + 1]):
            count += 1
            x = string[j]
            listik.append(j)
            string[j] = string[j + 1]
            string[j + 1] = x
        if j in listik:
            s = 'NO'
            break
print(s)