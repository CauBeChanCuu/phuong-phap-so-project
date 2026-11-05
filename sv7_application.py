import numpy as np
import matplotlib.pyplot as plt
from euler_methods import euler, euler_improved
from p4 import midpoint_ode, ralston

# ==============================================================================
# CÁC HÀM MÔ HÌNH HÓA VÀ PHÂN TÍCH BÀI TOÁN ỨNG DỤNG (SV7)
# ==============================================================================

def logistic_rhs(t: float, P: float, r: float = 0.3, K: float = 10.0) -> float:
    """Hàm vế phải của phương trình vi phân logistic: P' = r * P * (1 - P / K)."""
    if K <= 0:
        raise ValueError("Sức chứa K phải lớn hơn 0.")
    return r * P * (1.0 - P / K)

def logistic_exact(t: np.ndarray | float, P0: float = 1.0, r: float = 0.3, K: float = 10.0) -> np.ndarray | float:
    """Nghiệm đúng giải tích của bài toán tăng trưởng logistic."""
    if P0 <= 0 or K <= 0:
        raise ValueError("P0 và K phải là số dương.")
    return K / (1.0 + (K / P0 - 1.0) * np.exp(-r * t))
def find_crossing_year(ts: np.ndarray, Ps: np.ndarray, threshold: float = 8.0) -> tuple[int | None, float | None]:
    """Xác định thời điểm t (năm) khi số phương tiện P(t) vượt ngưỡng."""
    idx = np.where(Ps >= threshold)[0]
    if len(idx) == 0:
        return None, None
    first_idx = idx[0]
    discrete_year = float(ts[first_idx])
    if first_idx == 0:
        return discrete_year, discrete_year
    t_prev, t_curr = ts[first_idx - 1], ts[first_idx]
    P_prev, P_curr = Ps[first_idx - 1], Ps[first_idx]
    interp_year = t_prev + (threshold - P_prev) * (t_curr - t_prev) / (P_curr - P_prev)
    return discrete_year, float(interp_year)

def run_application():
    """Chạy toàn bộ thực nghiệm bài toán ứng dụng của SV7"""
    a, b = 0.0, 20.0
    P0 = 1.0
    r, K = 0.3, 10.0
    threshold = 8.0

    methods = {
        "Euler": euler,
        "Euler cải tiến": euler_improved,
        "Điểm giữa (Midpoint)": midpoint_ode,
        "Ralston": ralston,
    }

    t_exact_8 = np.log((K / P0 - 1.0) / (K / threshold - 1.0)) / r
    print("=" * 80)
    print("BÀI TOÁN ỨNG DỤNG: MÔ HÌNH TĂNG TRƯỞNG LOGISTIC SỐ PHƯƠNG TIỆN ĐĂNG KÝ")
    print(f"Thời điểm chính xác P(t) chạm ngưỡng {threshold} triệu xe: t = {t_exact_8:.6f} năm")
    print("=" * 80)

    results = {}