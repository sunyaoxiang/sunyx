# -*- coding: utf-8 -*-
import qrcode


qr = qrcode.QRCode(version= None)

qr.add_data("yes man")
qr.make(fit=True)
img = qr.make_image()
img.save("see.png")