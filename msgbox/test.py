# -*- coding: utf-8 -*-
import win32api, win32con

win32api.MessageBox(0, u"正文", u"标题", win32con.MB_YESNO | win32con.MB_ICONQUESTION)