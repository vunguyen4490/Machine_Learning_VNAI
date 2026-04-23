"""
Ex4: print all Possible Combinations from the three Digits
data4 = [1, 2, 3]
"""

import math
data4 = [1, 2, 3]

for i in range(len(data4)):
    for j in range(len(data4)):
        if j!=i:
            for k in range(len(data4)):
                if k!=j and k!= i:
                    print(data4[i], data4[j], data4[k])
