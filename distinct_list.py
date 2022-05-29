lst = list(map(int, input().split()))
distinct = []
for i in lst:
    if i not in distinct:
        distinct.append(i)

print(distinct)
