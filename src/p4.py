# -*- coding: utf-8 -*-
from __future__ import annotations

from collections.abc import Callable
import numpy as np
from numpy.typing import NDArray

ScalarFunction = Callable[[float, float], float]
FloatArray = NDArray[np.float64]


def _validate_inputs(
    f: ScalarFunction, a: float, b: float, y0: float, n: int
) -> None:
    """Kiểm tra điều kiện biên và đầu vào hợp lệ."""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Lỗi biên: Số bước chia n phải là số nguyên dương lớn hơn 0.")
    if a >= b:
        raise ValueError("Lỗi biên: Đầu mút khoảng [a, b] không hợp lệ (yêu cầu a < b).")


def midpoint_ode(
    f: ScalarFunction, a: float, b: float, y0: float, n: int
) -> tuple[FloatArray, FloatArray]:
    """
    Thuật toán: Phương pháp Điểm giữa (Midpoint ODE) giải phương trình vi phân y' = f(x, y).

    Require: Hàm f, đoạn [a, b], điều kiện đầu y0, số bước chia n.
    Ensure: Mảng điểm mốc xs và mảng nghiệm xấp xỉ ys.

    Pseudocode (Thuật toán Điểm giữa - Trường hợp riêng RK2 với alpha = beta = 1/2, r1 = 0, r2 = 1):
    1: Kiểm tra điều kiện đầu vào (a < b, n > 0). Báo lỗi nếu không thỏa mãn.
    2: h <- (b - a) / n
    3: Tạo mảng xs gồm n + 1 điểm chia từ a đến b
    4: Tạo mảng ys kích thước n + 1, gán ys[0] <- y0
    5: Lặp i từ 0 đến n - 1:
    6:     k1 <- h * f(xs[i], ys[i])
    7:     k2 <- h * f(xs[i] + h / 2, ys[i] + k1 / 2)
    8:     ys[i + 1] <- ys[i] + k2
    9: Trả về (xs, ys)
    """
    # Dòng 1 - Pseudocode: Kiểm tra điều kiện hợp lệ
    _validate_inputs(f, a, b, y0, n)

    # Dòng 2 - Pseudocode: Tính bước lưới h
    h = (b - a) / n

    # Dòng 3 - Pseudocode: Khởi tạo mảng các điểm mốc x
    xs = np.linspace(a, b, n + 1)

    # Dòng 4 - Pseudocode: Khởi tạo mảng y và đặt giá trị ban đầu y0
    ys = np.zeros(n + 1)
    ys[0] = y0

    # Dòng 5 - Pseudocode: Vòng lặp các bước tính toán
    for i in range(n):
        x_i = xs[i]
        y_i = ys[i]

        # Dòng 6 - Pseudocode: Tính k1
        k1 = h * f(x_i, y_i)

        # Dòng 7 - Pseudocode: Tính k2 tại điểm giữa (x_i + h/2, y_i + k1/2)
        k2 = h * f(x_i + 0.5 * h, y_i + 0.5 * k1)

        # Dòng 8 - Pseudocode: Cập nhật giá trị y_{i+1}
        ys[i + 1] = y_i + k2

    # Dòng 9 - Pseudocode: Trả về cặp mảng (xs, ys)
    return xs, ys


def ralston(
    f: ScalarFunction, a: float, b: float, y0: float, n: int
) -> tuple[FloatArray, FloatArray]:
    """
    Thuật toán: Phương pháp Ralston (Tối ưu sai số RK2) giải phương trình vi phân y' = f(x, y).

    Require: Hàm f, đoạn [a, b], điều kiện đầu y0, số bước chia n.
    Ensure: Mảng điểm mốc xs và mảng nghiệm xấp xỉ ys.

    Pseudocode (Thuật toán Ralston - Trường hợp riêng RK2 với alpha = beta = 3/4, r1 = 1/3, r2 = 2/3):
    1: Kiểm tra điều kiện đầu vào (a < b, n > 0). Báo lỗi nếu không thỏa mãn.
    2: h <- (b - a) / n
    3: Tạo mảng xs gồm n + 1 điểm chia từ a đến b
    4: Tạo mảng ys kích thước n + 1, gán ys[0] <- y0
    5: Lặp i từ 0 đến n - 1:
    6:     k1 <- h * f(xs[i], ys[i])
    7:     k2 <- h * f(xs[i] + 3*h / 4, ys[i] + 3*k1 / 4)
    8:     ys[i + 1] <- ys[i] + (1/3)*k1 + (2/3)*k2
    9: Trả về (xs, ys)
    """
    # Dòng 1 - Pseudocode: Kiểm tra điều kiện hợp lệ
    _validate_inputs(f, a, b, y0, n)

    # Dòng 2 - Pseudocode: Tính bước lưới h
    h = (b - a) / n

    # Dòng 3 - Pseudocode: Khởi tạo mảng các điểm mốc x
    xs = np.linspace(a, b, n + 1)

    # Dòng 4 - Pseudocode: Khởi tạo mảng y và đặt giá trị ban đầu y0
    ys = np.zeros(n + 1)
    ys[0] = y0

    # Dòng 5 - Pseudocode: Vòng lặp các bước tính toán
    for i in range(n):
        x_i = xs[i]
        y_i = ys[i]

        # Dòng 6 - Pseudocode: Tính k1
        k1 = h * f(x_i, y_i)

        # Dòng 7 - Pseudocode: Tính k2 theo hệ số Ralston (3/4)
        k2 = h * f(x_i + 0.75 * h, y_i + 0.75 * k1)

        # Dòng 8 - Pseudocode: Cập nhật giá trị y_{i+1} theo công thức tổ hợp (1/3)*k1 + (2/3)*k2
        ys[i + 1] = y_i + (1.0 / 3.0) * k1 + (2.0 / 3.0) * k2

    # Dòng 9 - Pseudocode: Trả về cặp mảng (xs, ys)
    return xs, ys
