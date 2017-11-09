# -*- coding: utf-8 -*-
import qrcode


class make_png(object):

    def __init__(self,url):
        self.url = url
        # print url

    def get_png(self,name):
        qr = qrcode.QRCode(version= None)
        qr.add_data(self.url)
        qr.make(fit=True)
        img = qr.make_image()
        img.save("{}.png".format(name))

url = "https://github.com/rainyear/pytips/blob/master/Markdowns/{}.md".format("2016-05-11-Floating-Point-Arithmetic")
a = make_png(url).get_png("abc")
b = make_png(url).get_png
b("cash")
pass