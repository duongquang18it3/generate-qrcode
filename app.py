import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# Hàm để tạo mã QR
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Lấy các tham số từ URL
params = st.experimental_get_query_params()
full_name = params.get('fullName', [''])[0]
whats_app = params.get('whatsApp', [''])[0]
friends = params.get('friends', [''])[0]

# Kiểm tra các tham số và tạo mã QR
if full_name and whats_app and friends:
    qr_code_data = f"{full_name}-{whats_app}-{friends}"
    qr_code_image = generate_qr_code(qr_code_data)
    
    # Chuyển đổi hình ảnh từ PIL sang bytes
    buf = BytesIO()
    qr_code_image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    # Hiển thị mã QR trên Streamlit
    st.image(byte_im, caption=qr_code_data)
else:
    st.write("Missing required parameters: fullName, whatsApp, and friends")

# Để kiểm tra và hiển thị URL hiện tại (hữu ích cho việc debug)
st.write(f"Current URL parameters: {params}")
