import qrcode.image.svg
import os

current_file_path = os.path.abspath(__file__)
directory_path = os.path.dirname(current_file_path)
directory_path = os.path.dirname(directory_path)

factory=qrcode.image.svg.SvgPathImage
svg_img=qrcode.make("Hello world",image_factory=factory)
svg_img.save(f"{directory_path}/Output/Basic_qr.svg")

