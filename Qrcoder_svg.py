import qrcode.image.svg

factory=qrcode.image.svg.SvgPathImage
svg_img=qrcode.make("Hello world",image_factory=factory)
svg_img.save("Basic_qr.svg")

