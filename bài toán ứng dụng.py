import numpy as np
import matplotlib.pyplot as plt
from euler_methods import euler, euler_improved
from p4 import midpoint_ode, ralston

# Phần của SV7: Bài toán ứng dụng mô hình logistic

def logistic_rhs(t, P, r=0.3, K=10.0):
    """
    Hàm tính vế phải phương trình logistic P' = rP(1 - P/K)
    Require: t (thời gian), P (số xe), r (tốc độ tăng), K (sức chứa)
    Ensure: Trả về giá trị đạo hàm P'
    """
    if K <= 0:
        raise ValueError("Lỗi: K phải lớn hơn 0")
    return r * P * (1.0 - P / K)

def logistic_exact(t, P0=1.0, r=0.3, K=10.0):
    """
    Nghiệm đúng giải tích của bài toán
    Require: t, P0, r, K
    Ensure: Trả về số xe P(t) thực tế
    """
    if P0 <= 0 or K <= 0:
        raise ValueError("P0 và K phải là số dương")
    return K / (1.0 + (K / P0 - 1.0) * np.exp(-r * t))

def find_crossing_year(ts, Ps, threshold=8.0):
    """
    Tìm năm mà số xe vượt ngưỡng 8 triệu
    Require: mảng thời gian ts, mảng số xe Ps, ngưỡng threshold
    Ensure: Trả về năm rời rạc và năm nội suy tuyến tính
    """
    idx = np.where(Ps >= threshold)[0]
    if len(idx) == 0:
        return None, None
    
    first = idx[0]
    discrete_yr = float(ts[first])
    
    if first == 0:
        return discrete_yr, discrete_yr
        
    # Tính nội suy
    t0, t1 = ts[first - 1], ts[first]
    P0, P1 = Ps[first - 1], Ps[first]
    interp_yr = t0 + (threshold - P0) * (t1 - t0) / (P1 - P0)
    
    return discrete_yr, float(interp_yr)

def run_application():
    """
    Hàm chạy chính để in kết quả và vẽ đồ thị
    Require: Không có
    Ensure: In bảng số liệu ra terminal và lưu ảnh đồ thị
    """
    a, b = 0.0, 20.0
    P0 = 1.0
    r, K = 0.3, 10.0
    threshold = 8.0

    methods = {
        "Euler": euler,
        "Euler cải tiến": euler_improved,
        "Điểm giữa": midpoint_ode,
        "Ralston": ralston,
    }

    t_exact_8 = np.log((K / P0 - 1.0) / (K / threshold - 1.0)) / r
    print(f"Thời điểm đúng P(t) = {threshold} là: {t_exact_8:.4f} năm\n")

    results = {}
    for h in [1.0, 0.5]:
        n = int((b - a) / h)
        results[h] = {}
        print(f"--- Kết quả với h = {h} ---")
        print(f"{'Phương pháp':<18} | {'P(10)':<8} | {'P(20)':<8} | {'Năm vượt 8tr':<12}")
        print("-" * 55)

        for name, func in methods.items():
            ts, Ps = func(logistic_rhs, a, b, P0, n)
            results[h][name] = (ts, Ps)
            idx_10 = int(10.0 / h)
            disc_yr, interp_yr = find_crossing_year(ts, Ps, threshold)
            print(f"{name:<18} | {Ps[idx_10]:<8.4f} | {Ps[-1]:<8.4f} | {disc_yr:<12.1f}")
        print("\n")

    print("--- Khảo sát bước nhảy h lớn với Euler ---")
    ts_h5, Ps_h5 = euler(logistic_rhs, 0.0, 20.0, P0, n=4)
    print("Với h = 5:")
    for t_val, p_val in zip(ts_h5, Ps_h5):
        print(f"  t = {t_val}: P = {p_val:.4f}")

    ts_h8, Ps_h8 = euler(logistic_rhs, 0.0, 40.0, P0, n=5)
    print("\nVới h = 8:")
    for t_val, p_val in zip(ts_h8, Ps_h8):
        print(f"  t = {t_val}: P = {p_val:.4f}")

    # Vẽ đồ thị
    t_fine = np.linspace(0, 20, 400)
    P_fine = logistic_exact(t_fine)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Đồ thị 1: so sánh h=1
    ax1 = axes[0]
    ax1.plot(t_fine, P_fine, "k-", label="Nghiệm đúng")
    styles = {"Euler": "r--", "Euler cải tiến": "b-.", "Điểm giữa": "g:", "Ralston": "m--"}
    for name, style in styles.items():
        ts, Ps = results[1.0][name]
        ax1.plot(ts, Ps, style, label=f"{name}")
    ax1.axhline(threshold, color="gray", linestyle="--")
    ax1.set_title("So sánh các phương pháp (h=1)")
    ax1.legend()

    # Đồ thị 2: khảo sát h lớn
    ax2 = axes[1]
    t_fine_ext = np.linspace(0, 40, 500)
    ax2.plot(t_fine_ext, logistic_exact(t_fine_ext), "k-", label="Nghiệm đúng")
    ts_h1, Ps_h1 = results[1.0]["Euler"]
    ax2.plot(ts_h1, Ps_h1, "g--", label="Euler (h=1)")
    ts_h5_ext, Ps_h5_ext = euler(logistic_rhs, 0.0, 40.0, P0, n=8)
    ax2.plot(ts_h5_ext, Ps_h5_ext, "b-", label="Euler (h=5)")
    ax2.plot(ts_h8, Ps_h8, "r-", label="Euler (h=8 - Dao động)")
    ax2.axhline(K, color="orange", linestyle="--")
    ax2.set_title("Mất ổn định khi h=5, h=8")
    ax2.legend()

    plt.tight_layout()
    plt.savefig("logistic_application_sv7.png")
    print("\n[Đã lưu ảnh đồ thị]")

if __name__ == "__main__":
    run_application()