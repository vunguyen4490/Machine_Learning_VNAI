# 1. NOTES ÔN TẬP PYTHON
## 1.1 List

### Kiến thức cần nắm

**1. List cơ bản**
- Tạo list và truy cập phần tử theo index

```python
data = [1, 2, 3]
print(data[0])  # lấy phần tử đầu tiên → 1
print(data[-1]) # lấy phần tử cuối → 3
```

**2. Duyệt list — vòng lặp for**

```python
for x in data:
    print(x)
```

**3. Điều kiện — if/elif/else**

```python
if x > 0:
    # số dương
elif x < 0:
    # số âm
else:
    # số 0
```

**4. Biến đếm / tích lũy**

```python
count = 0   # đếm số lượng
total = 0   # tính tổng

for x in data:
    count += 1
    total += x
```

---

> Nắm 4 thứ này là làm được: đếm, tính tổng, tìm max/min, lọc phần tử

**5. Duyệt list theo index**

Dùng khi cần truy cập 2 phần tử liền kề cùng lúc.

```python
# range(len(data)) → tạo dãy số 0, 1, 2, ... đến hết list
for i in range(len(data)):
    print(data[i])   # truy cập theo vị trí

# range(len(data) - 1) → dừng trước phần tử cuối
# (tránh lỗi khi lấy data[i+1])
for i in range(len(data) - 1):
    print(data[i], data[i + 1])   # 2 phần tử liền kề
```

**6. List lồng nhau (Nested List)**

List mà mỗi phần tử bên trong cũng là 1 list.

```python
# Tạo nested list
matrix = [[4, 3, 5],
          [1, 2, 3],
          [3, 7, 4]]

# Truy cập hàng
matrix[0]      # → [4, 3, 5]  (hàng 0)
matrix[1]      # → [1, 2, 3]  (hàng 1)

# Truy cập từng phần tử
matrix[0][0]   # → 4  (hàng 0, cột 0)
matrix[0][1]   # → 3  (hàng 0, cột 1)
matrix[1][2]   # → 3  (hàng 1, cột 2)

# Duyệt nested list
for row in matrix:
    print(row)         # in từng hàng

for row in matrix:
    for x in row:
        print(x)       # in từng phần tử
```

---

> **Nhớ:** `matrix[i]` → lấy hàng, `matrix[i][j]` → lấy phần tử cụ thể

## 1.2 Dictionary

Dictionary = **cuốn sổ tra cứu**, lưu dữ liệu dạng **key: value** (tên: giá trị), dùng `{}`.

**Tạo dictionary**

```python
# Rỗng
d = {}

# Có sẵn dữ liệu
hoc_sinh = {"ten": "An", "tuoi": 16, "lop": "10A1"}
diem = {"Toan": 9, "Van": 8}
freq = {4: 3, 6: 1}
```

**Truy cập theo key**

```python
print(hoc_sinh["ten"])   # → An
print(diem["Toan"])      # → 9
```

**Thêm / cập nhật giá trị**

```python
d["ten"] = "Binh"   # thêm mới
d["tuoi"] += 1      # cập nhật
```

**Kiểm tra key có tồn tại không**

```python
if "ten" in d:
    d["ten"] += 1
else:
    d["ten"] = 1
```

**Duyệt dictionary**

```python
for key, value in d.items():
    print(key, value)
```

---

> **List vs Dictionary**
> - `[]` List → lấy theo **số thứ tự** (index): `data[0]`
> - `{}` Dictionary → lấy theo **tên** (key): `d["ten"]`

> **Dùng khi nào:** Cần gắn tên (key) cho từng giá trị.  
> Ví dụ: thông tin học sinh, điểm môn học, đếm tần suất...