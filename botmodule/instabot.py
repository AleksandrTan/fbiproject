"""
The class describes a bot object that simulates user behavior on the Instagram social network.
It is launched from the worker process, initialized, and then, using api,
receives tasks that it performs, accompanying its work with logging at the database level,
a file on the standard output stream.
"""
from apimodule.systemapiwork import SystemApiRequests


class InstaBot:

    def __init__(self, host_proxy: str, port_proxy: int, social_api, system_api, individual_id: int, login_task=True):
        """
        Bot object initialization
        :param host_proxy: str
        :param port_proxy: int
        :param social_api: object
        :param system_api: object
        :param login_task: bool
        individual identifier
        :param individual_id: int
        """
        self.individual_id = individual_id
        self.execution_status = True  # a flag that determines the state of the bot running shutdown
        self.login_task = login_task
        self.host_proxy = host_proxy
        self.port_proxy = port_proxy
        self.social_api = social_api
        self.source_api = system_api

    def start(self):
        pass

    def perform_task(self):
        pass

    def get_new_task(self):
        new_task = self.source_api.get_next_task()
        print(new_task)

    def send_data_api(self):
        pass

    def set_log_record_api(self):
        pass

    def set_log_record_source(self):
        pass


if __name__ == "__main__":
    bot = InstaBot("http://proxyserver.com", 3500, "SocialApiObject", SystemApiRequests(1), 1)
    bot.get_new_task()
