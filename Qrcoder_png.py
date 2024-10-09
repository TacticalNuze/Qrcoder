import qrcode


qr=qrcode.QRCode(version=1,box_size=20,border=1)
qr.add_data("Hello World")
qr.make()
img=qr.make_image()
img.show()
img.save("BasicQR.png")

