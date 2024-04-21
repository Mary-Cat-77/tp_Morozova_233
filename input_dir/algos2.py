n = int(input())
string = input().split()
count = 0
x = 0
for i in range(len(string) - 1):
    for j in range(len(string) - i - 1):
        if int(string[j]) > int(string[j + 1]):
            count += 1
            x = string[j]
            string[j] = string[j + 1]
            string[j + 1] = x
string = sorted(set(string), key=lambda d: string.index(d))
if len(string) < 3:
    print(-1)
else:
    print(string[-3])