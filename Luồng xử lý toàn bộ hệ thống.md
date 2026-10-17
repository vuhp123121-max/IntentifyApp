ếu ui.py đã hoàn thành phần giao diện, bạn có thể tiếp tục dự án theo lộ trình này:

1. Chốt yêu cầu và luồng sử dụng
   Xác định đầu vào cần hỗ trợ (câu nhập trực tiếp, .txt/.csv, giọng nói), các intent cần nhận diện và cách xử lý câu không thuộc intent nào. Chốt tùy chọn ngôn ngữ đầu vào và ngôn ngữ hiển thị kết quả (Anh/Việt).
2. Kiểm tra dữ liệu
   Xem cấu trúc và nhãn trong data/dataset/example.csv, kiểm tra dữ liệu có đủ ví dụ cho từng intent không, rồi xác định cách chia tập huấn luyện và kiểm tra. Không sửa dữ liệu gốc; nếu cần dữ liệu bổ sung, tạo tệp riêng sau khi thống nhất định dạng.
3. Xây dựng bộ nhận diện
   Bắt đầu với mô hình đơn giản, dễ đánh giá: TF-IDF kết hợp bộ phân loại hoặc so khớp câu tương đồng. Xử lý câu rỗng, nhãn không hợp lệ và trường hợp độ tin cậy thấp.
4. Hoàn thiện train.py và test.py
   train.py đọc dữ liệu và lưu mô hình; test.py đánh giá trên phần dữ liệu tách riêng, báo accuracy và các lỗi phân loại. Chỉ chuyển sang mô hình phức tạp hơn khi có dữ liệu và kết quả đánh giá làm căn cứ.
5. Nối giao diện với phần xử lý
   Thay kết quả mẫu trong ui.py bằng kết quả thật. Nối các nút nhập câu, tải tệp, phân tích hàng loạt và xóa nội dung; hiển thị intent, độ tin cậy và thông tin liên quan nếu mô hình có trả về.
6. Bổ sung nhập liệu theo phạm vi đã chọn
   Làm lần lượt: nhập câu trực tiếp, đọc .txt/.csv, rồi mới thêm giọng nói. Giọng nói cần bước chuyển âm thanh thành văn bản trước khi đưa vào bộ nhận diện.
7. Rà soát trải nghiệm Anh–Việt và lỗi
   Kiểm tra nhãn giao diện, thông báo, lỗi tệp, câu trống và kết quả không chắc chắn ở cả hai ngôn ngữ.
8. Chạy thử toàn bộ luồng
   Thử từng luồng từ giao diện đến kết quả, đối chiếu với test.py, ghi lại lỗi và sửa trước khi đóng gói hoặc viết hướng dẫn chạy trong README.md.
   Trong cấu trúc hiện tại, model.py, train.py, test.py và README.md đang rỗng, nên phần hợp lý để bắt đầu sau khi chốt dữ liệu là xây bộ nhận diện và quy trình đánh giá.
