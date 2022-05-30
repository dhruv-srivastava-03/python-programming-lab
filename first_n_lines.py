a = open(f"stry.txt", 'r')
n = int(input())
for i in n:
    out = a.readline()
    print(out)
a.close()
