import pexpect
from pexpect import pxssh
import re

class PexpectUtil( object ):


    def __init__(self, ssh_user , ssh_password):
        self.ssh_user = ssh_user
        self.ssh_password = ssh_password


    def pexpect_cmd(self,cmd, ssh_hostname):
        print cmd
        print ssh_hostname
        child = pexpect.spawn('ssh -o StrictHostKeyChecking=no %s@%s' %(self.ssh_user, ssh_hostname))
        child.logfile = open("data/remote.log", "a+")
        try:
            child.expect(['.*assword:.*'])
            child.sendline(self.ssh_password)
            child.expect(['.*$'])
        except:
            child.expect(['.*$'])
        print "executing command : %s" %cmd
        child.sendline(cmd)
        child.expect(['.*$'],timeout=1000)
        child.sendline('exit')
        child.expect(['.*$'])

    def pxssh_cmd(self,cmd,ssh_hostname):

        try:
            s = pxssh.pxssh(options={"StrictHostKeyChecking": "no"})
            s.login(ssh_hostname, self.ssh_user, self.ssh_password)
            s.sendline(cmd)  # run a command
            rootprompt = re.compile('.*[$#]')
            i = s.expect([rootprompt, 'assword.*: '])
            if i == 0:
                print "Didn't need password"
            elif i==1 :
                s.sendline(self.ssh_password)
                j = s.expect([rootprompt, 'Sorry, try again'])
                if j == 0:
                    pass
                elif j==1:
                    raise Exception("bad password")
            else:
                raise Exception("unexpected output")
            s.set_unique_prompt()
            s.logout()

        except pxssh.ExceptionPxssh as e:
            print("pxssh failed on login.")
            print e

    def pexpect_scp(self,cmd, hostname):

        try:
            var_child = pexpect.spawn(cmd)
            i = var_child.expect([".*assword.*"])
            if i == 0:
                var_child.sendline(self.ssh_password)
                j = var_child.expect([".*password.*"])
                if j == 0:
                    var_child.sendline(self.ssh_password)
                    var_child.expect(pexpect.EOF)
                elif j == 1:
                    pass
            elif i == 1:
                print "Got the key or connection timeout"

        except Exception as e:
            print "Oops Something went wrong buddy"
            print e