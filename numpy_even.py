import numpy as np
lst = []
for i in range(2, 101, 2):
    lst.append(i)
arr = np.array(lst, int)
print(arr)
