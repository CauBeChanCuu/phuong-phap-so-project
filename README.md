# DỰ ÁN PHƯƠNG PHÁP SỐ – NHÓM 7

## 1. Giới thiệu

Dự án được thực hiện nhằm cài đặt, kiểm thử và đánh giá các phương pháp số sử dụng để giải gần đúng phương trình vi phân thường bằng ngôn ngữ lập trình Python.

Dự án tập trung vào phương pháp Euler, Euler cải tiến và các phương pháp Runge–Kutta bậc 2. Các thành viên phối hợp thực hiện mã nguồn, kiểm thử, thực nghiệm và xây dựng báo cáo.

## 2. Mục tiêu

- Cài đặt các phương pháp số bằng Python.
- Tổ chức mã nguồn thành các tệp riêng biệt, dễ đọc và dễ quản lý.
- Kiểm thử chương trình nhằm phát hiện lỗi và đánh giá kết quả.
- Thực nghiệm, so sánh và nhận xét về các phương pháp số.
- Tích hợp mã nguồn và tài liệu của các thành viên thành một sản phẩm thống nhất.
- Hoàn thiện báo cáo và slide thuyết trình.

## 3. Cấu trúc dự án

| Tệp | Chức năng |
|---|---|
| `euler_methods.py` | Cài đặt phương pháp Euler và Euler cải tiến. |
| `test_euler_methods.py` | Kiểm thử các phương pháp Euler. |
| `p4.py` | Cài đặt phương pháp Midpoint và Ralston. |
| `test.py` | Kiểm thử các phương pháp trong `p4.py`. |
| `report_section.md` | Báo cáo về các phương pháp Euler. |
| `Báo cáo Phân tích Lý thuyết P4.md` | Tài liệu phân tích lý thuyết phần P4. |
| `.gitignore` | Quy định các tệp và thư mục không đưa vào Git. |
| `README.md` | Giới thiệu dự án, cấu trúc và hướng dẫn sử dụng. |

## 4. Công nghệ sử dụng

- **Ngôn ngữ lập trình:** Python.
- **Thư viện tính toán:** NumPy.
- **Thư viện kiểm thử:** pytest.
- **Môi trường phát triển:** Visual Studio Code.
- **Quản lý mã nguồn:** GitHub và GitHub Desktop.

## 5. Yêu cầu cài đặt

Cài đặt Python 3 và các thư viện cần thiết.

Mở Terminal tại thư mục dự án và chạy:

```bash
python -m pip install numpy pytest
```

Kiểm tra phiên bản Python:

```bash
python --version
```

## 6. Hướng dẫn chạy chương trình

### 6.1. Chạy chương trình Euler

```bash
python euler_methods.py
```

### 6.2. Chạy chương trình Midpoint và Ralston

```bash
python p4.py
```

### 6.3. Kiểm thử các phương pháp Euler

```bash
python -m pytest -v test_euler_methods.py
```

### 6.4. Kiểm thử các phương pháp trong P4

```bash
python -m pytest -v test.py
```

Các lệnh chạy chương trình áp dụng khi tệp tương ứng có phần thực thi phù hợp. Kết quả cần được xác nhận bằng cách chạy trực tiếp trên môi trường thực tế.

## 7. Nội dung chuyên môn

### 7.1. Phương pháp Euler

Phương pháp Euler được sử dụng để tính gần đúng nghiệm của phương trình vi phân thường. Nội dung cài đặt và kiểm thử được tổ chức trong các tệp liên quan.

### 7.2. Phương pháp Euler cải tiến

Phương pháp Euler cải tiến được triển khai nhằm nâng cao độ chính xác của kết quả xấp xỉ so với phương pháp Euler cơ bản trong những điều kiện phù hợp.

### 7.3. Phương pháp Midpoint

Phương pháp Midpoint là một phương pháp Runge–Kutta bậc 2, sử dụng thông tin tại điểm giữa của bước tính để xấp xỉ nghiệm.

### 7.4. Phương pháp Ralston

Phương pháp Ralston là một phương pháp Runge–Kutta bậc 2 khác, được triển khai và kiểm thử trong phần mã nguồn tương ứng.

## 8. Kiểm thử và đánh giá

Dự án sử dụng pytest để tổ chức và thực hiện kiểm thử.

Các nội dung kiểm thử bao gồm:

- Kiểm tra kết quả tính toán.
- Kiểm tra cấu trúc và số lượng phần tử của dữ liệu đầu ra.
- Kiểm tra cách xử lý đầu vào không hợp lệ.
- Chạy lại các
