# Hướng Dẫn Viết File Markdown (.md)

> Markdown là ngôn ngữ định dạng văn bản đơn giản, dùng ký tự đặc biệt để tạo tiêu đề, danh sách, code...  
> Xem preview trong VS Code bằng cách nhấn **Ctrl + Shift + V**

---

## 1. Tiêu Đề

Dùng dấu `#` ở đầu dòng. Càng nhiều `#` thì chữ càng nhỏ.

```markdown
# Tiêu đề cấp 1 (lớn nhất)
## Tiêu đề cấp 2
### Tiêu đề cấp 3
#### Tiêu đề cấp 4
```

**Kết quả:** Giống như Heading 1, 2, 3, 4 trong Word.

---

## 2. Danh Sách Bullet

Dùng dấu `-` hoặc `*` ở đầu dòng.

```markdown
- Mục thứ nhất
- Mục thứ hai
- Mục thứ ba
```

Danh sách có thụt đầu dòng (nested):

```markdown
- Mục chính
  - Mục con
  - Mục con nữa
```

---

## 3. Danh Sách Có Số Thứ Tự

```markdown
1. Bước một
2. Bước hai
3. Bước ba
```

---

## 4. Code Ngắn (Inline Code)

Bọc trong dấu backtick `` ` `` (phím ở góc trên trái bàn phím, cạnh phím `1`).

```markdown
Dùng lệnh `git push` để đẩy lên GitHub
Nhấn `Ctrl + C` để dừng lệnh
Tạo file bằng `New-Item notes.md`
```

**Kết quả:** Chữ trong `` ` `` hiển thị nền xám, font code — dùng khi nhắc đến lệnh hoặc tên file trong câu văn.

---

## 5. Block Code (Nhiều Dòng)

Bọc trong 3 dấu backtick ` ``` `. Thêm tên ngôn ngữ ngay sau để tô màu cú pháp.

````markdown
```python
# Code Python
for x in data:
    print(x)
```

```powershell
# Lệnh PowerShell
git add .
git commit -m "message"
```

```markdown
# Markdown trong markdown
```
````

**Kết quả:** Hiển thị block code có màu sắc, dễ đọc. Hỗ trợ: `python`, `javascript`, `powershell`, `bash`, `html`, `css`...

---

## 6. Chữ Đậm và Nghiêng

```markdown
**chữ đậm** — bọc trong 2 dấu sao **
*chữ nghiêng* — bọc trong 1 dấu sao *
***đậm và nghiêng*** — bọc trong 3 dấu sao ***
~~gạch ngang~~ — bọc trong 2 dấu ngã ~~
```

---

## 7. Dòng Kẻ Ngang

Dùng `---` để tạo đường kẻ ngang phân cách các phần.

```markdown
Phần trên

---

Phần dưới
```

---

## 8. Trích Dẫn (Blockquote)

Dùng dấu `>` ở đầu dòng.

```markdown
> Đây là ghi chú quan trọng cần nhớ
> Có thể viết nhiều dòng
```

---

## 9. Link

```markdown
[Tên hiển thị](https://địa-chỉ-web.com)

Ví dụ:
[GitHub](https://github.com)
[Python Docs](https://docs.python.org)
```

---

## 10. Bảng

```markdown
| Cột 1 | Cột 2 | Cột 3 |
|-------|-------|-------|
| A     | B     | C     |
| D     | E     | F     |
```

---

## Tóm Tắt Nhanh

| Ký hiệu | Tác dụng |
|---------|----------|
| `#` `##` `###` | Tiêu đề cấp 1, 2, 3 |
| `-` hoặc `*` | Danh sách bullet |
| `1.` `2.` | Danh sách có số |
| `` `code` `` | Code ngắn inline |
| ` ```python ` | Block code nhiều dòng |
| `**chữ**` | Chữ **đậm** |
| `*chữ*` | Chữ *nghiêng* |
| `---` | Đường kẻ ngang |
| `> text` | Trích dẫn |
| `[text](url)` | Đường link |

---

> **Mẹo:** Nhấn `Ctrl + Shift + V` trong VS Code để xem preview file .md đẹp như trang web!
