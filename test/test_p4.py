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
        
    # 3. Vi phạm ràng buộc (6.9) của RK2: r2*alpha != 0.5
    with pytest.raises(ValueError, match="ràng buộc"):
        rk2(f, 0, 1, 1, 10, r1=0.5, r2=0.5, alpha=0.5, beta=0.5)
