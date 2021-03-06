"""
The class describes a bot object that simulates user behavior on the Instagram social network.
It is launched from the worker process, initialized, and then, using api,
receives tasks that it performs, accompanying its work with logging at the database level,
a file on the standard output stream.
"""
import sys
import time

from logsource.logconfig import logger
from taskmodule.inittask import InitTasks
from apimodule.systemapiwork import SystemApiRequests
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
        individual bot identifier
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
        self.authorization_data = dict()
        self.tasks = InitTasks(self.host_proxy, self.port_proxy, self.individual_id, self.account_data)
        self.task_objects = self.tasks.get_init_tasks()
        self.session_parameters = dict()  # account session parameters for a work session

    def start(self):
        logger.warning(f"Bot {self.individual_id} start working!!!")
        # log in to the social network
        if self.login_task:
            data_authorization = self._perform_task(self.task_objects['login'], 0)
            if not data_authorization['status']:
                sys.stdout.write(f"The authorization process for the bot"
                                 f" number {self.individual_id} was not correct.!!!")
                logger.warning(f"The authorization process for the bot number {self.individual_id} was not correct.!!!")
                return
            self.authorization_data = data_authorization["authorization_data"]

        while self.execution_status:
            new_task = self._get_new_task()

            if new_task["status"]:
                # run new task
                sys.stdout.write(f"Task {new_task['task_name']} is running!\n")
                self._perform_task(self.task_objects[new_task["task_name"]], new_task['task_id'])
                continue

            elif new_task["error"]:
                sys.stdout.write("Server error!!!\n")
                time.sleep(10)
                continue

            else:
                sys.stdout.write("No tasks, I work autonomously!\n")
                self._perform_task(self.task_objects["flipping_tape"], 3)
                time.sleep(10)
                continue

    def _perform_task(self, task_object, task_id):
        data_task = task_object.run(task_id, self.authorization_data)
        time.sleep(10)
        return data_task

    def _get_new_task(self) -> dict:
        new_task = self.system_api.get_new_task()

        return new_task

    def _send_data_api(self, data):
        logger.warning(f"Bot {data} start working!!!")

    def _set_log_record_api(self):
        pass


if __name__ == "__main__":
    bot = InstaBot("http://localhost", 3500, InstagramRequestsWeb("http://localhost", 8000),
                   SystemApiRequests(1), 1, {"username": "rumych2013@gmail.com", "password": 1234567})
    bot.start()
