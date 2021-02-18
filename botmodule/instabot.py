"""
The class describes a bot object that simulates user behavior on the Instagram social network.
It is launched from the worker process, initialized, and then, using api,
receives tasks that it performs, accompanying its work with logging at the database level,
a file on the standard output stream.
"""
import time

from logsource.logconfig import logger
from apimodule.systemapiwork import SystemApiRequests
from taskmodule.logintask import LoginTask
from taskmodule.liketask import LikeTask
from socialapimodule.instarequestweb import InstagramRequestsWeb


class InstaBot:

    def __init__(self, host_proxy: str, port_proxy: int, social_api: object, system_api: object, individual_id: int,
                 account_data: dict, login_task=True):
        """
        Bot object initialization
        :param host_proxy: str
        :param port_proxy: int
        :param social_api: object InstagramRequestsWeb or InstagramRequestsMobile
        :param system_api: object SystemApiRequests
        :param login_task: bool
        individual identifier
        :param individual_id: int
        :param account_data: dict
        """
        self.individual_id = individual_id
        self.execution_status = True  # a flag that determines the state of the bot running shutdown
        self.login_task = login_task
        self.host_proxy = host_proxy
        self.account_data = account_data
        self.port_proxy = port_proxy
        self.social_api = social_api
        self.system_api = system_api
        self.task_objects = dict({"login": LoginTask(self.social_api, self.account_data),
                                  "like": LikeTask(social_api, self.account_data)})

    def start(self):
        logger.warning(f"Bot {self.individual_id} start working!!!")
        while self.execution_status:
            new_task = self.get_new_task()
            print(new_task)
            if new_task["status"]:
                # run new task
                self.perform_task(self.task_objects[new_task["task_name"]])
            else:
                time.sleep(10)

    def perform_task(self, task_object):
        data_result = task_object.run()
        print(data_result)
        time.sleep(10)
        return True

    def get_new_task(self) -> dict:
        new_task = self.system_api.get_next_task()

        return new_task

    def send_data_api(self):
        pass

    def set_log_record_api(self):
        pass

    def set_log_record_source(self):
        pass


if __name__ == "__main__":
    bot = InstaBot("http://localhost", 3500, InstagramRequestsWeb("http://localhost", 8000),
                   SystemApiRequests(1), 1, {"login": "rumych2013@gmail.com", "password": 1234567})
    bot.start()
