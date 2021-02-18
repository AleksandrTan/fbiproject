"""
Performs the task of implementing a like on a social network
"""


class LikeTask:

    def __init__(self, social_api, account_data: dict):
        self.social_api = social_api
        self.account_data = account_data

    def run(self) -> dict:
        """
        Run task
        :return: dict
        """
        print("Task start working!!!")
        data_result = self.social_api.login(self.account_data)

        return data_result
