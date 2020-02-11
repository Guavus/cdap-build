from exe_cmd.install_cmd import CommandUtil

import getpass

ambari_username = raw_input("Ambari username: ")
ambari_password = getpass.getpass(prompt="Ambari password: ")
ambari_hostname = raw_input("Ambari hostname: ")

if __name__ == '__main__':


    execute_cmd = CommandUtil(ambari_username,ambari_password, ambari_hostname)

    execute_cmd.execute_ambari_config()
