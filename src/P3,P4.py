import numpy as np
def rk2(f, a, b, y0, n, r1, r2, alpha, beta):
"""
Runge–Kutta bậc 2 tổng quát (công thức 6.8).
Kiểm tra ràng buộc (6.9) trước khi tính.
Parameters
----------
alpha, beta : float -- tham số bước phụ
f : callable -- hàm vế phải f(x, y)
a, b : float -- cận tích phân
y0 : float -- giá trị ban đầu y(a)
n : int -- số bước chia
r1, r2 : float -- trọng số
Returns
-------
xs, ys : tuple[np.ndarray, np.ndarray]
Raises
------
ValueError : nếu vi phạm ràng buộc (6.9) hoặc n <= 0 hoặc a >= b
"""
if n <= 0:
raise ValueError("n phải là sốnguyên dương")
if a >= b:
raise ValueError("a phải nhỏ hơn b")
# Kiem tra rang buoc (6.9) -- dong 1 thuat toan RK2
if not np.isclose(r1 + r2, 1.0, atol=1e-12):
raise ValueError(
f"Vi phạm (6.9): r1 + r2 = {r1+r2:.6f} ≠ 1"
)
if not np.isclose(r2 * alpha, 0.5, atol=1e-12):
raise ValueError(
f"Vi phạm (6.9): r2 * alpha = {r2*alpha:.6f} ≠ 0.5"
)
if not np.isclose(r2 * beta, 0.5, atol=1e-12):
raise ValueError(
f"Vi phạm (6.9): r2 * beta = {r2*beta:.6f} ≠ 0.5"
)
# dong 2 - thuat toan RK2
h = (b - a) / n
xs = np.linspace(a, b, n + 1)
ys = np.zeros(n + 1)
ys[0] = y0
for i in range(n):
# dong 6 - Cong thuc (6.8)
k1 = f(xs[i], ys[i])
# dong 7 - Cong thuc (6.8)
k2 = f(xs[i] + alpha * h, ys[i] + beta * h * k1)
# dong 8 - Cong thuc (6.8)
ys[i + 1] = ys[i] + h * (r1 * k1 + r2 * k2)
return xs, ys
def midpoint_ode(f, a, b, y0, n):
"""
Phương pháp điểm giữa — trường hợp riêng của rk2.
Tham số: alpha = beta = 1/2, r1 = 0, r2 = 1.
"""
return rk2(f, a, b, y0, n,
r1=0.0, r2=1.0, alpha=0.5, beta=0.5)
def ralston(f, a, b, y0, n):
"""
Phương pháp Ralston — trường hợp riêng của rk2.
Tham số: alpha = beta = 3/4, r1 = 1/3, r2 = 2/3.
"""
return rk2(f, a, b, y0, n,
r1=1/3, r2=2/3, alpha=0.75, beta=0.75)
