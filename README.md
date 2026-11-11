# Nhóm 7 - Phương trình vi phân: Euler và họ Runge-Kutta bậc 2

Bài tập lớn môn **Phương pháp số** (Chương 6)
Lớp: `<lớp>` | Giảng viên: `<tên giảng viên>` | Học kỳ: `<học kỳ>`

Repo này cài đặt, kiểm thử và so sánh các phương pháp giải bài toán Cauchy
y' = f(x, y), y(a) = y0 trên đoạn [a, b]: **Euler**, **Euler cải tiến (Heun)**,
**Runge-Kutta bậc 2 tổng quát (RK2)** và hai trường hợp riêng của RK2 là
**điểm giữa** và **Ralston**. Các phương pháp được áp dụng vào mô hình tăng trưởng logistic.

## 1. Thành viên và phân công

| Họ tên | MSSV | GitHub | Phân công ban đầu | Đóng góp thực tế |
|---|---|---|---|---|
| Phan Thị Hương Giang | `<mssv>` | `<tài khoản>` | Euler, Euler cải tiến | `<file, commit>` |
| Lê Đức Anh | `<mssv>` | `<tài khoản>` | RK2, điểm giữa, Ralston | `<file, commit>` |
| Nguyễn Việt Dũng | `<mssv>` | `<tài khoản>` | Bài toán ứng dụng | `<file, commit>` |
| Phạm Trung Hiếu | `<mssv>` | `<tài khoản>` | Kiểm thử cho cả nhóm, kiểm thử chéo cho nhóm cặp đôi | `<file, commit>` |
| Triệu Minh Hoàng | `<mssv>` | `<tài khoản>` | Tạo repo, chuẩn mã, tích hợp, README, báo cáo, slide | `CONVENTIONS.md`, `README.md`, tích hợp repo, `<báo cáo, slide>` |
| Nguyễn Đức Trường | `<mssv>` | `<tài khoản>` | Thực nghiệm so sánh, nhận xét | `<file, commit>` |
| Vũ Minh Thành | `<mssv>` | `<tài khoản>` | Không tham gia (theo bảng phân công của nhóm) | - |

Mỗi thành viên commit bằng tài khoản GitHub của chính mình. Mọi thay đổi so với phân công ban đầu (nếu có): `<ghi rõ>`.

## 2. Cấu trúc thư mục

```
.
├── src/
│   ├── euler_heun.py      # euler, euler_improved
│   └── p4.py              # rk2, midpoint_ode, ralston
├── test/                  # kiểm thử pytest
├── experiments/           # thực nghiệm so sánh
├── application/           # bài toán ứng dụng (logistic)
├── report/                # báo cáo, slide, tài liệu
├── CONVENTIONS.md         # quy ước mã nguồn của nhóm
├── requirements.txt
└── README.md
```

## 3. Cài đặt và chạy (Windows)

Yêu cầu Python 3.10 trở lên (kiểm tra bằng `python --version`).
Mở Command Prompt tại thư mục gốc của repo rồi chạy:

```
pip install -r requirements.txt
pytest
```

Chạy thực nghiệm và bài ứng dụng (từ thư mục gốc):

```
python experiments/<tên file>.py
python application/<tên file>.py
```

Kết quả (bảng, đồ thị) được lưu tại `<thư mục kết quả>`.

## 4. Các thuật toán đã cài đặt

| Phương pháp | Hàm | File | Cơ sở trong bài giảng |
|---|---|---|---|
| Euler | `euler` | `src/euler_heun.py` | Thuật toán 17 |
| Euler cải tiến (Heun) | `euler_improved` | `src/euler_heun.py` | Thuật toán 18 |
| RK2 tổng quát | `rk2` | `src/p4.py` | Công thức (6.8), ràng buộc (6.9) |
| Điểm giữa | `midpoint_ode` | `src/p4.py` | RK2 với r1 = 0, r2 = 1, α = β = 1/2 |
| Ralston | `ralston` | `src/p4.py` | RK2 với r1 = 1/3, r2 = 2/3, α = β = 3/4 |

Chữ ký chung: `hàm(f, a, b, y0, n)` (riêng `rk2` có thêm `r1, r2, alpha, beta`).
Giá trị trả về là `(xs, ys)`, hai mảng numpy có n + 1 phần tử, bước chia h = (b - a) / n.
Hàm vế phải được gọi dạng `f(x, y)`. Chi tiết quy ước xem `CONVENTIONS.md`.

## 5. Ví dụ nhanh

Chạy từ thư mục gốc của repo. Bài toán y' = y - x² + 1, y(0) = 0,5 trên [0; 2], h = 0,2 (n = 10):

```python
from src.euler_heun import euler

xs, ys = euler(lambda x, y: y - x**2 + 1, 0, 2, 0.5, 10)
print(ys[-1])  # xấp xỉ 4.865785
```

## 6. Kiểm thử

