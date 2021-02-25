"""
Performs the task of implementing a login on a social network
Parameters and headers are pre-initialized. Prerequisites for initializing the device
and the login request itself are performed.
"""
from pprint import pprint

from core.initheaders import InitHeaders
from core.initparams import InitParams


class LoginTask:
    """
    The first request to the api of instagram. If parameters csrftoken, mid, ig_did are passed,
    initialize InitParams with existing ones, if not,
    after pre-requests, transfer them to the system api server.
    """

    def __init__(self, social_api, account_data: dict, individual_bot_id: int):
        self.social_api = social_api
        self.account_data = account_data
        self.individual_id = individual_bot_id

    def run(self, task_id: int, initialization_parameters: dict) -> dict:
        """
        Run task
        :param initialization_parameters:
        :param task_id: int
        :return: dict
        """
        data = dict()
        initialization_parameters = self.initialization_parameters(initialization_parameters)
        print(initialization_parameters.mid)

        # initialize request headers
        initialization_headers = self.initialization_headers(initialization_parameters)

        # run pre-requests
        # these requests are desirable and in addition,
        # the request will allow you to get the parameter cookie - csrftoken from the api
        pre_requests = self.social_api.run_pre_requests(initialization_parameters, initialization_headers)
        print(initialization_parameters.mid)

        # run login
        # data = self.social_api.login(self.account_data, initialization_parameters, initialization_headers)
        # sys_report = SystemApiRequests(self.individual_id)
        # send report to api
        # sys_report.task_report(task_id, data)

        return data

    def initialization_parameters(self, initialization_parameters: dict) -> object:
        """
        Initialization of account parameters for login request
        :return: dict
        """
        params = InitParams(self.account_data, initialization_parameters)
        return params

    def initialization_headers(self, initialization_parameters: object) -> dict:
        """
        Initialization of headers parameters for login request
        :param initialization_parameters: dict
        :return: dict
        """
        headers = InitHeaders(initialization_parameters)
        return headers.get_headers()
