from utils.shell_utils import ShellUtils
from utils.misc_utils import MiscUtil
import logging
from utils.yaml_parser import YmlParser

# Create and configure logger
logging.basicConfig(filename="data/hbase_snapshots.log",
                    format='%(asctime)s %(message)s',
                    filemode='a+')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

class HbaseBackup(object):

    def __init__(self):

        self.shell_obj = ShellUtils()
        self.misc_utils = MiscUtil()
        self.filename1 = "/tmp/out1"
        self.filename = 'data/config.yml'
        self.dict_file = YmlParser().yml_parse()
        self.namespaces = self.dict_file['namespaces']
        print self.namespaces

    def hbase_shell(self,namepsace):

        cmd = "hbase shell <<< \"list '%s.*'\" > /tmp/output.txt" %namepsace
        self.shell_obj.shell_command(cmd)
        logger.info("Executing command %s", cmd)

    def get_list(self):
        f = open("/tmp/output.txt", 'r')
        last_line = f.readlines()[-1]
        ret_array = self.misc_utils.string_to_list(last_line)
        f.close()
        return ret_array

    def hbase_snapshot(self):

        today = self.misc_utils.today_date()
        f = open (self.filename1,'w+')
        ret_array = self.get_list()
        for i in range(0,len(ret_array)):
            test_array = ret_array[i]
            if ":" in test_array:
                test_array = test_array.replace(":",".")
            else:
                pass
            cmd = "snapshot \'%s\', \'%sSnapshot-%s\'" %(ret_array[i],test_array,today)
            f.writelines(cmd)
            f.writelines('\n')
        f.writelines("exit")
        f.close()

    def execute_snapshot_file(self):
        cmd = "/bin/hbase shell %s" %self.filename1
        self.shell_obj.shell_command(cmd)
        logger.info("Executing command %s", cmd)


if __name__ == '__main__':

    hbase_obj = HbaseBackup()
    for i in range(0,len(hbase_obj.namespaces)):

        hbase_obj.hbase_shell(hbase_obj.namespaces[i])
        hbase_obj.hbase_snapshot()
        hbase_obj.execute_snapshot_file()











