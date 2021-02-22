"""
Performs the subscribe  of implementing a like on a social network
"""
from apimodule.systemapiwork import SystemApiRequests


class SubscribeTask:

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
        data_result = self.social_api.subscribe({}, authorization_data)
        sys_report = SystemApiRequests(self.individual_id)
        # send report to api
        sys_report.task_report(task_id, data_result)

        return data_result
