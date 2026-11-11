PHẦN 3: PHÂN TÍCH LÝ THUYẾT - PHƯƠNG PHÁP RUNGE - KUTTA BẬC 2 TỔNG QUÁT (RK2)
1. Cơ sở lý thuyết và Khai triển TaylorPhương pháp Runge - Kutta bậc 2 tổng quát (ký hiệu là rk2) là lớp phương pháp số một bước dùng để giải gần đúng bài toán Cauchy cho phương trình vi phân thông thường:
y' = f(x, y), y(a) = y0 trên đoạn [a, b]
Ý tưởng cốt lõi của phương pháp Runge - Kutta là xấp xỉ số gia của hàm nghiệm bằng cách tính giá trị của hàm vế phải f(x, y) tại một số điểm bên trong đoạn [xi, xi+1] mà không cần tính đạo hàm cấp cao của f(x, y) (khác với phương pháp khai triển Taylor trực tiếp)
Công thức tổng quát của Runge - Kutta bậc 2 có dạng:
yi+1 = yi + r1*K1 + r2*K2
Trong đó các hệ số gia tăng K1 và K2 được xác định theo Công thức (6.8) trong giáo trình:
K1 = hf(xi, yi)
K2 = hf(xi + alpha*h, yi + beta*K1)
2. Hệ điều kiện ràng buộc (Công thức 6.9)Để phương pháp đạt được độ chính xác bậc 2 (tức là sai số địa phương là O(h^3), sai số toàn cục là O(h^2), các tham số r1, r2, alpha, beta bắt buộc phải thỏa mãn hệ điều kiện ràng buộc (6.9) suy ra từ việc đồng nhất hệ số với khai triển Taylor bậc 2:
r1 + r2 = 1
r2*alpha = 1/2
r2*beta = 1/2
3. Chữ ký hàm chuẩn lập trình (Theo yêu cầu đồ án)
Hàm cài đặt trong module mã nguồn Python tuân thủ nghiêm ngặt chữ ký sau để phục vụ bộ kiểm thử chung:
def rk2(f, a, b, y0, n, r1, r2, alpha, beta) -> tuple[np.ndarray, np.ndarray]:
    """
    Phương pháp Runge-Kutta bậc 2 tổng quát (P3).
    Kiểm tra ràng buộc hệ số (6.9) và tính nghiệm trên lưới [a, b] chia thành n đoạn.
    """
    pass

PHẦN 4: PHÂN TÍCH LÝ THUYẾT - PHƯƠNG PHÁP ĐIỂM GIỮA VÀ RALSTON (THUỘC RK2)
1. Cơ sở lý thuyết chung
Cả hai phương pháp Điểm giữa (midpoint_ode) và Ralston (ralston) đều thuộc lớp phương pháp Runge - Kutta bậc 2 (RK2) dùng để giải gần đúng bài toán Cauchy cho phương trình vi phân thông thường:
Phương trình: y' = f(x, y), y(a) = y0 trên đoạn [a, b]
Công thức tổng quát của lớp phương pháp RK2 có dạng:
yi+1 = yi + r1*K1 + r2*K2
Trong đó các hệ số gia tăng K1 và K2 được tính theo công thức:
K1 = hf(xi, yi)
K2 = hf(xi + alpha*h, yi + beta*K1)
Để phương pháp đạt độ chính xác bậc 2 (sai số địa phương O(h^3)), bộ tham số phải thỏa mãn hệ điều kiện ràng buộc:
r1 + r2 = 1
r2*alpha = 1/2
r2*beta = 1/2
2. Chi tiết hai trường hợp riêng trong Nhiệm vụ P4
2.1. Phương pháp Điểm giữa (midpoint_ode)
Bộ hệ số lựa chọn: alpha = 1/2, beta = 1/2, r1 = 0, r2 = 1
Ý nghĩa: Phương pháp tính giá trị đạo hàm tại điểm giữa của bước lưới để tăng độ chính xác so với phương pháp Euler thuần túy
Công thức triển khai trong code:
K1 = hf(xi, yi)
K2 = hf(xi + 0.5h, yi + 0.5K1)
yi+1 = yi + K2
2.2. Phương pháp Ralston (ralston)
Bộ hệ số lựa chọn: alpha = 3/4, beta = 3/4, r1 = 1/3, r2 = 2/3
Ý nghĩa: Đây là bộ hệ số được tối ưu hóa đặc biệt nhằm giảm thiểu tối đa hằng số chặn của sai số cận trên trong lớp phương pháp Runge - Kutta bậc 2
Công thức triển khai trong code:
K1 = hf(xi, yi)
K2 = hf(xi + 0.75h, yi + 0.75K1)
yi+1 = yi + (1/3)K1 + (2/3)K2
3. Chữ ký hàm chuẩn lập trình (Theo yêu cầu đồ án)
Các hàm cài đặt trong module mã nguồn Python tuân thủ nghiêm ngặt chữ ký sau để phục vụ bộ kiểm thử chung:
def midpoint_ode(f, a, b, y0, n) -> tuple[np.ndarray, np.ndarray]:
    """Phương pháp Điểm giữa (Midpoint method)."""
    pass

def ralston(f, a, b, y0, n) -> tuple[np.ndarray, np.ndarray]:
    """Phương pháp Ralston."""
    pass
