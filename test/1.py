import pytest
import numpy as np

from baitoanungdung import (
    logistic_rhs,
    logistic_exact,
    find_crossing_year,
    run_application
)

def test_logistic_rhs_validation():
    with pytest.raises(ValueError, match="K phải lớn hơn 0"):
        logistic_rhs(0.0, 1.0, r=0.3, K=0.0)
    with pytest.raises(ValueError, match="K phải lớn hơn 0"):
        logistic_rhs(0.0, 1.0, r=0.3, K=-5.0)

def test_logistic_rhs_values():
    assert logistic_rhs(0.0, 0.0) == 0.0
    assert logistic_rhs(0.0, 10.0, K=10.0) == 0.0
    assert np.isclose(logistic_rhs(0.0, 5.0, r=0.3, K=10.0), 0.75)

def test_logistic_exact_validation():
    with pytest.raises(ValueError, match="P0 và K phải là số dương"):
        logistic_exact(1.0, P0=0.0, K=10.0)
    with pytest.raises(ValueError, match="P0 và K phải là số dương"):
        logistic_exact(1.0, P0=1.0, K=-2.0)

def test_logistic_exact_values():
    # Tại t = 0, P(0) phải bằng P0
    assert np.isclose(logistic_exact(0.0, P0=1.0, K=10.0), 1.0)
    # Khi t rất lớn, P(t) tiến tới sức chứa K
    assert np.isclose(logistic_exact(100.0, P0=1.0, K=10.0), 10.0, atol=1e-4)

def test_find_crossing_year():
    ts = np.array([0.0, 1.0, 2.0, 3.0])
    
    # Chưa vượt ngưỡng
    Ps_low = np.array([1.0, 3.0, 5.0, 7.0])
    assert find_crossing_year(ts, Ps_low, threshold=8.0) == (None, None)
    
    # Vượt ngưỡng ngay từ điểm ban đầu
    Ps_start = np.array([9.0, 9.5, 10.0, 10.0])
    assert find_crossing_year(ts, Ps_start, threshold=8.0) == (0.0, 0.0)
    
    # Nội suy tuyến tính đúng: P(1)=6, P(2)=10 => ngưỡng 8 nằm chính giữa t=1.5
    Ps_mid = np.array([1.0, 6.0, 10.0, 10.0])
    disc, interp = find_crossing_year(ts, Ps_mid, threshold=8.0)
    assert disc == 2.0
    assert np.isclose(interp, 1.5)

def test_run_application_execution(monkeypatch):
    # Mock plt.savefig để không tạo file ảnh khi chạy tự động
    monkeypatch.setattr("matplotlib.pyplot.savefig", lambda *args, **kwargs: None)
    monkeypatch.setattr("matplotlib.pyplot.show", lambda *args, **kwargs: None)
    
    # Kiểm tra xem hàm chạy hoàn chỉnh không văng lỗi
    run_application()
