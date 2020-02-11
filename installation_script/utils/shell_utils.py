import logging
import subprocess
from guavus_response import GuavusResponse

_LOGGER = logging.getLogger(__name__)

class ShellUtils(object):
    """Utilities related to linux shell."""

    def shell_command(self,command):
        """Execute command on shell

        :param command: Command that needs to be executed
        :return: output of command executed on shell
        """
        proc = subprocess.Popen(command,stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        response = proc.communicate()
        guavus_response = GuavusResponse(response[0].strip(), response[1], proc.returncode)
        return guavus_response
