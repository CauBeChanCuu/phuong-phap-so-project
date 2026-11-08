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
    for h in [1.0, 0.5]:
        n = int((b - a) / h)
        results[h] = {}
        print(f"\n--- KẾT QUẢ VỚI BƯỚC NHẢY h = {h} ---")
        print(f"{'Phương pháp':<22} | {'P(10)':<10} | {'P(20)':<10} | {'Mốc t (P>=8)':<12}")
        print("-" * 65)

        for name, func in methods.items():
            ts, Ps = func(logistic_rhs, a, b, P0, n)
            results[h][name] = (ts, Ps, 0)
            idx_10 = int(10.0 / h)
            disc_yr, interp_yr = find_crossing_year(ts, Ps, threshold)
            print(f"{name:<22} | {Ps[idx_10]:<10.6f} | {Ps[-1]:<10.6f} | {disc_yr:<12.1f}")

    print("\n" + "=" * 80)
    print("KHẢO SÁT HIỆN TƯỢNG VỚI BƯỚC NHẢY LỚN (h = 5 VÀ h = 8) TRÊN PHƯƠNG PHÁP EULER")
    
    ts_h5, Ps_h5 = euler(logistic_rhs, 0.0, 20.0, P0, n=4)
    print("\n* Với h = 5 (trên đoạn [0, 20]):")
    for t_val, p_val in zip(ts_h5, Ps_h5):
        print(f"  t = {t_val:4.1f}: P_Euler = {p_val:10.6f}")

    ts_h8, Ps_h8 = euler(logistic_rhs, 0.0, 40.0, P0, n=5)
    print("\n* Với h = 8 (khảo sát đến t = 40):")
    for t_val, p_val in zip(ts_h8, Ps_h8):
        print(f"  t = {t_val:4.1f}: P_Euler = {p_val:10.6f}")

    # Vẽ đồ thị
    t_fine = np.linspace(0, 20, 400)
    P_fine = logistic_exact(t_fine, P0, r, K)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    ax1 = axes[0]
    ax1.plot(t_fine, P_fine, "k-", linewidth=2, label="Nghiệm đúng")
    styles = {"Euler": "r--o", "Euler cải tiến": "b-.s", "Điểm giữa (Midpoint)": "g:^", "Ralston": "m:d"}
    for name, style in styles.items():
        ts, Ps, _ = results[1.0][name]
        ax1.plot(ts, Ps, style, markersize=4, alpha=0.85, label=f"{name} (h=1)")
    ax1.axhline(threshold, color="gray", linestyle="--")
    ax1.set_title("Mô hình tăng trưởng Logistic (h = 1.0)")
    ax1.legend()

    ax2 = axes[1]
    t_fine_ext = np.linspace(0, 40, 500)
    ax2.plot(t_fine_ext, logistic_exact(t_fine_ext), "k-", linewidth=2, label="Nghiệm đúng")
    ts_h1, Ps_h1, _ = results[1.0]["Euler"]
    ax2.plot(ts_h1, Ps_h1, "g--o", label="Euler (h = 1)")
    ts_h5_ext, Ps_h5_ext = euler(logistic_rhs, 0.0, 40.0, P0, n=8)
    ax2.plot(ts_h5_ext, Ps_h5_ext, "b-s", label="Euler (h = 5)")
    ax2.plot(ts_h8, Ps_h8, "r-^", label="Euler (h = 8 - Dao động)")
    ax2.axhline(K, color="darkorange", linestyle="--")
    ax2.set_title("Ảnh hưởng của bước nhảy lớn h = 5 và h = 8 (Euler)")
    ax2.legend()

    plt.tight_layout()
    plt.savefig("logistic_application_sv7.png", dpi=300)
    print("\n[Đã lưu đồ thị vào file 'logistic_application_sv7.png']")

if __name__ == "__main__":
    run_application()