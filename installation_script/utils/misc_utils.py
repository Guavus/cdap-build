import ast
import datetime
from utils.shell_utils import ShellUtils

class MiscUtil(object):

    def __init__(self):
        pass

    def string_to_list(self, str_cvrt):
        ret_array = ast.literal_eval(str_cvrt)
        return ret_array

    def today_date(self):
        today = datetime.date.today().strftime("%d%m%Y")
        return today

    def get_hostname(self):
        shell_util = ShellUtils()
        cmd = hostname -A
        response = shell_util.shell_command(cmd)
        return response.stdout