from utils.shell_utils import ShellUtils
from utils.yaml_parser import YmlParser
from utils.dict_utils import DictUtil
import logging

# Create and configure logger
logging.basicConfig(filename="data/execution.log",
                    format='%(asctime)s %(message)s',
                    filemode='a+')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

class CommandUtil(object):



    def __init__(self,ambari_username,ambari_password,ambari_hostname):

        self.filename = 'data/config.yml'
        self.dict_file = self.config_read()
        self.ambari_port = self.dict_file['ambari_port']
        self.node_cluster_name = self.dict_file['node_cluster_name']
        self.protocol_value = self.dict_file['protocol_value']
        self.ambari_admin_user = ambari_username
        self.ambari_admin_password = ambari_password
        self.ambari_host = ambari_hostname
        self.cdap_site = self.dict_file['config']['cdap-site']
        self.cdap_security = self.dict_file['config']['cdap-security']
        self.install_env = self.dict_file['install_env']


    def execute_ambari_config(self):
        obj = ShellUtils()
        for k in self.dict_file['config']:
            for key, value in self.dict_file['config'][k].items():

                if value:
                    dic_utils = DictUtil()
                    if (dic_utils.check_dict(self.dict_file['config'][k][key]) and key == self.install_env):
                        arr_recur = dic_utils.get_key_value(self.dict_file['config'][k][key])
                        for i in range(0, len(arr_recur)):
                            config_key = arr_recur[i][0]
                            config_value = arr_recur[i][1]
                            cmd = "/var/lib/ambari-server/resources/scripts/configs.py -t %s -s %s -a set -u %s -p %s -l %s -n %s -c %s -k %s -v \'%s\'" % (
                            self.ambari_port, self.protocol_value, self.ambari_admin_user, self.ambari_admin_password,
                            self.ambari_host, self.node_cluster_name, k, config_key, config_value)
                            logging.info("Executing command : %s" % cmd)

                    elif (dic_utils.check_dict(self.dict_file['config'][k][key])) == False:
                          config_key = key
                          config_value = value
                          cmd = "/var/lib/ambari-server/resources/scripts/configs.py -t %s -s %s -a set -u %s -p %s -l %s -n %s -c %s -k %s -v \'%s\'" % (
                          self.ambari_port, self.protocol_value, self.ambari_admin_user, self.ambari_admin_password,
                          self.ambari_host, self.node_cluster_name, k, config_key, config_value)
                          logging.info("Executing command : %s" % cmd)


                    response = obj.shell_command(cmd)
                    logging.error("Error while executing is %s" %response.stderr)
                    logging.debug("Stdout while executing is %s" %response.stdout)
                    logging.info("Response code of command executed is %s" %response.status_code)
                    logging.debug("Complete response is %s" %response)


        return response

    def config_read(self):

        response = YmlParser().yml_parse()
        return response
