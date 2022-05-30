a = open(f"stry.txt", 'r')
n = int(input())
print(a.readlines()[-n:])
a.close()
