# P1 - THUẬT TOÁN 16: PHƯƠNG PHÁP EULER

Require: f(x,y), a, b, y0, n; b>a; n là số nguyên dương.
Ensure: Hai dãy xs, ys; ys[i] là nghiệm gần đúng tại xs[i].

1. h <- (b-a)/n
2. x[0] <- a; y[0] <- y0
3. For i <- 1 to n do
       y[i] <- y[i-1] + h*f(x[i-1], y[i-1])
       x[i] <- x[i-1] + h
   End For
4. Return x, y


# P2 - THUẬT TOÁN 17: EULER CẢI TIẾN (HEUN)

Require: f(x,y), a, b, y0, n; b>a; n là số nguyên dương.
Ensure: Hai dãy xs, ys; ys[i] là nghiệm gần đúng tại xs[i].

1. h <- (b-a)/n
2. x[0] <- a; y[0] <- y0
3. For i <- 1 to n do
       k1 <- f(x[i-1], y[i-1])
       y_predict <- y[i-1] + h*k1
       k2 <- f(x[i-1]+h, y_predict)
       y[i] <- y[i-1] + (h/2)*(k1+k2)
       x[i] <- x[i-1] + h
   End For
4. Return x, y


ĐỐI CHIẾU VỚI SÁCH:
- Bước 1: tính h.
- Bước 2: bắt đầu vòng lặp i=1,...,n.
- Bước 3: tính y_i (với Heun gồm dự đoán và hiệu chỉnh).
- Bước 4: cập nhật x_i.
- Bước 5: kết thúc vòng lặp.
- Bước 6: trả về nghiệm.
Code có thêm kiểm tra đầu vào và tạo mảng kết quả để đáp ứng R6 và giao diện nhóm.
Trong chữ ký hàm của nhóm không có x0 riêng, do đó đặt x0=a.
