# coding=utf8
import sys;

reload(sys);
sys.setdefaultencoding("utf8")
import pexpect

if __name__ == '__main__':
    user = 'yaoxiang.sun'
    ip = '*'
    mypassword = '*'

    print user
    child = pexpect.spawn('ssh %s@%s' % (user, ip))
    child.expect('password:')
    child.sendline(mypassword)

    child.expect('$')
    child.sendline('sudo -i')
    child.expect(':')
    child.sendline(mypassword)

    ip = '10.21.139.34'
    user = 'yaoxiang.sun'
    psd = 'datayes@123'
    file_out = '/datayes/data/mktdata/level2/out/20160620/SH900945'
    file_in = '/home/yin.zhang/datayes/data/mktdata/level2/out/20160620/SH900945'
    file_name = 'Transaction.csv'

    smg = "scp " + user + "@" + ip + ":" + file_out + "/" + file_name + " " + file_in + "/" + file_name
    child = pexpect.spawn(smg)
    child.expect(user + "@" + ip + "'s password:")
    child.sendline("datayes@123")
    child.interact()