"""
P1 và P2: Phương pháp Euler và Euler cải tiến giải bài toán Cauchy
y' = f(x, y), y(a) = y0 trên đoạn [a, b].

Yêu cầu tương thích: Python >= 3.10, NumPy.
Chữ ký hàm theo phân công của nhóm:
    euler(f, a, b, y0, n) -> tuple[np.ndarray, np.ndarray]
    euler_improved(f, a, b, y0, n) -> tuple[np.ndarray, np.ndarray]
"""

from __future__ import annotations

from collections.abc import Callable
import numpy as np
from numpy.typing import NDArray

ScalarFunction = Callable[[float, float], float]
FloatArray = NDArray[np.float64]


def _validate_inputs(
    f: ScalarFunction, a: float, b: float, y0: float, n: int
) -> tuple[float, float, float, int]:
    """Kiểm tra dữ liệu đầu vào dùng chung cho các phương pháp.

    Parameters
    ----------
    f : callable
        Hàm vế phải của phương trình vi phân y' = f(x, y).
    a, b : float
        Hai đầu mút của đoạn tính nghiệm.
    y0 : float
        Điều kiện đầu y(a) = y0.
    n : int
        Số bước chia đoạn; phải là số nguyên dương.

    Returns
    -------
    tuple[float, float, float, int]
        Các dữ liệu đã được chuyển về kiểu số phù hợp.

    Raises
    ------
    TypeError
        Nếu f không callable hoặc n không phải số nguyên.
    ValueError
        Nếu n <= 0 hoặc dữ liệu số không hữu hạn.
    """
    if not callable(f):
        raise TypeError("f phải là một hàm có thể gọi được.")
    if isinstance(n, bool) or not isinstance(n, (int, np.integer)):
        raise TypeError("n phải là một số nguyên dương.")
    if n <= 0:
        raise ValueError("n phải lớn hơn 0.")
    try:
        a, b, y0 = float(a), float(b), float(y0)
    except (TypeError, ValueError) as exc:
        raise TypeError("a, b và y0 phải là các giá trị số.") from exc
    if not np.all(np.isfinite([a, b, y0])):
        raise ValueError("a, b và y0 phải là các giá trị hữu hạn.")
    if b <= a:
        raise ValueError("Cần có b > a để tính trên đoạn [a, b].")
    return a, b, y0, int(n)


def _evaluate(f: ScalarFunction, x: float, y: float) -> float:
    """Tính f(x, y) và báo lỗi rõ ràng nếu kết quả không hữu hạn."""
    try:
        value = float(f(x, y))
    except Exception as exc:
        raise ValueError(
            f"Không tính được f(x, y) tại x={x!r}, y={y!r}."
        ) from exc
    if not np.isfinite(value):
        raise ValueError(
            f"f(x, y) không hữu hạn tại x={x!r}, y={y!r}."
        )
    return value


def euler(
    f: ScalarFunction, a: float, b: float, y0: float, n: int
) -> tuple[FloatArray, FloatArray]:
    """Xấp xỉ nghiệm bài toán Cauchy bằng phương pháp Euler (P1).

    Phương pháp dùng công thức:
        h = (b - a) / n
        y[i] = y[i-1] + h * f(x[i-1], y[i-1])
        x[i] = a + i*h

    Parameters
    ----------
    f : callable
        Hàm f(x, y) trong phương trình y' = f(x, y).
    a, b : float
        Đoạn tính nghiệm [a, b], với b > a.
    y0 : float
        Giá trị đầu y(a) = y0.
    n : int
        Số bước chia đoạn, là số nguyên dương.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        (xs, ys), hai mảng một chiều độ dài n + 1. xs chứa các nút
        từ a đến b; ys chứa nghiệm xấp xỉ tại các nút tương ứng.

    Raises
    ------
    TypeError
        Nếu f không callable hoặc n không phải số nguyên.
    ValueError
        Nếu dữ liệu đầu vào không hợp lệ hoặc f cho giá trị không hữu hạn.

    Notes
    -----
    Đây là phương pháp Euler hiện (Euler tiến), tương ứng Thuật toán 16
    trong tài liệu môn học. Không dùng bộ giải ODE có sẵn.
    """
    a, b, y0, n = _validate_inputs(f, a, b, y0, n)
    h = (b - a) / n

    xs = np.linspace(a, b, n + 1, dtype=float)
    ys = np.empty(n + 1, dtype=float)
    ys[0] = y0

    for i in range(1, n + 1):
        slope = _evaluate(f, float(xs[i - 1]), float(ys[i - 1]))
        ys[i] = ys[i - 1] + h * slope
        if not np.isfinite(ys[i]):
            raise ValueError(
                f"Nghiệm xấp xỉ không hữu hạn tại bước i={i}; "
                "hãy kiểm tra bài toán hoặc tăng độ ổn định của phép tính."
            )

    return xs, ys


def euler_improved(
    f: ScalarFunction, a: float, b: float, y0: float, n: int
) -> tuple[FloatArray, FloatArray]:
    """Xấp xỉ nghiệm bằng phương pháp Euler cải tiến (Heun) (P2).

    Ở mỗi bước, trước hết dự đoán:
        y_pred = y[i-1] + h*f(x[i-1], y[i-1])
    Sau đó hiệu chỉnh bằng trung bình hai hệ số góc:
        y[i] = y[i-1] + h/2 * (
            f(x[i-1], y[i-1]) + f(x[i], y_pred)
        )

    Parameters
    ----------
    f : callable
        Hàm f(x, y) trong phương trình y' = f(x, y).
    a, b : float
        Đoạn tính nghiệm [a, b], với b > a.
    y0 : float
        Giá trị đầu y(a) = y0.
    n : int
        Số bước chia đoạn, là số nguyên dương.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        (xs, ys), hai mảng một chiều độ dài n + 1. xs chứa các nút
        từ a đến b; ys chứa nghiệm xấp xỉ tại các nút tương ứng.

    Raises
    ------
    TypeError
        Nếu f không callable hoặc n không phải số nguyên.
    ValueError
        Nếu dữ liệu đầu vào không hợp lệ hoặc f cho giá trị không hữu hạn.

    Notes
    -----
    Phương pháp này tương ứng Thuật toán 17 trong tài liệu môn học.
    Không dùng bộ giải ODE có sẵn.
    """
    a, b, y0, n = _validate_inputs(f, a, b, y0, n)
    h = (b - a) / n

    xs = np.linspace(a, b, n + 1, dtype=float)
    ys = np.empty(n + 1, dtype=float)
    ys[0] = y0

    for i in range(1, n + 1):
        x_prev = float(xs[i - 1])
        y_prev = float(ys[i - 1])
        x_next = float(xs[i])

        slope_start = _evaluate(f, x_prev, y_prev)
        y_predict = y_prev + h * slope_start
        if not np.isfinite(y_predict):
            raise ValueError(
                f"Giá trị dự đoán không hữu hạn tại bước i={i}."
            )

        slope_end = _evaluate(f, x_next, float(y_predict))
        ys[i] = y_prev + (h / 2.0) * (slope_start + slope_end)
        if not np.isfinite(ys[i]):
            raise ValueError(
                f"Nghiệm xấp xỉ không hữu hạn tại bước i={i}; "
                "hãy kiểm tra bài toán hoặc tăng độ ổn định của phép tính."
            )

    return xs, ys
