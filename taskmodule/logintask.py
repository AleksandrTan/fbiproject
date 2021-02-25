"""
Performs the task of implementing a login on a social network
Parameters and headers are pre-initialized. Prerequisites for initializing the device
and the login request itself are performed.
"""
from pprint import pprint

from core.initheaders import InitHeaders
from core.initparams import InitParams


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
        # initialize request parameters
        initialization_parameters = self.initialization_parameters()
        pprint(dir(initialization_parameters))

        # initialize request headers
        initialization_headers = self.initialization_headers(initialization_parameters)
        pprint(initialization_headers)
        # run pre-requests
        # these requests are desirable and in addition,
        # the request will allow you to get the parameter cookie - csrftoken from the api
        # pre_requests = self.social_api.run_pre_requests(initialization_parameters)

        # run login
        # data = self.social_api.login(self.account_data, initialization_parameters, initialization_headers)
        # sys_report = SystemApiRequests(self.individual_id)
        # send report to api
        # sys_report.task_report(task_id, data)

        return data

    def initialization_parameters(self) -> object:
        """
        Initialization of account parameters for login request
        :return: dict
        """
        params = InitParams(self.account_data)
        return params

    def initialization_headers(self, initialization_parameters: object) -> dict:
        """
        Initialization of headers parameters for login request
        :param initialization_parameters: dict
        :return: dict
        """
        headers = InitHeaders(initialization_parameters)
        return headers.get_headers()
