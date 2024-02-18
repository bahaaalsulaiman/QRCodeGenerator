import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.ERROR_CORRECT_L,   #recomanded to check the documntation of this library
    box_size = 10,
    border=4,

)


qr.add_data("Here you put the link of a website or wep page")
qr.make(fit=True)

img = qr.make_image(fill_color = "green", back_color="white") # specifies the color of theqr and the background color
img.save("bahaa_p.png") #here you save the qr code in the folder of the project
