import qrcode as qr
img = qr.make("https://www.linkedin.com/in/partha-rakshit/")
img.save("partha_rakshit.png")