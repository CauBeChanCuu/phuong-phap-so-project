from __future__ import annotations

from collections.abc import Callable
import numpy as np
from numpy.typing import NDArray

ScalarFunction = Callable[[float, float], float]
FloatArray = NDArray[np.float64]

def _validate_inputs(
    f: ScalarFunction, a: float, b: float, y0: float, n: int
) -> tuple[float, float, float, int]:
    """Kiểm tra điều kiện đầu vào dùng chung cho các phương pháp số."""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Số bước chia đoạn n phải là số nguyên dương lớn hơn 0.")
    if a >= b:
        raise ValueError("Đầu mút đoạn [a, b] không hợp lệ: a phải nhỏ hơn b.")
    return f, a, b, y0, n

def midpoint_ode(
    f: ScalarFunction, a: float, b: float, y0: float, n: int
) -> tuple[FloatArray, FloatArray]:
    """
    Phương pháp Điểm giữa (Midpoint method - thuộc RK2).
    
    Parameters
    ----------
    f : callable
        Hàm vế phải của phương trình vi phân y' = f(x, y).
    a, b : float
        Hai đầu mút của đoạn tính nghiệm [a, b].
    y0 : float
        Điều kiện đầu y(a) = y0.
    n : int
        Số bước chia đoạn; phải là số nguyên dương.
        
    Returns
    -------
    tuple[NDArray, NDArray]
        Mảng chứa các giá trị x và mảng chứa giá trị nghiệm y tương ứng.
    """
    _validate_inputs(f, a, b, y0, n)
    h = (b - a) / n
    xs = np.linspace(a, b, n + 1)
    ys = np.zeros(n + 1)
    ys[0] = y0
    
    for i in range(n):
        x_i = xs[i]
        y_i = ys[i]
        
        # Thuật toán điểm giữa: alpha = beta = 1/2, r1 = 0, r2 = 1
        k1 = h * f(x_i, y_i)
        k2 = h * f(x_i + 0.5 * h, y_i + 0.5 * k1)
        
        ys[i + 1] = y_i + k2  # # dòng tương ứng công thức điểm giữa
        
    return xs, ys


def ralston(
    f: ScalarFunction, a: float, b: float, y0: float, n: int
) -> tuple[FloatArray, FloatArray]:
    """
    Phương pháp Ralston (thuộc RK2 với sai số tối ưu).
    
    Parameters
    ----------
    f : callable
        Hàm vế phải của phương trình vi phân y' = f(x, y).
    a, b : float
        Hai đầu mút của đoạn tính nghiệm [a, b].
    y0 : float
        Điều kiện đầu y(a) = y0.
    n : int
        Số bước chia đoạn; phải là số nguyên dương.
        
    Returns
    -------
    tuple[NDArray, NDArray]
        Mảng chứa các giá trị x và mảng chứa giá trị nghiệm y tương ứng.
    """
    _validate_inputs(f, a, b, y0, n)
    h = (b - a) / n
    xs = np.linspace(a, b, n + 1)
    ys = np.zeros(n + 1)
    ys[0] = y0
    
    for i in range(n):
        x_i = xs[i]
        y_i = ys[i]
        
        # Thuật toán Ralston: alpha = beta = 3/4, r1 = 1/3, r2 = 2/3
        k1 = h * f(x_i, y_i)
        k2 = h * f(x_i + 0.75 * h, y_i + 0.75 * k1)
        
        ys[i + 1] = y_i + (1.0 / 3.0) * k1 + (2.0 / 3.0) * k2  # # dòng tương ứng công thức Ralston
        
    return xs, ys