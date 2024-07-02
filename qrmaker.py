import qrcode
img = qrcode.make('Ratna Dahal')
type(img)  # qrcode.image.pil.PilImage
img.save("ratna.png")
 