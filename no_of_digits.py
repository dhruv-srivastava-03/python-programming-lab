a = int(input("enter the number whose digit you want to know: "))
temp = 0
while(a):
    temp += 1
    a = a//10
print(temp)
