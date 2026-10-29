# PHÂN TÍCH LÝ THUYẾT \- PHƯƠNG PHÁP RUNGE \- KUTTA BẬC 2 (RK2)

## **1\. Giới thiệu chung về phương pháp Runge \- Kutta bậc 2**

Phương pháp Runge \- Kutta bậc 2 (RK2) là một lớp các phương pháp số một bước dùng để giải gần đúng bài toán Cauchy cho phương trình vi phân thông thường dạng:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$y'=f(x,y),y(a)={y}_{0}trên\ đoạn[a,b]$

Công thức tổng quát của phương pháp Runge \- Kutta bậc 2 được xây dựng dựa trên khai triển Taylor của hàm nghiệm, có dạng:

&nbsp;

Công thức tổng quát của phương pháp Runge \- Kutta bậc 2 được xây dựng dựa trên khai triển Taylor của hàm nghiệm, có dạng:

$${y}_{i+1}={y}_{i}+{r}_{1}{K}_{1}+{r}_{2}{K}_{2}$$

Trong đó các hệ số tăng trưởng ${K}_{1}$ và ${K}_{2}$ được xác định bởi:

* ${K}_{1}=h\cdot f({x}_{i},{y}_{i})$  
* ${K}_{2}=h\cdot f({x}_{i}+\alpha h,{y}_{i}+\beta {K}_{1})$&nbsp;

Để đạt độ chính xác bậc 2 (sai số địa phương $O({h}^{3})$, sai số toàn cục $O({h}^{2})$), các tham số ${r}_{1},{r}_{2},\alpha ,\beta$ phải thỏa mãn hệ điều kiện ràng buộc sau:

1. ${r}_{1}+{r}_{2}=1$  
2. ${r}_{2}\alpha =\frac{1}{2}$  
3. ${r}_{2}\beta =\frac{1}{2}$

---

## 2\. Các trường hợp riêng ứng với Nhiệm vụ P4

Tùy thuộc vào việc lựa chọn các hệ số thỏa mãn hệ phương trình ràng buộc trên, ta thu được các phương pháp cụ thể sau:

### 2.1. Phương pháp Điểm giữa (Midpoint Method) \- Công thức (6.17)

* **Bộ hệ số:** $\alpha =\beta =\frac{1}{2}$, ${r}_{1}=0$, ${r}_{2}=1$.

**Công thức tính toán trong code (midpoint\_ode):**

&nbsp;

${K}_{1}=h\cdot f({x}_{i},{y}_{i})$

&nbsp;

${K}_{2}=h\cdot f\left({{x}_{i}+\frac{1}{2}h,{y}_{i}+\frac{1}{2}{K}_{1}}\right)$

&nbsp;

${y}_{i+1}={y}_{i}+{K}_{2}$

&nbsp;

### 2.2. Phương pháp Ralston \- Công thức (6.19)

* **Bộ hệ số:** $\alpha =\beta =\frac{3}{4}$, ${r}_{1}=\frac{1}{3}$, ${r}_{2}=\frac{2}{3}$. Phương pháp này được thiết kế để tối ưu hóa giảm thiểu sai số chặn trên của phương pháp RK2.

**Công thức tính toán trong code (ralston):**

&nbsp;

${K}_{1}=h\cdot f({x}_{i},{y}_{i})$

&nbsp;

${K}_{2}=h\cdot f\left({{x}_{i}+\frac{3}{4}h,{y}_{i}+\frac{3}{4}{K}_{1}}\right)$

&nbsp;

${y}_{i+1}={y}_{i}+\frac{1}{3}{K}_{1}+\frac{2}{3}{K}_{2}$

&nbsp;

## 3\. Chữ ký hàm chuẩn lập trình

Các hàm cài đặt trong module mã nguồn Python tuân thủ nghiêm ngặt chữ ký sau để phục vụ bộ kiểm thử chung (`pytest`):

```py
def midpoint_ode(f, a, b, y0, n) -> tuple[np.ndarray, np.ndarray]:
    """Phương pháp Điểm giữa (Midpoint ODE)."""
    pass

def ralston(f, a, b, y0, n) -> tuple[np.ndarray, np.ndarray]:
    """Phương pháp Ralston."""
    pass
```

&nbsp;