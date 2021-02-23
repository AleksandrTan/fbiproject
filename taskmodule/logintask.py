"""
Performs the task of implementing a login on a social network
"""
from apimodule.systemapiwork import SystemApiRequests


class LoginTask:

    def __init__(self, social_api, account_data: dict, individual_bot_id: int):
        self.social_api = social_api
        self.account_data = account_data
        self.individual_id = individual_bot_id

    def run(self, task_id: int) -> dict:
        """
        Run task
        :param task_id: int
        :return: dict
        """
        initialization_parameters = self.initialization_parameters()
        data_result = self.social_api.login(self.account_data, initialization_parameters)
        sys_report = SystemApiRequests(self.individual_id)
        # send report to api
        sys_report.task_report(task_id, data_result)

        return data_result

    def initialization_parameters(self) -> dict:
        """
        Initialization of account parameters for login request
        :return: dict
        """

        params = dict()
        return params
