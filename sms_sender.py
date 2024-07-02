import qrcode
phone="9864281567"
message="hello, how are you?"
sms=f"SMSTO:{phone}:{message}"
img = qrcode.make('sms')
type(img)  # qrcode.image.pil.PilImage
img.save("sms.png")
 