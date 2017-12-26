# coding=utf8
import sys;

reload(sys);
sys.setdefaultencoding("utf8")
import os


class RemoteShell:
    def __init__(self, host, user, pwd):
        self.host = host
        self.user = user
        self.pwd = pwd


    def put(self, local_path, remote_path):
        scp_put = '''
        set timeout -1
        spawn scp %s %s@%s:%s
        expect "(yes/no)?" {
        send "yes\r"
        expect "password:"
        send "%s\r"
        } "password:" {send "%s\r"}
        expect eof
        exit'''
        os.system("echo '%s' > scp_put.cmd" % (
        scp_put % (os.path.expanduser(local_path), self.user, self.host, remote_path, self.pwd, self.pwd)))
        os.system('expect scp_put.cmd')
        os.system('rm scp_put.cmd')