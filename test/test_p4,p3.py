# TEST P4
import pytest
import numpy as np
from p4 import midpoint_ode, ralston, rk2

def test_midpoint_basic():
    """Kiểm tra phương pháp Điểm giữa với bài toán y' = y - x^2 + 1, y(0) = 0.5 trên [0, 2], h = 0.2."""
    f = lambda x, y: y - x**2 + 1
    xs, ys = midpoint_ode(f, 0.0, 2.0, 0.5, 10)
    
    assert len(xs) == 11
    assert len(ys) == 11
    # Giá trị gần đúng tại x = 2 (y_10) khoảng 5.290369
    assert np.isclose(ys[-1], 5.290369, atol=1e-4)

def test_ralston_basic():
    """Kiểm tra phương pháp Ralston để đảm bảo mảng trả về đúng kích thước và chạy không lỗi."""
    f = lambda x, y: y - x**2 + 1
    xs, ys = ralston(f, 0.0, 2.0, 0.5, 10)
    
    assert len(xs) == 11
    assert len(ys) == 11

def test_rk2_heun_equivalent():
    """
    Kiểm tra rk2 với tham số của Euler cải tiến (r1=0.5, r2=0.5, alpha=1.0, beta=1.0).
    Bài toán: y' = y - x^2 + 1, y(0) = 0.5 trên [0, 2], h = 0.2.
    Kết quả y_10 phải gần bằng 5.233055.
    """
    f = lambda x, y: y - x**2 + 1
    xs, ys = rk2(f, 0.0, 2.0, 0.5, 10, r1=0.5, r2=0.5, alpha=1.0, beta=1.0)
    
    assert len(xs) == 11
    assert len(ys) == 11
    assert np.isclose(ys[-1], 5.233055, atol=1e-4)

def test_rk2_custom_function():
    """Kiểm tra rk2 với phương trình y' = 3*x^2*y, y(0) = 1 trên [0, 1], h = 0.2."""
    f = lambda x, y: 3 * (x**2) * y
    xs, ys = rk2(f, 0.0, 1.0, 1.0, 5, r1=0.5, r2=0.5, alpha=1.0, beta=1.0)
    
    assert np.isclose(ys[-1], 2.700507, atol=1e-4)

def test_edge_cases_and_exceptions():
    """Kiểm tra các trường hợp bắt lỗi ValueError (ca biên và ràng buộc rk2)."""
    f = lambda x, y: y
    
    # 1. Ca biên: n âm hoặc bằng 0
    with pytest.raises(ValueError):
        midpoint_ode(f, 0, 1, 1, 0)
        
    # 2. Ca biên: a >= b
    with pytest.raises(ValueError):
        ralston(f, 1, 0, 1, 5)
        
#TEST P3
import pytest
import numpy as np
from p3_rk2 import rk2


def test_rk2_lecture_example():
    """
    Ca 1: Ví dụ trong bài giảng/đề bài.
    Phương trình: y' = y - x^2 + 1, y(0) = 0.5 trên [0, 2] với h = 0.2 (n = 10).
    Với tham số Euler cải tiến (r1=0.5, r2=0.5, alpha=1.0, beta=1.0),
    kết quả y_10 thu được phải gần bằng 5.233055.
    """
    f = lambda x, y: y - x**2 + 1
    a, b, y0, n = 0.0, 2.0, 0.5, 10
    r1, r2, alpha, beta = 0.5, 0.5, 1.0, 1.0  # Bộ tham số Heun / Euler cải tiến

    xs, ys = rk2(f, a, b, y0, n, r1, r2, alpha, beta)

    assert len(xs) == 11
    assert len(ys) == 11
    # Kiểm tra y(2) khớp với giá trị Euler cải tiến trong đề bài
    assert np.isclose(ys[-1], 5.233055, atol=1e-4)


def test_rk2_heun_equivalent_to_euler_improved():
    """
    Ca 2: Kiểm tra tính đúng đắn với nghiệm đúng / trùng khớp với Euler cải tiến (R7).
    Bài toán: y' = 3*x^2*y, y(0) = 1 trên [0, 1] với n = 5 (h = 0.2).
    Kết quả y5 thu được phải bằng 2.700507.
    """
    f = lambda x, y: 3 * (x**2) * y
    a, b, y0, n = 0.0, 1.0, 1.0, 5
    r1, r2, alpha, beta = 0.5, 0.5, 1.0, 1.0

    xs, ys = rk2(f, a, b, y0, n, r1, r2, alpha, beta)

    assert np.isclose(ys[-1], 2.700507, atol=1e-4)


def test_rk2_edge_cases_and_exceptions():
    """
    Ca 3: Ca biên và kiểm tra phát hiện vi phạm ràng buộc (R6, R7).
    - Bộ tham số vi phạm ràng buộc (6.9) phải báo lỗi ValueError.
    - Điều kiện đầu vào không hợp lệ (n <= 0 hoặc a >= b) phải báo lỗi ValueError.
    """
    f = lambda x, y: y

    # 1. Vi phạm ràng buộc (6.9): r1 = r2 = 0.5 nhưng alpha = beta = 0.5 (r2*alpha = 0.25 != 0.5)
    with pytest.raises(ValueError) as exc_info:
        rk2(f, 0, 1, 1, 10, r1=0.5, r2=0.5, alpha=0.5, beta=0.5)
    assert "vi phạm điều kiện ràng buộc (6.9)" in str(exc_info.value)

    # 2. Ca biên n <= 0
    with pytest.raises(ValueError):
        rk2(f, 0, 1, 1, 0, 0.5, 0.5, 1.0, 1.0)

    # 3. Ca biên a >= b
    with pytest.raises(ValueError):
        rk2(f, 2, 1, 1, 10, 0.5, 0.5, 1.0, 1.0)
        
    # 3. Vi phạm ràng buộc (6.9) của RK2: r2*alpha != 0.5
    with pytest.raises(ValueError, match="ràng buộc"):
        rk2(f, 0, 1, 1, 10, r1=0.5, r2=0.5, alpha=0.5, beta=0.5)
