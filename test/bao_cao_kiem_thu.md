BÁO CÁO KIỂM THỬ CHƯƠNG TRÌNH 

Dự án: Phương pháp số 

 

Nhiệm vụ: SV5 – Kiểm thử chương trình bằng Pytest 

 

Mục tiêu kiểm thử 

Kiểm tra tính đúng đắn của các phương pháp giải phương trình vi phân thường bằng số, phát hiện lỗi và kiểm tra khả năng xử lý các trường hợp đầu vào không hợp lệ. 

 

Các chương trình được kiểm thử 

euler_methods.py: phương pháp Euler và Euler cải tiến (Heun). 

p4.py: phương pháp điểm giữa (Midpoint) và phương pháp Ralston. 

 

Công cụ kiểm thử 

Ngôn ngữ lập trình: Python. 

Thư viện kiểm thử: Pytest. 

Thư viện tính toán: NumPy. 

 

Nội dung kiểm thử 

Kiểm tra kết quả với ví dụ minh họa. 

Kiểm tra giá trị ban đầu và tính hữu hạn của kết quả. 

Kiểm tra với hàm có nghiệm đã biết. 

Kiểm tra số bước chia không hợp lệ. 

Kiểm tra trường hợp hàm số trả về giá trị không hữu hạn. 

So sánh độ chính xác của phương pháp Euler cải tiến trong trường hợp phù hợp. 

Kiểm tra các trường hợp cơ bản và trường hợp biên của Midpoint và Ralston. 

 

Kết quả kiểm thử 

Lệnh kiểm thử được sử dụng: 

 

python -m pytest -v 

 

Kết quả thực tế: 12 bài kiểm thử thành công, không có bài kiểm thử thất bại. 

 
