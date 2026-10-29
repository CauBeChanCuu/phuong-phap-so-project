"""Kiểm thử P1/P2 bằng pytest: ví dụ bài giảng, nghiệm đã biết và ca biên."""

import numpy as np
import pytest

from euler_methods import euler, euler_improved


def lecture_f(x, y):
    # Ví dụ 6.2 trong tài liệu: y' = y + exp(x)/x, y(1) = e.
    return y + np.exp(x) / x


def lecture_exact(x):
    # Nghiệm chính xác của ví dụ 6.2 trên đoạn [1, 2].
    return np.exp(x) * (1.0 + np.log(np.abs(x)))


@pytest.mark.parametrize("method", [euler, euler_improved])
def test_lecture_example_initial_value(method):
    """Ca kiểm thử từ ví dụ 6.2: điều kiện đầu y(1) = e phải được giữ."""
    xs, ys = method(lecture_f, 1.0, 2.0, np.e, 5)
    assert len(xs) == len(ys) == 6
    assert xs[0] == pytest.approx(1.0)
    assert xs[-1] == pytest.approx(2.0)
    assert ys[0] == pytest.approx(np.e)
    assert np.all(np.isfinite(xs))
    assert np.all(np.isfinite(ys))


@pytest.mark.parametrize("method", [euler, euler_improved])
def test_known_solution_constant_derivative(method):
    """Nghiệm y=x+2 của y'=1, y(0)=2 là nghiệm chính xác đã biết."""
    xs, ys = method(lambda x, y: 1.0, 0.0, 1.0, 2.0, 4)
    expected = xs + 2.0
    assert np.allclose(ys, expected, atol=1e-12, rtol=0.0)


@pytest.mark.parametrize("method", [euler, euler_improved])
def test_invalid_step_count(method):
    """Ca biên: số bước bằng 0 phải báo lỗi rõ ràng."""
    with pytest.raises(ValueError, match="n phải lớn hơn 0"):
        method(lambda x, y: y, 0.0, 1.0, 1.0, 0)


@pytest.mark.parametrize("method", [euler, euler_improved])
def test_non_finite_function_value(method):
    """Ca biên: hàm vế phải không hữu hạn phải báo lỗi, không trả kết quả sai."""
    def bad_function(x, y):
        return np.nan

    with pytest.raises(ValueError, match="không hữu hạn"):
        method(bad_function, 0.0, 1.0, 1.0, 2)


def test_improved_euler_more_accurate_for_simple_exponential():
    """Kiểm tra tính chất thực nghiệm: Heun thường chính xác hơn Euler với y'=y."""
    f = lambda x, y: y
    exact_at_one = np.e
    _, euler_values = euler(f, 0.0, 1.0, 1.0, 10)
    _, improved_values = euler_improved(f, 0.0, 1.0, 1.0, 10)
    assert abs(improved_values[-1] - exact_at_one) < abs(euler_values[-1] - exact_at_one)
