"""
P1 và P2: Phương pháp Euler và Euler cải tiến (Heun)
Giải bài toán Cauchy: y' = f(x, y), y(a) = y0 trên [a, b].

Quy ước:
- Đầu vào: hàm f(x, y), hai đầu mút a < b, giá trị đầu y0, số bước n > 0.
- Đầu ra: hai mảng xs, ys; xs là các nút lưới, ys là nghiệm xấp xỉ tương ứng.
- P1: Euler
- P2: Euler cải tiến (Heun).
"""

import numpy as np


def _validate_inputs(f, a, b, y0, n):
    """Kiểm tra đầu vào dùng chung cho hai phương pháp."""
    # Pseudocode chung - Bước 1: Kiểm tra f có thể gọi được và n là số nguyên dương.
    if not callable(f):
        raise TypeError("f phải là một hàm có thể gọi được.")
    if isinstance(n, bool) or not isinstance(n, (int, np.integer)):
        raise TypeError("n phải là một số nguyên dương.")
    if n <= 0:
        raise ValueError("n phải lớn hơn 0.")

    # Pseudocode chung - Bước 2: Chuyển a, b, y0 sang kiểu số thực và kiểm tra hữu hạn.
    try:
        a, b, y0 = float(a), float(b), float(y0)
    except (TypeError, ValueError) as exc:
        raise TypeError("a, b và y0 phải là các giá trị số.") from exc

    if not np.all(np.isfinite([a, b, y0])):
        raise ValueError("a, b và y0 phải là các giá trị hữu hạn.")
    if b <= a:
        raise ValueError("Cần có b > a để tính trên đoạn [a, b].")

    # Pseudocode chung - Bước 3: Trả về dữ liệu đầu vào hợp lệ.
    return a, b, y0, int(n)


def _evaluate(f, x, y):
    """Tính f(x, y) và báo lỗi nếu kết quả không hữu hạn."""
    # Pseudocode chung - Bước 4: Tính hệ số góc f(x, y).
    try:
        value = float(f(x, y))
    except Exception as exc:
        raise ValueError(f"Không tính được f(x, y) tại x={x!r}, y={y!r}.") from exc

    # Pseudocode chung - Bước 5: Kiểm tra hệ số góc có hữu hạn hay không.
    if not np.isfinite(value):
        raise ValueError(f"f(x, y) không hữu hạn tại x={x!r}, y={y!r}.")
    return value


def euler(f, a, b, y0, n):
    """
    P1 - Phương pháp Euler .

    Pseudocode:
    1. Kiểm tra đầu vào.
    2. Tính h = (b - a) / n.
    3. Tạo các nút x_i = a + i*h; đặt y_0 = giá trị đầu.
    4. Với i = 1, ..., n:
           y_i = y_(i-1) + h*f(x_(i-1), y_(i-1)).
    5. Trả về các mảng x và y.
    """
    # Pseudocode bước 1: Kiểm tra đầu vào.
    a, b, y0, n = _validate_inputs(f, a, b, y0, n)

    # Pseudocode bước 2: Tính độ dài mỗi bước lưới.
    h = (b - a) / n

    # Pseudocode bước 3: Tạo n+1 nút từ a đến b và mảng chứa nghiệm xấp xỉ.
    xs = np.linspace(a, b, n + 1, dtype=float)
    ys = np.empty(n + 1, dtype=float)

    # Pseudocode bước 3: Gán điều kiện đầu y(a) = y0.
    ys[0] = y0

    # Pseudocode bước 4: Lặp qua từng bước để tính nghiệm kế tiếp.
    for i in range(1, n + 1):
        # Tính hệ số góc tại điểm trước (x_(i-1), y_(i-1)).
        slope = _evaluate(f, float(xs[i - 1]), float(ys[i - 1]))

        # Công thức Euler: y_i = y_(i-1) + h*f(x_(i-1), y_(i-1)).
        ys[i] = ys[i - 1] + h * slope

        # Kiểm tra kết quả của bước hiện tại có hữu hạn hay không.
        if not np.isfinite(ys[i]):
            raise ValueError(
                f"Nghiệm xấp xỉ không hữu hạn tại bước i={i}; "
                "hãy kiểm tra bài toán hoặc tăng độ ổn định của phép tính."
            )

    # Pseudocode bước 5: Trả về lưới x và nghiệm xấp xỉ y.
    return xs, ys


def euler_improved(f, a, b, y0, n):
    """
    P2 - Phương pháp Euler cải tiến (Heun).

    Pseudocode:
    1. Kiểm tra đầu vào.
    2. Tính h = (b - a) / n.
    3. Tạo các nút x_i; đặt y_0 = giá trị đầu.
    4. Với i = 1, ..., n:
           k1 = f(x_(i-1), y_(i-1))
           y_du_doan = y_(i-1) + h*k1
           k2 = f(x_i, y_du_doan)
           y_i = y_(i-1) + (h/2)*(k1 + k2)
    5. Trả về các mảng x và y.
    """
    # Pseudocode bước 1: Kiểm tra đầu vào.
    a, b, y0, n = _validate_inputs(f, a, b, y0, n)

    # Pseudocode bước 2: Tính độ dài mỗi bước lưới.
    h = (b - a) / n

    # Pseudocode bước 3: Tạo lưới và mảng nghiệm xấp xỉ.
    xs = np.linspace(a, b, n + 1, dtype=float)
    ys = np.empty(n + 1, dtype=float)

    # Pseudocode bước 3: Đặt giá trị ban đầu.
    ys[0] = y0

    # Pseudocode bước 4: Tính nghiệm tại từng bước bằng dự đoán rồi hiệu chỉnh.
    for i in range(1, n + 1):
        # Lấy tọa độ và nghiệm xấp xỉ tại bước trước.
        x_prev = float(xs[i - 1])
        y_prev = float(ys[i - 1])
        x_next = float(xs[i])

        # Tính k1: hệ số góc ở đầu khoảng.
        k1 = _evaluate(f, x_prev, y_prev)

        # Dự đoán nghiệm ở đầu phải bằng công thức Euler.
        y_predict = y_prev + h * k1
        if not np.isfinite(y_predict):
            raise ValueError(f"Giá trị dự đoán không hữu hạn tại bước i={i}.")

        # Tính k2: hệ số góc tại đầu phải, dùng giá trị dự đoán.
        k2 = _evaluate(f, x_next, float(y_predict))

        # Hiệu chỉnh: lấy trung bình hai hệ số góc k1 và k2.
        ys[i] = y_prev + (h / 2.0) * (k1 + k2)

        # Kiểm tra nghiệm sau hiệu chỉnh có hữu hạn hay không.
        if not np.isfinite(ys[i]):
            raise ValueError(
                f"Nghiệm xấp xỉ không hữu hạn tại bước i={i}; "
                "hãy kiểm tra bài toán hoặc tăng độ ổn định của phép tính."
            )

    # Pseudocode bước 5: Trả về lưới x và nghiệm xấp xỉ y.
    return xs, ys


    

