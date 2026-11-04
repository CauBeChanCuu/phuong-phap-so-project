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
