# coding=utf8
import sys;

reload(sys);
sys.setdefaultencoding("utf8")
import pexpect
#
# user = 'yaoxiang.sun'
# ip = '*'
# mypassword = '*'
#
# print user
# child = pexpect.spawn('ssh %s@%s' % (user,ip))
# child.expect ('password:')
# child.sendline (mypassword)
# print 'login ok'
# child.sendline('sudo -i')
# child.expect (':')
# child.sendline (mypassword)
# print 'sudo ok'


ip = '10.21.139.34'
user = 'yaoxiang.sun'
psd = 'datayes@123'
# user = 'lei.ge'
# psd = 'Welcome2015'


file_out = '/datayes/data/mktdata/level2/out/20160322/SH900945'
file_in = '/home/yin.zhang/Bigdata_check'
# file_name = 'Transaction.csv'
file_name = 'MarketData.csv'

smg = "scp " + user + "@" + ip + ":" + file_out + "/" + file_name + " " + file_in + "/" + file_name
print smg
child = pexpect.spawn(smg)
child.expect(user + "@" + ip + "'s password:")
child.sendline(psd)
child.interact()

