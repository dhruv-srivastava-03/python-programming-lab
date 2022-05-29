lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
dict1 = {}
for i in range(0, len(lst1)):
    dict1[lst1[i]] = lst2[i]
print(dict1)
