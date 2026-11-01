import pytest
import numpy as np
from p4 import midpoint_ode, ralston  # hoặc tên file chứa hàm của bạn

def test_midpoint_basic():
    # Kiểm tra với bài toán cơ bản y' = y - x^2 + 1, y(0) = 0.5, [0, 2], h = 0.2 (n = 10)
    f = lambda x, y: y - x**2 + 1
    xs, ys = midpoint_ode(f, 0, 2, 0.5, 10)
    # Kiểm tra giá trị gần đúng tại x = 2 (y_10) theo đề bài là khoảng 5.290369
    assert np.isclose(ys[-1], 5.290369, atol=1e-4)

def test_ralston_basic():
    f = lambda x, y: y - x**2 + 1
    xs, ys = ralston(f, 0, 2, 0.5, 10)
    # Kiểm tra tính hợp lệ của mảng trả về
    assert len(xs) == 11
    assert len(ys) == 11

def test_edge_cases():
    f = lambda x, y: y
    # Ca biên: n âm hoặc bằng 0 phải báo lỗi ValueError
    with pytest.raises(ValueError):
        midpoint_ode(f, 0, 1, 1, 0)
    with pytest.raises(ValueError):
        ralston(f, 1, 0, 1, 5)  # a >= b
