# Quy ước mã nguồn - Nhóm 7 (Euler và họ RK2)

## 1. File và thư mục
- `src/euler_heun.py`: hàm `euler`, `euler_improved`
- `src/p4.py`: hàm `rk2`, `midpoint_ode`, `ralston`
- `test/`: các file kiểm thử pytest, tên dạng `test_<tên>.py`
- `application/`: bài toán ứng dụng (logistic)
- `experiments/`: thực nghiệm so sánh
- `report/`: báo cáo, slide, tài liệu
- Mỗi người chỉ sửa file thuộc phần mình.

## 2. Chữ ký hàm (đúng như đề, không đổi)
- `euler(f, a, b, y0, n)`
- `euler_improved(f, a, b, y0, n)`
- `rk2(f, a, b, y0, n, r1, r2, alpha, beta)`
- `midpoint_ode(f, a, b, y0, n)`
- `ralston(f, a, b, y0, n)`
Cả năm hàm trả về `(xs, ys)`, hai mảng numpy.

## 3. Quy ước chung
- `n` là số bước, bước chia h = (b - a) / n.
- `xs` và `ys` đều có n + 1 phần tử, `xs[0] = a`, `xs[-1] = b`, `ys[0] = y0`.
- Hàm vế phải được gọi dạng `f(x, y)` (theo bài giảng).
- Trong `src/` chỉ dùng numpy, không dùng scipy.
- So sánh số thực bằng dung sai, không dùng dấu `==`.

## 4. Kiểm tra đầu vào (R6)
Báo `ValueError` với thông điệp rõ ràng khi:
- `n` không phải số nguyên dương,
- `a >= b`,
- `f` không gọi được,
- `rk2` có tham số vi phạm ràng buộc (6.9).

## 5. Docstring (R5)
Mỗi hàm có: mô tả; tham số (Require); giá trị trả về (Ensure);
tên và số thuật toán trong bài giảng.

## 6. Chú thích (R2)
Mỗi khối lệnh có comment dạng `# dong X - Thuat toan Y`.

## 7. Git
- Commit bằng tài khoản của chính mình.
- Lời nhắn cụ thể (ví dụ "Cài đặt euler theo Thuat toan 17").
- `git pull` trước khi bắt đầu làm và trước khi push.

## 8. Kiểm thử (R7)
Chạy `pytest` từ thư mục gốc. Mỗi thuật toán có ít nhất 3 ca:
ví dụ bài giảng, ví dụ có nghiệm đúng, ca biên.
