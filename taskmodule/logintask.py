"""
Performs the task of implementing a login on a social network
Parameters and headers are pre-initialized. Prerequisites for initializing the device
and the login request itself are performed.
"""
from apimodule.systemapiwork import SystemApiRequests


class LoginTask:

    def __init__(self, social_api, account_data: dict, individual_bot_id: int):
        self.social_api = social_api
        self.account_data = account_data
        self.individual_id = individual_bot_id

    def run(self, task_id: int, authorization_data: dict) -> dict:
        """
        Run task
        :param authorization_data: dict
        :param task_id: int
        :return: dict
        """
        data = dict()
        print(self.account_data)
        # initialize request parameters
        initialization_parameters = self.initialization_parameters()

        # initialize request headers
        initialization_headers = self.initialization_headers()

        # run pre-requests
        pre_requests = self.run_pre_requests()

        # run login
        data = self.social_api.login(self.account_data, initialization_parameters, initialization_headers)
        sys_report = SystemApiRequests(self.individual_id)
        # send report to api
        sys_report.task_report(task_id, data)

        return data

    def initialization_parameters(self) -> dict:
        """
        Initialization of account parameters for login request
        :return: dict
        """

        params = dict()
        return params

    def initialization_headers(self) -> dict:
        """
        Initialization of headers parameters for login request
        :return: dict
        """

        headers = dict()
        return headers

    def run_pre_requests(self):
        """
        Run pre requests
        :return: bool
        """
        return True
