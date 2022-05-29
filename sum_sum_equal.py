lst = list(map(int, input().split()))
left = 0
right = 0
temp = 0
for i in range(0, len(lst)):
    for j in range(0, i):
        left += lst[j]
    for k in range(i+1, len(lst)):
        right += lst[k]
if(left == right):
    temp = True
if(temp):
    print(True)
else:
    print(False)
