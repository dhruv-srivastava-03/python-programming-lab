str1 = input().split()
temp = []
s = ""
for i in range(0, len(str1)):
    temp.append(str1[i][::-1])
for i in temp:
    s += i + " "
print(s)
