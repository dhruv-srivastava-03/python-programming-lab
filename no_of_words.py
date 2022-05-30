a = open(f"stry.txt", 'r')
out = a.read()
print(len(out.split()))
a.close()
