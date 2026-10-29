# Nội dung báo cáo — P1 và P2

## P1. Phương pháp Euler (Thuật toán 16)

Xét bài toán Cauchy
\[
y'=f(x,y),\qquad y(a)=y_0,\qquad x\in[a,b].
\]
Chia đoạn \([a,b]\) thành \(n\) bước đều, với \(h=(b-a)/n\). Phương pháp Euler hiện tính lần lượt:
\[
x_i=a+ih,\qquad
y_i=y_{i-1}+h f(x_{i-1},y_{i-1}),\quad i=1,\ldots,n.
\]
Hàm Python `euler(f, a, b, y0, n)` trả về hai mảng NumPy `(xs, ys)`, mỗi mảng có \(n+1\) phần tử. `xs` lưu các nút lưới và `ys` lưu nghiệm xấp xỉ tương ứng.

## P2. Phương pháp Euler cải tiến (Thuật toán 17)

Phương pháp Euler cải tiến dùng bước dự đoán theo Euler rồi hiệu chỉnh bằng trung bình hai hệ số góc. Với \(h=(b-a)/n\):
\[
\widetilde y_i=y_{i-1}+h f(x_{i-1},y_{i-1}),
\]
\[
y_i=y_{i-1}+\frac h2\left[
f(x_{i-1},y_{i-1})+f(x_i,\widetilde y_i)
\right].
\]
Hàm Python `euler_improved(f, a, b, y0, n)` cũng trả về `(xs, ys)` dưới dạng hai mảng NumPy có \(n+1\) phần tử.

## Kiểm tra dữ liệu và xử lý trường hợp biên

Cả hai hàm kiểm tra `f` có thể gọi được, `n` là số nguyên dương, các dữ liệu số hữu hạn và \(b>a\). Trong quá trình tính, nếu \(f(x,y)\), giá trị dự đoán hoặc nghiệm xấp xỉ không hữu hạn, chương trình phát sinh `ValueError` với thông báo cụ thể. Các điều kiện này phù hợp với bài toán giải gần đúng phương trình vi phân; điều kiện đổi dấu \(f(a)f(b)<0\) không áp dụng cho bài toán Cauchy tổng quát.

## Ví dụ minh họa và kiểm thử

Sử dụng Ví dụ 6.2 trong tài liệu:
\[
y'=y+\frac{e^x}{x},\qquad y(1)=e,\qquad x\in[1,2],
\]
có nghiệm chính xác
\[
y(x)=e^x(1+\ln|x|).
\]
Ví dụ này được dùng để chạy thử hai hàm và so sánh với nghiệm chính xác. Bộ kiểm thử `test_euler_methods.py` còn kiểm tra bài toán \(y'=1,\ y(0)=2\), trường hợp `n=0`, và trường hợp hàm vế phải trả về `NaN`. Chạy toàn bộ kiểm thử bằng `python -m pytest -v`.
