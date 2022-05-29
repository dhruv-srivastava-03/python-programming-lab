def factorial(num):
    temp = 1
    for i in range(1, num+1):
        temp *= i
    return temp


val = int(input("Enter the number you want to find the factorial of: "))
print(factorial(val))
