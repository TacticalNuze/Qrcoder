import qrcode
import os

current_file_path = os.path.abspath(__file__)
directory_path = os.path.dirname(current_file_path)
directory_path = os.path.dirname(directory_path)

def Qr_png(data,box_size=2,border=1):
    qr=qrcode.QRCode(box_size,border)
    qr.add_data(data)
    qr.make()
    img=qr.make_image()
    return img

def Qr_svg(data):
    factory=qrcode.image.svg.SvgPathImage
    svg_img=qrcode.make("Hello world",image_factory=factory)
    return svg_img


