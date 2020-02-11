from utils.shell_utils import ShellUtils

import logging

# Create and configure logger
logging.basicConfig(filename="data/execution.log",
                    format='%(asctime)s %(message)s',
                    filemode='a+')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

class KeytabUtil(object):
    def __init__(self,password):
        self.shell_utils = ShellUtils()
        self.password = password

    def sudo_get_principal(self):
        try:
            cmd = "echo %s | sudo -S -u hbase klist -kte /etc/security/keytabs/hbase.headless.keytab | tail -1 | awk \'{print $4}\'" %self.password
            response = self.shell_utils.shell_command(cmd)
            logging.info("Executing command %s" %cmd)
            principal_name = response.stdout.rstrip('\n')
        except:
            cmd = "sudo -u hbase klist -kte /etc/security/keytabs/hbase.headless.keytab | tail -1 | awk \'{print $4}\'"
            response = self.shell_utils.shell_command(cmd)
            print response
            print type(response)
            logging.info("Executing command %s" % cmd)
            principal_name = response.stdout.rstrip('\n')
        cmd = "sudo -u hbase kinit -kt /etc/security/keytabs/hbase.service %s" %principal_name
        self.shell_utils.shell_command(cmd)
        logging.info("Executing command %s" % cmd)
        logging.info("Principal name is %s") %principal_name