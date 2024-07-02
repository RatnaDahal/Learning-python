##WIFI link
import qrcode
wifi_type="WPA"
wifi_ssid="iambrp_fpkhr"
wifi_password="password@1234"
wifi=f"WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"
img = qrcode.make('wifi')
type(img)  # qrcode.image.pil.PilImage
img.save("wifi.png")
 