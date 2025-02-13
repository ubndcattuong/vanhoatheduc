import qrcode
from PIL import Image


# URL trỏ đến trang HTML chứa danh sách liên kết
data = "https://ubndcattuong.github.io/datdaimoitruong/"  # Thay bằng URL online nếu đã upload

# Tạo mã QR
qr = qrcode.QRCode(
    version=15,  # Kích thước của mã QR
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Độ bền của mã QR
    box_size=20,  # Kích thước mỗi ô
    border=4,  # Độ dày của biên mã QR
)

qr.add_data(data)
qr.make(fit=True)

# Tạo ảnh mã QR
img = qr.make_image(fill='black', back_color='white')

# Mở hình ảnh bạn muốn chèn vào giữa mã QR
logo = Image.open("D:/QR/logo.png")  # Đảm bảo rằng "logo.png" là đường dẫn đến hình ảnh bạn muốn sử dụng

# Chuyển logo về chế độ RGBA nếu chưa có alpha channel
if logo.mode != 'RGBA':
    logo = logo.convert('RGBA')

# Tính toán kích thước logo để phù hợp với mã QR
qr_width, qr_height = img.size
logo_size = int(qr_width / 4)  # Kích thước logo sẽ chiếm 1/5 chiều rộng của mã QR
logo = logo.resize((logo_size, logo_size))

# Tính toán vị trí để chèn logo vào giữa
logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# Tạo một bản sao của img và chèn logo
img_with_logo = img.convert('RGBA')
img_with_logo.paste(logo, logo_position, logo)  # Sử dụng alpha channel của logo

# Lưu mã QR có hình ảnh
img_with_logo.save("Phòng Đ,Đ, MT.png")

print("Mã QR đã được tạo và lưu thành công!")
