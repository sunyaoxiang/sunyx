# coding=utf-8
import os
import re
import time
import email
import poplib
import imaplib
import cStringIO
import base64


host = "imap.datayes.com";
port = "143";
# port = "995";
conn = imaplib.IMAP4(host, port)
usr = "service.data@datayes.com";
pwd = "Wmcl0ud.com@123";
conn.login(usr, pwd)
conn.select("INBOX", readonly=True)
# t = conn.list()
# for t in conn.list()[1]:
# print t
# t = conn.select("Notes", readonly=True)
# print t[1][0]
# for i in conn.search(None, "ALL")[1]:
#     # print conn.fetch(i)
# typ,data = conn.fetch(t[1][0], "(RFC822)")
try:
    typ, data = conn.search(None, 'ALL')
    print typ, data
    for msg_dataz in data[0].split():
        print msg_dataz
        type, msg_data = conn.fetch(msg_dataz, '(RFC822)')
        msg = email.message_from_string(msg_data[0][1])
        # print msg._payload.get_payload(decode=True)
        print msg._headers[0][1]  #邮件发送人
        for part in msg.walk():
            if not part.is_multipart():
                content = part.get_payload(decode=True)
                print content




except Exception, e:
    print e;
    print "no email exist!"