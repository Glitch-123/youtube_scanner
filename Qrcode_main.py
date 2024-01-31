import qrcode as qr

img = qr.make("https://www.youtube.com/") # make() QR code ko bnanae ka kaam karega.
img.save("youtube_QRcode_image.png")  # save() humare QR code ko png format mai dega. image ka dot extension hota hai hum png ka use krenge.
#image save hori hai is name sai or kis format mai krni hai png toh png dediya.

