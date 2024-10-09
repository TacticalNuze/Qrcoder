import qrcode
import os


current_file_path = os.path.abspath(__file__)
directory_path = os.path.dirname(current_file_path)
directory_path = os.path.dirname(directory_path)

qr=qrcode.QRCode(version=1,box_size=20,border=1)
qr.add_data("www.google.com")
qr.make()
img=qr.make_image()
img.show()
img.save(f"{directory_path}/Output/BasicQR.png")

