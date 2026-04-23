"""
Ex2: Given a list, extract all elements whose frequency is greater than k.
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

Step 1: Tạo dictionary đếm tần suất
         → Duyệt list, mỗi số xuất hiện thì tăng đếm lên 1

Step 2: Lọc những số có tần suất > k
         → Duyệt dictionary, so sánh value với k

Step 3: In kết quả
"""

import math
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
d = {}
for x in data2:
    if x in d:
        d[x] +=1
    else:
        d[x]=1 

result = []
for key, value in d.items():
    if value > 3:
        result.append(key)
print(result)


