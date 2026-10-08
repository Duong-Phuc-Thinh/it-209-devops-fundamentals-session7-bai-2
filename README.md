# Bài tập 2: Quản trị Tường lửa UFW cho Cụm Dịch vụ Multi-port

Thư mục này chứa cấu hình tường lửa UFW để bảo mật hệ thống máy chủ chạy nhiều cổng dịch vụ đồng thời (SSH, Web, Spring Boot) và chặn cổng cơ sở dữ liệu MySQL từ Internet.

## Chức năng đã thực hiện
1. Thiết lập chính sách mặc định: Chặn toàn bộ lưu lượng đi vào (`deny incoming`), cho phép toàn bộ lưu lượng đi ra (`allow outgoing`).
2. Cho phép kết nối SSH (port `22/tcp`).
3. Cho phép cổng kết nối Web HTTP tiêu chuẩn (port `80/tcp`).
4. Cho phép cổng ứng dụng Spring Boot (port `8082/tcp`).
5. Đảm bảo cổng MySQL (`3306/tcp`) bị chặn hoàn toàn từ Internet bằng cách không thêm luật cho phép (bị chặn tự động bởi chính sách mặc định).

## Hướng dẫn chạy chương trình

Bạn có thể sử dụng script Python `setup_ufw.py` để tự động hóa quá trình cấu hình này.

```bash
# Chạy script cấu hình tự động với quyền root
sudo python3 setup_ufw.py
```

## Kết quả đầu ra mong đợi của lệnh `sudo ufw status verbose`

```text
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    Anywhere
80/tcp                     ALLOW IN    Anywhere
8082/tcp                   ALLOW IN    Anywhere
22/tcp (v6)                ALLOW IN    Anywhere (v6)
80/tcp (v6)                ALLOW IN    Anywhere (v6)
8082/tcp (v6)              ALLOW IN    Anywhere (v6)
```