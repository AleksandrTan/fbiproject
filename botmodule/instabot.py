"""
The class describes a bot object that simulates user behavior on the Instagram social network.
It is launched from the worker process, initialized, and then, using api,
receives tasks that it performs, accompanying its work with logging at the database level,
a file on the standard output stream.
"""


class InstaBot:

    def __init__(self, host_proxy, port_proxy, social_api, source_api, login_task=True):
        """
        Bot object initialization
        :param host_proxy: str
        :param port_proxy: int
        :param social_api: object
        :param source_api: object
        :param login_task: bool
        """
        self.execution_status = True
        self.login_task = login_task
        self.host_proxy = host_proxy
        self.port_proxy = port_proxy
        self.social_api = social_api
        self.source_api = source_api

    def start(self):
        pass

    def perform_task(self):
        pass

    def get_new_task(self):
        pass

    def send_data_api(self):
        pass

    def set_log_record_api(self):
        pass

    def set_log_record_source(self):
        pass
