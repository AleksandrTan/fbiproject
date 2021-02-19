"""
Performs the subscribe  of implementing a like on a social network
"""


class SubscribeTask:

    def __init__(self, social_api, account_data: dict):
        self.social_api = social_api
        self.account_data = account_data

    def run(self, task_id: int) -> dict:
        """
        Run task
        :param task_id: int
        :return: dict
        """
        data_result = self.social_api.subscribe(self.account_data)

        return data_result
