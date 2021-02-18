"""
Performs the task of implementing a login on a social network
"""


class LoginTask:

    def __init__(self, social_api, account_data: dict):
        self.social_api = social_api
        self.account_data = account_data

    def run(self):
        print("Task start working!!!")
        self.social_api.login(self.account_data)
