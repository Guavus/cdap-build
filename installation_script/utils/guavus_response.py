import logging

_LOGGER = logging.getLogger(__name__)


class GuavusResponse(object):
    def __init__(self, stdout, stderr, status_code):
        self.stdout = stdout
        self.stderr = stderr
        self.status_code = status_code