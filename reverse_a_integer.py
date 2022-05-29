a = int(input("Enter the integer you want to reverse: "))
reverse = 0
temp = 0
while a:
    temp = a % 10
    reverse = (reverse*10) + temp
    a = a//10
print(reverse)
