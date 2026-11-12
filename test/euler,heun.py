#test euler
import pytest
import numpy as np
from src/euler_heun.py import euler

def test_euler_edge_cases():
    f = lambda x, y: y
    with pytest.raises(TypeError):
        euler("not_callable", 0, 1, 1, 10)
    with pytest.raises(TypeError):
        euler(f, 0, 1, 1, 10.5)
    with pytest.raises(ValueError):
        euler(f, 0, 1, 1, 0)
    with pytest.raises(ValueError):
        euler(f, 2, 0, 1, 10)

def test_euler_basic():
    f = lambda x, y: y - x**2 + 1
    exact_y_at_2 = (2 + 1)**2 - 0.5 * np.exp(2)
    xs, ys = euler(f, 0, 2, 0.5, 10)
    assert len(xs) == 11 and len(ys) == 11
    assert np.isclose(ys[-1], exact_y_at_2, atol=0.6)

def test_euler_convergence_order():
    f = lambda x, y: y
    exact_val = np.exp(1.0)
    _, ys_10 = euler(f, 0, 1, 1.0, 10)
    _, ys_100 = euler(f, 0, 1, 1.0, 100)
    ratio = abs(exact_val - ys_10[-1]) / abs(exact_val - ys_100[-1])
    assert 8 < ratio < 12
    import pytest
    # test heun
import numpy as np
from src/euler_heun.py import euler_improved

def test_euler_improved_edge_cases():
    f = lambda x, y: y
    with pytest.raises(TypeError):
        euler_improved("not_callable", 0, 1, 1, 10)
    with pytest.raises(TypeError):
        euler_improved(f, 0, 1, 1, 10.5)
    with pytest.raises(ValueError):
        euler_improved(f, 0, 1, 1, 0)
    with pytest.raises(ValueError):
        euler_improved(f, 2, 0, 1, 10)

def test_euler_improved_basic():
    f = lambda x, y: y - x**2 + 1
    exact_y_at_2 = (2 + 1)**2 - 0.5 * np.exp(2)
    xs, ys = euler_improved(f, 0, 2, 0.5, 10)
    assert len(xs) == 11 and len(ys) == 11
    assert np.isclose(ys[-1], exact_y_at_2, atol=0.05)

def test_euler_improved_convergence_order():
    f = lambda x, y: y
    exact_val = np.exp(1.0)
    _, ys_10 = euler_improved(f, 0, 1, 1.0, 10)
    _, ys_100 = euler_improved(f, 0, 1, 1.0, 100)
    ratio = abs(exact_val - ys_10[-1]) / abs(exact_val - ys_100[-1])
    assert 90 < ratio < 110