Chạy bằng lệnh `pytest`. Mỗi thuật toán có ít nhất 3 ca: ví dụ trong bài giảng, ví dụ có nghiệm đúng, ca biên.
Các ca bắt buộc theo đề (dung sai khoảng 1e-6 vì đề làm tròn 6 chữ số):

| Ca | Kết quả mong đợi |
|---|---|
| y' = y - x² + 1, y(0) = 0,5, [0; 2], h = 0,2: Euler | y10 = 4,865785 |
| Cùng bài: Euler cải tiến | 5,233055 |
| Cùng bài: điểm giữa | 5,290369 |
| Cùng bài: nghiệm đúng | y(2) = 5,305472 |
| y' = 3x²y, y(0) = 1, [0; 1], n = 5: Euler cải tiến | y5 = 2,700507 |
| `rk2` với tham số vi phạm (6.9) | báo lỗi |
| `rk2` với r1 = r2 = 1/2, α = β = 1 | trùng `euler_improved` |

Ngoài ra kiểm thử đầu vào (n không nguyên dương, a >= b, f không gọi được) theo yêu cầu R6.

## 7. Thực nghiệm so sánh

Với h = 0,4; 0,2; 0,1; 0,05; 0,025, vẽ sai số tại x = 2 của bốn phương pháp theo h (thang log-log),
kiểm chứng Euler có bậc 1 và các công thức thuộc RK2 có bậc 2, so sánh hằng số sai số giữa
Euler cải tiến, điểm giữa và Ralston.

Kết quả chính: `<tóm tắt 2-3 dòng: độ dốc đo được, phương pháp có hằng số sai số nhỏ nhất>`.
Chi tiết: `report/<tên file báo cáo thực nghiệm>`.

## 8. Bài toán ứng dụng: mô hình tăng trưởng logistic

Số phương tiện đăng ký P(t) (triệu xe) tại một thành phố thỏa
P' = r·P·(1 - P/K), P(0) = 1, r = 0,3, K = 10, 0 <= t <= 20 (năm),
có nghiệm đúng P(t) = K / (1 + (K/P0 - 1)·e^(-r·t)).

Nhóm giải bằng bốn phương pháp với h = 1 và h = 0,5, xác định năm P vượt 8 triệu xe
(theo nghiệm đúng, t xấp xỉ 11,95 năm), và thử h = 5, h = 8 với Euler để quan sát và giải thích hiện tượng.

Kết quả chính: `<tóm tắt: năm P vượt 8 triệu theo từng phương pháp, nhận xét về h = 5 và h = 8>`.
Chi tiết: `report/<tên file báo cáo ứng dụng>`, hình: `application/logistic_application_sv7.png`.

## 9. Đối chiếu yêu cầu của đề

Đánh dấu `[x]` sau khi đã tự kiểm tra từng mục.

- [ ] R1: Python 3.10+, chỉ dùng numpy, matplotlib, pytest (scipy chỉ dùng để lấy nghiệm đối chiếu nếu có)
- [ ] R2: mỗi khối lệnh có chú thích dạng `# dong X - Thuat toan Y`
- [ ] R3: hàm thuật toán không gọi `scipy.integrate`, `numpy.linalg.solve` hay hàm có sẵn tương tự
- [ ] R4: chữ ký hàm đúng như đề
- [ ] R5: mọi hàm có docstring (mô tả, Require, Ensure, tên thuật toán)
- [ ] R6: kiểm tra đầu vào và báo lỗi rõ ràng (n, a < b, f, ràng buộc 6.9)
- [ ] R7: mỗi thuật toán có ít nhất 3 ca kiểm thử, toàn bộ chạy qua `pytest`

## 10. Sử dụng AI và nguồn tham khảo

**Sử dụng AI** (theo mục 1.8 của đề):
- Triệu Minh Hoàng: dùng Claude (Anthropic) để hướng dẫn thao tác Git/GitHub, gợi ý cấu trúc repo, soạn bản nháp `CONVENTIONS.md` và `README.md`, lập danh sách kiểm tra tích hợp. Nội dung đã được đọc lại và đối chiếu với đề, bài giảng: `<xác nhận hoặc chỉnh lại cho đúng thực tế>`.
- Phạm Trung Hiếu : 
- Các thành viên khác: `<mỗi người tự ghi: có dùng AI hay không, vào việc gì>`.

**Tài liệu tham khảo:**
- Bài giảng môn Phương pháp số, Chương 6 (Thuật toán 17, 18, công thức 6.8, 6.9).
- Đề bài tập lớn và bài toán ứng dụng do giảng viên cung cấp.
- `<tài liệu khác nếu có, ghi rõ nguồn>`

## 11. Sản phẩm nộp

- Báo cáo PDF: `report/<tên file>.pdf`
- Slide thuyết trình: `report/<tên file>`
- Biên bản phản biện chéo: `report/<tên file>`
