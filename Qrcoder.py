import qrcode
img=qrcode.make("Hello world!")
img.save("BasicQR.png")