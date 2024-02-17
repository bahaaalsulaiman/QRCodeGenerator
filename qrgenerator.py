import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.ERROR_CORRECT_L,
    box_size = 10,
    border=4,

)


qr.add_data("https://github.com/bahaaalsulaiman")
qr.make(fit=True)

img = qr.make_image(fill_color = "green", back_color="white")
img.save("bahaa_p.png")
