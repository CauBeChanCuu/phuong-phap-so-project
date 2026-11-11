### 1. Mô hình hóa và Dữ liệu bài toán
* **Mô hình toán học:** Số lượng phương tiện đăng ký $P(t)$ (triệu xe) theo thời gian $t$ (năm) tuân theo phương trình vi phân tăng trưởng logistic:
  $$P'(t) = rP\left(1 - \frac{P}{K}\right), \quad P(0) = 1, \quad 0 \le t \le 20$$
* **Tham số đầu vào:** Tốc độ tăng trưởng $r = 0.3$, sức chứa giới hạn $K = 10$, số xe ban đầu $P_0 = 1$.
* **Nghiệm giải tích chính xác:**
  $$P(t) = \frac{10}{1 + 9e^{-0.3t}}$$

### 2. Xác định năm P(t) vượt 8 triệu xe
* **Theo nghiệm đúng:** Giải phương trình $\frac{10}{1 + 9e^{-0.3t}} = 8 \implies t = \frac{\ln(36)}{0.3} \approx 11.9451\text{ năm}$ (Cuối năm thứ 12).
* **So sánh các phương pháp:**
  * Các phương pháp RK2 (Euler cải tiến, Điểm giữa, Ralston) đều xác định chính xác mốc vượt 8 triệu xe tại năm thứ 12 với $h = 1$.
  * Phương pháp Euler bậc 1 với $h = 1$ báo trễ sang năm thứ 13 ($P_{12} \approx 7.772$). Khi giảm bước xuống $h = 0.5$, kết quả cải thiện về mốc năm 12.5.

### 3. Mô tả và giải thích hiện tượng khi thử h = 5 và h = 8 với Euler
Hệ số khuếch đại sai số quanh điểm cân bằng $K=10$ của Euler là $(1 - hr)$ với $r=0.3$.
* **Trường hợp $h = 5$ ($hr = 1.5$):** $1 < hr < 2$. Nghiệm vọt lố (overshoot) vượt qua sức chứa tối đa $K = 10$ (lên tới $10.384$) ở bước $t=20$ do bước nhảy dài, sau đó sẽ dao động tắt dần quanh 10.
* **Trường hợp $h = 8$ ($hr = 2.4$):** $hr > 2$. Phương pháp mất ổn định số hoàn toàn. Nghiệm nhảy vọt lên $11.656$, sau đó bị kéo sập xuống $6.826$ và tiếp tục nảy lên $12.025$. Nghiệm dao động răng cưa vĩnh viễn quanh $K = 10$ và không bao giờ hội tụ.