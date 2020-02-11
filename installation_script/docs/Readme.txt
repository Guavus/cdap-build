############################################################
###### Script is used to run ambari commands from shell ####
############################################################


Prerequisite:

Below python packages are used in script -
1. yaml
2. subprocess
3. getpass
4. logging
5. pexpect
6. ast
7. datetime

It works on python2.7

Install :
In Upgrade doc all the command in section 6 Enabling Configurations will be executed with this script.


1. To change configuration according to setup -
   i) Open file data/config.yml -
      vi data/config.yml

   ii) Change configuration according to setup mostly setup related configuration will be -
       hive.server2.jdbc.url - hive jbdc url -> to be get from ambari -> hive -> HiveServer2 JDBC URL -> copy url and paste in configuration
       node_cluster_name - ambari cluster name -> login to ambari and get cluster name
       program.container.dist.jars - comma (,) seperated keytabs in namespaces used
       install_env -> It takes two values dev or prod . If installing on guavus environment give value as "dev". If installing on JIO environment give value as "prod".
       namespaces -> Value of namespaces to be added to take backup of For Eg- For default namespace provide cdap and for dev_netowrk value would be ["cdap","dev_network"]

2. Command line argument are ambari username, ambari password and ambari hostname.

3. To run scipt you need to execute command -

   python test_install.py

4. Run below script for enabling log rotation on cdap nodes and copying ranger jars to path /opt/cdap/master/ext/security/   ->

   python master_command.py

   Note -> script to be run on both cdap master nodes

5. Run below script to take snapshots of hbase tables -
   Need to run script with hbase user perform below steps to run
   i)    sudo su hbase          (Provide password)
   ii)   klist -kte /etc/security/keytabs/hbase.service.keytab   (Get principal name)
   iii)  kinit -kt /etc/security/keytabs/hbase.service.keytab <principal name get from step ii>
   iv)   python hbase_backup.py

6. Logs can be seen at path -

   data/execution.log
   data/hbase.log
   data/master_commands.log
   data/hbase_snapshots.log

7. Note after execution if you want to delete logs you can delete from above specified location.