import numpy as np
arr = np.array([1, 2, 3, 4])
for i in arr:
    if(i > 100):
        print("Number greater than hundred detected!!")
        break
    