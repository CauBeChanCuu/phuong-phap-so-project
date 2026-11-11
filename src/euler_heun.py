P1 Euler (Thuật toán 17) và P2 Euler cải tiến/Heun (Thuật toán 18)."""
from __future__ import annotations
from collections.abc import Callable
import numpy as np
from numpy.typing import NDArray

ScalarFunction = Callable[[float, float], float]
FloatArray = NDArray[np.float64]


def _validate_inputs(f: ScalarFunction, a: float, b: float, y0: float, n: int):
    """Require: f callable; a,b,y0 hữu hạn; b>a; n nguyên dương.
    Ensure: trả về a,b,y0 kiểu float và n kiểu int.
    Thuật toán: kiểm tra đầu vào bổ sung, không phải bước tính lõi.
    """
    if not callable(f):
        raise TypeError("f phải là một hàm có thể gọi được.")
    if isinstance(n, (bool, np.bool_)) or not isinstance(n, (int, np.integer)):
        raise TypeError("n phải là số nguyên.")
    if n <= 0:
        raise ValueError("n phải lớn hơn 0.")
    try:
        a, b, y0 = float(a), float(b), float(y0)
    except (TypeError, ValueError, OverflowError) as exc:
        raise TypeError("a, b và y0 phải là các giá trị số.") from exc
    if not np.all(np.isfinite([a, b, y0])):
        raise ValueError("a, b và y0 phải là các giá trị hữu hạn.")
    if b <= a:
        raise ValueError("Cần có b > a để tính trên đoạn [a, b].")
    return a, b, y0, int(n)


def _evaluate(f: ScalarFunction, x: float, y: float) -> float:
    """Require: f gọi được. Ensure: trả về f(x,y) hữu hạn.
    Thuật toán: hàm hỗ trợ đánh giá hàm vế phải cho P1 và P2.
    """
    try:
        value = float(f(x, y))
    except Exception as exc:
        raise ValueError(f"Không tính được f(x,y) tại x={x!r}, y={y!r}.") from exc
    if not np.isfinite(value):
        raise ValueError(f"f(x,y) không hữu hạn tại x={x!r}, y={y!r}.")
    return value


def euler(f: ScalarFunction, a: float, b: float, y0: float, n: int) -> tuple[FloatArray, FloatArray]:
    """Thuật toán 17 - Euler.
    Require: y'=f(x,y), y(a)=y0; b>a; n nguyên dương; dữ liệu hữu hạn.
    Ensure: trả về (xs,ys), hai mảng NumPy n+1 phần tử.
    """
    # Kiểm tra đầu vào bổ sung theo R6.
    a, b, y0, n = _validate_inputs(f, a, b, y0, n)
    # Dòng 1- Thuật toán 17: h <- (b-a)/n.
    h = (b - a) / n
    # Khởi tạo x0=a, y0 đã cho và cấp phát mảng kết quả.-> Sử dụng AI
    xs = np.empty(n + 1, dtype=float)
    ys = np.empty(n + 1, dtype=float)
    xs[0], ys[0] = a, y0
    # Dòng 2 - Thuật toán 17: for i=1,...,n.
    for i in range(1, n + 1):
        # Dòng 3 - Thuật toán 17: y_i <- y_(i-1)+h*f(x_(i-1),y_(i-1)).
        slope = _evaluate(f, float(xs[i-1]), float(ys[i-1]))
        ys[i] = ys[i-1] + h * slope
        # Dòng 4 - Thuật toán 17: x_i <- x_(i-1)+h.
        xs[i] = xs[i-1] + h
        if not np.isfinite(xs[i]) or not np.isfinite(ys[i]):
            raise ValueError(f"Nghiệm hoặc nút lưới không hữu hạn tại bước i={i}.")
    # Dòng 5 - Thuật toán 17: return y_i; giao diện nhóm trả thêm xs.
    return xs, ys


def euler_improved(f: ScalarFunction, a: float, b: float, y0: float, n: int) -> tuple[FloatArray, FloatArray]:
    """Thuật toán 18 - Euler cải tiến (Heun).
    Require: y'=f(x,y), y(a)=y0; b>a; n nguyên dương; dữ liệu hữu hạn.
    Ensure: trả về (xs,ys), hai mảng NumPy n+1 phần tử.
    """
    # Kiểm tra đầu vào bổ sung theo R6.
    a, b, y0, n = _validate_inputs(f, a, b, y0, n)
    # Dòng 1 - Thuật toán 18: h <- (b-a)/n.
    h = (b - a) / n
    # Khởi tạo x0=a, y0 đã cho và cấp phát mảng kết quả.-> Sử dụng AI
    xs = np.empty(n + 1, dtype=float)
    ys = np.empty(n + 1, dtype=float)
    xs[0], ys[0] = a, y0
    # Dòng 2 - Thuật toán 18: for i=1,...,n.
    for i in range(1, n + 1):
        x_prev, y_prev = float(xs[i-1]), float(ys[i-1])
        x_next = x_prev + h
        # Dòng 3 - Thuật toán 18: k1 là độ dốc đầu bước; dự đoán bằng Euler.
        k1 = _evaluate(f, x_prev, y_prev)
        y_predict = y_prev + h * k1
        # Dòng 3 - Thuật toán 18: k2 là độ dốc cuối bước tại điểm dự đoán.
        k2 = _evaluate(f, x_next, y_predict)
        # Dòng 3 - Thuật toán 18: hiệu chỉnh bằng trung bình hai độ dốc.
        ys[i] = y_prev + (h / 2.0) * (k1 + k2)
        # Dòng 4 - Thuật toán 18: x_i <- x_(i-1)+h.
        xs[i] = x_next
        if not np.isfinite(xs[i]) or not np.isfinite(ys[i]):
            raise ValueError(f"Nghiệm hoặc nút lưới không hữu hạn tại bước i={i}.")
    # Dòng 5 - Thuật toán 18 return y_i; giao diện nhóm trả thêm xs.
    return xs, ys

