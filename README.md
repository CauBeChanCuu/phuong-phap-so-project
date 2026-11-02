# DỰ ÁN PHƯƠNG PHÁP SỐ

## 1. Giới thiệu

Dự án được xây dựng nhằm cài đặt và minh họa một số phương pháp số dùng để giải gần đúng các bài toán toán học bằng Python.

Nội dung tập trung vào các phương pháp Euler, Euler cải tiến và một số phương pháp Runge–Kutta bậc 2.

## 2. Mục tiêu

- Cài đặt các thuật toán bằng Python.
- Tổ chức chương trình thành các tệp mã nguồn riêng biệt.
- Kiểm tra chương trình bằng các ví dụ và bộ kiểm thử.
- Tổng hợp lý thuyết, công thức và hướng dẫn sử dụng.

## 3. Cấu trúc dự án

- `euler_methods.py`: Cài đặt phương pháp Euler và Euler cải tiến.
- `test_euler_methods.py`: Các bài kiểm thử cho những phương pháp Euler.
- `p4.py`: Cài đặt phương pháp điểm giữa (Midpoint) và Ralston.
- `test.py`: Tệp kiểm tra các phương pháp trong `p4.py`.
- `report_section.md`: Nội dung báo cáo về các phương pháp Euler.
- `Báo cáo Phân tích Lý thuyết P4.md`: Tài liệu lý thuyết của phần P4.
- `.gitignore`: Quy định những tệp không đưa lên Git.

## 4. Yêu cầu môi trường

- Python 3.
- Thư viện NumPy nếu được sử dụng trong mã nguồn.
- Thư viện pytest để chạy kiểm thử bằng pytest.

Cài đặt các thư viện cần thiết bằng lệnh:

```bash
python -m pip install numpy pytest
```

## 5. Cách chạy chương trình

Mở Terminal tại thư mục gốc của dự án.

Chạy các phương pháp Euler:

```bash
python euler_methods.py
```

Chạy các phương pháp Midpoint và Ralston:

```bash
python p4.py
```

Chạy bộ kiểm thử Euler:

```bash
python -m pytest -q test_euler_methods.py
```

Chạy kiểm thử các phương pháp P4:

```bash
python test.py
```

Lưu ý: Các lệnh trên cần được kiểm tra với mã nguồn thực tế của dự án. Không kết luận chương trình chạy đúng cho đến khi đã chạy thử thành công.

## 6. Các phương pháp số

### 6.1. Phương pháp Euler

Công thức:

\[
y_{i+1}=y_i+h f(x_i,y_i)
\]

Trong đó \(h\) là bước lưới.

### 6.2. Phương pháp Euler cải tiến

Phương pháp sử dụng thông tin tại điểm đầu và giá trị dự đoán tại điểm tiếp theo để cải thiện kết quả gần đúng.

### 6.3. Phương pháp điểm giữa (Midpoint)

\[
k_1=h f(x_i,y_i)
\]

\[
k_2=h f\left(x_i+\frac{h}{2},y_i+\frac{k_1}{2}\right)
\]

\[
y_{i+1}=y_i+k_2
\]

### 6.4. Phương pháp Ralston

\[
k_1=h f(x_i,y_i)
\]

\[
k_2=h f\left(x_i+\frac{3h}{4},y_i+\frac{3k_1}{4}\right)
\]

\[
y_{i+1}=y_i+\frac{1}{3}k_1+\frac{2}{3}k_2
\]

## 7. Kiểm thử và đánh giá

Các bộ kiểm thử được sử dụng để kiểm tra kết quả tính toán, cách xử lý dữ liệu đầu vào và hoạt động của các phương pháp số.

Kết quả kiểm thử sẽ được cập nhật sau khi chạy chương trình và xử lý các lỗi phát sinh.

## 8. Kết luận

Dự án giúp minh họa cách áp dụng Python để triển khai các phương pháp số, đồng thời rèn luyện kỹ năng tổ chức mã nguồn, kiểm thử và viết tài liệu kỹ thuật.
