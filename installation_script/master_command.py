
from utils.shell_utils import ShellUtils


import logging

# Create and configure logger
logging.basicConfig(filename="data/master_commands.log",
                    format='%(asctime)s %(message)s',
                    filemode='a+')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

class master_command(object):
    def __init__(self):
        self.shell_obj = ShellUtils()

    def enable_rotation(self):
        cmd = 'chmod 0644 /etc/logrotate.d/cdap'
        logging.info("Executing command : %s on remote node" % cmd)
        self.shell_obj.shell_command(cmd)
        cmd = '/usr/sbin/logrotate -d /etc/logrotate.d/cdap'
        logging.info("Executing command : %s" % cmd)
        self.shell_obj.shell_command(cmd)


    def ranger_jar(self):
        cmd = "sudo rm -rf /opt/cdap/master/ext/security/*"
        logging.info("Executing command : %s" % cmd)
        self.shell_obj.shell_command(cmd)
        cmd = "sudo cp /tmp/security/*  /opt/cdap/master/ext/security/"
        logging.info("Executing command : %s" % cmd)
        self.shell_obj.shell_command(cmd)
        cmd = "sudo chown cdap:cdap -R /opt/cdap/master/ext/security/"
        logging.info("Executing command : %s" % cmd)
        self.shell_obj.shell_command(cmd)


if __name__ == '__main__':

    master_cmd = master_command()
    master_cmd.enable_rotation()
    master_cmd.ranger_jar()